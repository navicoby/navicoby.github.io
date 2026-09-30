import numpy as np

population = np.array([100, 900])
served_population = np.array([100, 450])
zone_ratios = served_population / population
simple_mean = zone_ratios.mean()
overall_ratio = served_population.sum() / population.sum()
assert np.isclose(simple_mean, 0.75)
assert np.isclose(overall_ratio, 0.55)
print("구역 비율 단순 평균:", simple_mean)
print("전체 인구 기준 접근 비율:", overall_ratio)
