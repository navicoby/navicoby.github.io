import torch
from torch import nn
import torch.nn.functional as F

torch.manual_seed(7)
class TinyUNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(nn.Conv2d(4,8,3,padding=1), nn.ReLU())
        self.pool = nn.MaxPool2d(2)
        self.bottom = nn.Sequential(nn.Conv2d(8,16,3,padding=1), nn.ReLU())
        self.decoder = nn.Sequential(nn.Conv2d(24,8,3,padding=1), nn.ReLU())
        self.head = nn.Conv2d(8,2,1)

    def forward(self, x):
        skip = self.encoder(x)
        low = self.bottom(self.pool(skip))
        up = F.interpolate(low, size=skip.shape[-2:],
                           mode="bilinear", align_corners=False)
        return self.head(self.decoder(torch.cat([skip, up], dim=1)))

model = TinyUNet()
x = torch.rand(1,4,16,16)
target = torch.randint(0,2,(1,16,16))
logits = model(x)
loss = nn.CrossEntropyLoss()(logits, target)
loss.backward()
assert tuple(logits.shape) == (1,2,16,16)
assert model.head.weight.grad is not None
print("shape:", tuple(logits.shape), "finite loss:", bool(torch.isfinite(loss)))
print("합성 무작위 입력이며, 학습된 분할 모델이 아닙니다.")
