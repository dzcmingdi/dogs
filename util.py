import os
import xml.dom.minidom
from pathlib import Path
from dog_detect import inference
import pandas
import torch
import torchvision
import torchvision.transforms.functional


def readxml(filename):
    dom_tree = xml.dom.minidom.parse(filename)
    annotation = dom_tree.documentElement
    folder_name = annotation.getElementsByTagName('folder')[0].childNodes[0].data
    image_filename = annotation.getElementsByTagName('filename')[0].childNodes[0].data
    class_name = annotation.getElementsByTagName('object')[0].childNodes[1].childNodes[0].data
    obj = annotation.getElementsByTagName('object')[0]
    bndboxes = obj.getElementsByTagName('bndbox')[0]
    xmin = bndboxes.getElementsByTagName('xmin')[0].childNodes[0].data
    ymin = bndboxes.getElementsByTagName('ymin')[0].childNodes[0].data
    xmax = bndboxes.getElementsByTagName('xmax')[0].childNodes[0].data
    ymax = bndboxes.getElementsByTagName('ymax')[0].childNodes[0].data

    return image_filename, class_name, [xmin, ymin, xmax, ymax]


def extract():  # 从原图像提取狗
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
            xy_whs = inference(weights, 224, root_ij, device)
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


def to_this_yolo_csv():  # 修改数据格式以适配该yolo实现
    root_path = '../data/datasets/dogs_detection'
    base_path = '../data/datasets/dogs_detection/annotations'
    image_path = '../data/datasets/dogs_detection/images'
    idx = 0

    data = []
    for i in os.listdir(base_path):
        image_filename, class_name, boxes = readxml(os.path.join(base_path, i))
        if class_name == 'cat':
            continue

        os.rename(os.path.join(image_path, image_filename), os.path.join(root_path, 'new_images', f"{idx}.png"))
        data.append([f"{idx}.png", boxes[0], boxes[1], boxes[2], boxes[3]])
        idx += 1

    data_frames = pandas.DataFrame(data, columns=['filename', 'xmin', 'ymin', 'xmax', 'ymax'])
    data_frames.to_csv(os.path.join(root_path, 'labels.csv'))
