parks = [
    {"name": "A", "area_m2": 3000, "people": 1000},
    {"name": "B", "area_m2": 2000, "people": 500},
]
for park in parks:
    assert park["people"] > 0
    per_person = park["area_m2"] / park["people"]
    print(park["name"], per_person, "m2/person")
