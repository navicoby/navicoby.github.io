import torch
from torch import nn

x = torch.arange(1,10,dtype=torch.float32).reshape(1,1,3,3)
layer = nn.Conv2d(1,1,kernel_size=3,bias=False)
with torch.no_grad():
    layer.weight.fill_(1/9)
    y = layer(x)
assert tuple(y.shape) == (1,1,1,1)
assert torch.isclose(y.flatten()[0], torch.tensor(5.0))
print("3x3 mean:", y.item())
