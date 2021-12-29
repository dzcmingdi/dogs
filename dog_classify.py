import os

import torch
import torch.nn.functional as f
import torchvision
from dog_detect import inference
from models.common import DetectMultiBackend
import torchvision.transforms.functional
import cv2 as cv
from util import ratio_transform


class DogClassify:
    def __init__(self):
        self.device = torch.device('cpu')

        self.classify_sequential = torch.load('./out/data/models/dog_classify_resnet50_e50_test83.pt', self.device)
        self.detect_sequential = DetectMultiBackend('./out/data/models/dog_detection_mAP50_93_imgsz_224.pt',
                                                    device=self.device,
                                                    dnn=False)

    def classify(self, filename):
        # image是原始图像
        all_boxes = []
        images = []
        for f in filename:
            image, boxes = inference(self.detect_sequential, imgsz=224, filename=f, device=self.device)
            images.append(image)
            all_boxes.append(boxes)

        all_labels = []
        all_crop_images = []
        for boxes, image in zip(all_boxes, images):
            labels = []
            crop_images = []
            origin_image = image.copy()
            for i, box in enumerate(boxes):
                x, y, w, h = (box[0] - box[2] / 2) * image.shape[1], (box[1] - box[3] / 2) * image.shape[0], \
                             box[2] * image.shape[1], box[3] * image.shape[0]
                x, y, w, h = int(x), int(y), int(w), int(h)
                image_c = torchvision.transforms.functional.crop(torch.tensor(origin_image).permute(2, 0, 1), y, x, h,
                                                                 w).float() / 255.

                crop_image = (torch.clone(image_c) * 255).byte().permute(1, 2, 0).numpy()
                import numpy
                crop_image = numpy.ascontiguousarray(crop_image)

                image = cv.rectangle(image, (int(x), int(y)), (int(x + w), int(y + h)),
                                     (0, 128, 0),
                                     thickness=5)
                label = self.classify_inference(self.classify_sequential, image_c)
                image = cv.putText(image, str(i), (int(x), int(y)), cv.FONT_HERSHEY_PLAIN, 3.,
                                   (0, 0, 255), 3)

                labels.append(label)
                crop_images.append(crop_image)
            all_labels.append(labels)
            all_crop_images.append(crop_images)
        return all_labels, images, all_crop_images

    def classify_inference(self, classify_sequential, image):
        sequential = classify_sequential
        sequential.eval()
        # transformer = torchvision.transforms.Compose([
        #     torchvision.transforms.Resize((224, 224)),
        # ])
        transformer = torchvision.transforms.Compose([
            ratio_transform,
            torchvision.transforms.Resize((224, 224)),

        ])
        image = transformer(image).unsqueeze(0)
        y_pred = sequential(image)
        y_pred = f.softmax(y_pred, dim=1)
        return torch.argmax(y_pred, dim=1).squeeze().item()
