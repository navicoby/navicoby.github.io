import numpy as np
import torch
from torch import nn
from skimage.measure import label, regionprops

logits = torch.tensor([[[[3.,1.],[1.,2.]],
                        [[1.,3.],[4.,1.]]]], requires_grad=True)
target = torch.tensor([[[0,1],[1,255]]], dtype=torch.long)
loss = nn.CrossEntropyLoss(ignore_index=255)(logits, target)
loss.backward()
prediction = logits.detach().argmax(dim=1)[0].numpy()
components = label(prediction == 1, connectivity=1)
areas = [int(region.area) for region in regionprops(components)]
assert np.array_equal(prediction, [[0,1],[1,0]])
assert areas == [1,1]
assert torch.isfinite(loss)
print("loss:", float(loss.detach()), "connected green pixel counts:", areas)
