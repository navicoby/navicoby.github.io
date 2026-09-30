import numpy as np

local_mm = np.array([[0,0], [10000,0]], dtype=float)
theta = np.deg2rad(90)
rotation = np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])
translation_m = np.array([953000,1952000])
world_m = (local_mm / 1000) @ rotation.T + translation_m
assert np.allclose(world_m[0], [953000,1952000])
assert np.allclose(world_m[1], [953000,1952010])
print(world_m)
print("가정한 좌표 변환 예시. 실제 IFC 지리참조를 읽은 결과가 아닙니다.")
