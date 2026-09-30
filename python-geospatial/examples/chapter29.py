import numpy as np
import torch

bands = np.array([[[0.1,0.2],[0.3,0.4]],
                  [[0.5,0.6],[0.7,0.8]]], dtype="float32")
x = torch.from_numpy(bands.copy()).unsqueeze(0)
training_mean = torch.tensor([0.25,0.65]).view(1,2,1,1)
training_std = torch.tensor([0.1,0.1]).view(1,2,1,1)
normalized = (x - training_mean) / training_std
assert tuple(x.shape) == (1,2,2,2)
assert torch.isfinite(normalized).all()
print("N,C,H,W:", tuple(x.shape))
print(normalized)
