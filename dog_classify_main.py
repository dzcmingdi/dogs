import matplotlib
import torch
import torchvision.transforms.functional

from dog_detect import inference
from models.experimental import attempt_load
from models.common import DetectMultiBackend
import matplotlib.pyplot as plot
from dog_classify import classify

matplotlib.use('TkAgg')


class DogClassify:
    def __init__(self):
        self.device = torch.device('cpu')
        
        self.classify_sequential = torch.load('./out/data/models/dog_classify_resnet101_e30_validate81.pt', self.device)
        self.detect_sequential = DetectMultiBackend('./out/data/models/dog_detection_mAP50_93.pt', device=self.device, dnn=False)

    def classify(self,filename):
        # image是原始图像
        print(filename)
        image, boxes = inference(self.detect_sequential, imgsz=224, filename=filename, device=self.device)
        if boxes is None or len(boxes) == 0:
            return [-1]
        labels = []
        for box in boxes:
            x, y, w, h = (box[0] - box[2] / 2) * image.size(2), (box[1] - box[3] / 2) * image.size(1), \
                         box[2] * image.size(2), box[3] * image.size(1)
            x, y, w, h = int(x), int(y), int(w), int(h)
            image_c = torchvision.transforms.functional.crop(image, y, x, h, w)
            label = classify(self.classify_sequential, image_c)
            labels.append(label)
        return labels, boxes


