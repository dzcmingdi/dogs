import argparse
import os
import sys
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
import torchvision.io

from detect import run
from models.common import DetectMultiBackend
from utils.datasets import IMG_FORMATS, VID_FORMATS, LoadImages, LoadStreams
from utils.general import (LOGGER, check_file, check_img_size, check_imshow, check_requirements, colorstr,
                           increment_path, non_max_suppression, print_args, scale_coords, strip_optimizer, xyxy2xywh)
from utils.plots import Annotator, colors, save_one_box
from utils.torch_utils import select_device, time_sync
import torchvision.transforms.functional


def inference(model, imgsz, filename, device):
    model.model.float()
    stride, names, pt, jit, onnx = model.stride, model.names, model.pt, model.jit, model.onnx
    imgsz = check_img_size(imgsz, s=stride)  # check image size
    dataset = LoadImages(filename, img_size=imgsz,
                         stride=stride, auto=pt and not jit)

    for path, im, im0s, vid_cap, s in dataset:
        im = torch.from_numpy(im).to(device)
        im = im.float()  # uint8 to fp16/32
        im /= 255  # 0 - 255 to 0.0 - 1.0
        if len(im.shape) == 3:
            im = im[None]  # expand for batch dim

        # Inference
        pred = model(im, augment=False, visualize=False)

        # NMS
        pred = non_max_suppression(pred, 0.5, 0.45, None, False, max_det=1000)
        
        if pred[0].size(0) == 0:
            return im,[]
        # Second-stage classifier (optional)
        # pred = utils.general.apply_classifier(pred, classifier_model, im, im0s)

        # Process predictions
        p, im0, frame = path, im0s.copy(), getattr(dataset, 'frame', 0)

        for i, det in enumerate(pred):  # per image
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(im.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                # Write results
                xywhs = []
                for *xyxy, conf, cls in reversed(det):
                    xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                    xywhs.append(xywh)
                return im[0], xywhs


if __name__ == '__main__':
    device = torch.device('cuda')
    weights = './runs/train/exp13/weights/best.pt'
    imgsz = 224
    root = '../stanford-dog/test/images'
    crop = '../stanford-dog/test/crops'
    for i in os.listdir(root)[3:]:
        root_i = os.path.join(root, i)
        if not Path(os.path.join(crop, i)).exists():
            os.mkdir(os.path.join(crop, i))
        files = os.listdir(root_i)
        for j in files:
            root_ij = os.path.join(root_i, j)
            xy_whs = inference(weights, 224, root_ij)
            image = torchvision.io.read_image(root_ij)
            if xy_whs is None:
                continue
            try:
                for xy_wh in xy_whs:
                    x, y, w, h = (xy_wh[0] - xy_wh[2] / 2) * image.size(2), (xy_wh[1] - xy_wh[3] / 2) * image.size(1), \
                                 xy_wh[2] * image.size(2), xy_wh[3] * image.size(1)
                    x, y, w, h = int(x), int(y), int(w), int(h)
                    image = torchvision.transforms.functional.crop(image, y, x, h, w)
                    if image.size(1) < 100 or image.size(2) < 100:
                        continue
                    torchvision.io.write_jpeg(image, os.path.join(crop, i, j))
            except:
                continue
