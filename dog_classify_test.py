import torch
import torchvision
import torch.utils.data
import torch.nn.functional as f


class DogTest:
    def __init__(self, sequential, test_iter, device, epochs):
        self.sequential = sequential
        self.test_iter = test_iter
        self.device = device
        self.epochs = epochs

    def test(self):
        c_sum, n_sum = 0, 0
        for x, y in self.test_iter:
            x, y = x.to(self.device), y.to(self.device)
            y_pred = self.sequential(x)
            y_pred = (f.softmax(y_pred,dim=1))
            c_sum += ((torch.argmax(y_pred,dim=1) == y).sum())
            n_sum += len(x)
        print(c_sum / n_sum)

if __name__ == '__main__':
    sequential = torch.load('./dog_classify_resnet101_e30_validate81.pt')
    sequential.eval()
    transformer = torchvision.transforms.Compose([
        torchvision.transforms.Resize((224, 224)),
        torchvision.transforms.ToTensor(),
    ])
    validate_dataset = torchvision.datasets.ImageFolder(root='D:/DataFiles/Github/dog_detection/stanford-dog/test/crops'
                                                        , transform=transformer
                                                        )

    classes = validate_dataset.classes

    test_iter = torch.utils.data.DataLoader(validate_dataset, 16, False)
    device = torch.device('cuda')
    dog_test = DogTest(sequential=sequential, test_iter=test_iter, device=device, epochs=1)
    dog_test.test()
