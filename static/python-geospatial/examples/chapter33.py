import numpy as np

train_regions = {"city_A", "city_B"}
test_regions = {"city_C"}
assert train_regions.isdisjoint(test_regions)
truth = np.array([1,1,0,0,255])
pred = np.array([1,0,1,0,1])
valid = truth != 255
tp = int(((truth == 1) & (pred == 1) & valid).sum())
fp = int(((truth != 1) & (pred == 1) & valid).sum())
fn = int(((truth == 1) & (pred != 1) & valid).sum())
union = tp + fp + fn
iou = tp / union if union else float("nan")
assert (tp,fp,fn) == (1,1,1)
assert np.isclose(iou, 1/3)
print("green IoU:", iou, "valid pixels:", int(valid.sum()))
