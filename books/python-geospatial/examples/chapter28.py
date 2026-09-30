import numpy as np

names = np.array(["A", "B", "C"])
# Both indicators: larger = preferred; values are synthetic.
indicators = np.array([[0.9,0.2], [0.5,0.8], [0.8,0.8]])
feasible = np.array([True, True, False])
for weights in (np.array([0.7,0.3]), np.array([0.3,0.7])):
    scores = indicators @ weights
    scores[~feasible] = -np.inf
    winner = names[scores.argmax()]
    print("weights:", weights, "scores:", scores, "winner:", winner)
assert names[(indicators @ [0.7,0.3])[:2].argmax()] == "A"
assert names[(indicators @ [0.3,0.7])[:2].argmax()] == "B"
