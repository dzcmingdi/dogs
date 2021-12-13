import torchvision
import torch
import torch.utils.data
import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
from torch.utils import data


@torch.no_grad()
def init_weights(m):
    if type(m) == torch.nn.Linear or type(m) == torch.nn.Conv2d:
        torch.nn.init.xavier_uniform_(m.weight)


class DogClassify:
    def __init__(self, sequential, optimizer, scheduler, train_iter, epochs, device):
        self.sequential = sequential
        self.optimizer = optimizer
        self.scheduler = scheduler
        self.train_iter = train_iter
        self.epochs = epochs
        self.device = device
        self.loss = torch.nn.CrossEntropyLoss()

    def train(self):
        self.sequential.train(True)
        self.sequential.to(self.device)
        for e in range(self.epochs):
            for batch, (x, y) in enumerate(self.train_iter):
                x, y = x.to(self.device), y.to(self.device)
                y_pred = self.sequential(x)
                l = self.loss(y_pred, y)
                self.optimizer.zero_grad()
                l.backward()
                self.optimizer.step()
                with torch.no_grad():
                    corrects = (torch.argmax(y_pred, dim=1) == y).sum().item()
                    print("\r", f"epoch: {e} loss: {l.item()} ", f"lr: {self.scheduler.get_last_lr()} ",
                          f"accuracies: {corrects} / {len(x)}",
                          f" [{batch * len(x):>5d}/{len(self.train_iter.dataset):>5d}]",
                          end='')
            self.scheduler.step()


if __name__ == '__main__':
    transformer = torchvision.transforms.Compose([
        torchvision.transforms.Resize((224, 224)),
        torchvision.transforms.ToTensor(),

    ])

    train_dataset = torchvision.datasets.ImageFolder(root='../out/data/datasets/crops'
                                                     , transform=transformer
                                                     )

    c = len(train_dataset.classes)

    train_iter = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True)
    # sequential = torchvision.models.resnet101(pretrained=True)
    sequential = torch.load('./dog_classify.pt')

    # sequential.fc = torch.nn.Linear(sequential.fc.in_features, c)
    lr = 1e-3

    params_non_output = [param for name, param in sequential.named_parameters()
                         if name not in ["fc.weight", "fc.bias"]
                         ]
    optimizer = torch.optim.SGD(
        [{'params': params_non_output, 'lr': lr}, {'params': sequential.fc.parameters(), 'lr': 0.1}], lr=lr)

    # optimizer = torch.optim.SGD(sequential.parameters(), lr=lr)
    epochs = 1
    scheduler = torch.optim.lr_scheduler.ConstantLR(optimizer, 1.0)
    device = torch.device('cuda')
    dog_train = DogClassify(sequential, optimizer, scheduler, train_iter, epochs, device)
    dog_train.train()
    torch.save(sequential, f='dog_classify.pt')
