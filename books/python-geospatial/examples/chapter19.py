park_area_m2 = 3000
for resolution_m in (10, 20, 60):
    nominal_cells = park_area_m2 / resolution_m**2
    print(f"{resolution_m} m: 면적 비율상 {nominal_cells:.2f} cells")
assert park_area_m2 / 10**2 == 30
print("실제 영상이나 관측값을 사용한 결과가 아닙니다.")
