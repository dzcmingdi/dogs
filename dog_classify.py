import torch
import torchvision
import torch.utils.data
import torch.nn.functional as f


def classify(classify_sequential, image):
    sequential = classify_sequential
    sequential.eval()
    transformer = torchvision.transforms.Compose([
        torchvision.transforms.Resize((224, 224)),
    ])
    image = transformer(image).unsqueeze(0)
    y_pred = sequential(image)
    y_pred = f.softmax(y_pred, dim=1)
    return torch.argmax(y_pred, dim=1).squeeze().item()
