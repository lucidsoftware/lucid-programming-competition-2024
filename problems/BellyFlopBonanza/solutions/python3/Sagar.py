n = int(input())
scores = []
for _ in range(n):
    name, coordinates_input, diameter_str = input().split('; ')
    diameter = float(diameter_str)
    x, y = map(float, coordinates_input[1:-1].split(', '))
    score = (x**2 + y**2)**0.5 + (diameter / 2)
    scores.append((name, score))

scores.sort(key = (lambda x: -x[1]))
for i in range(3):
    print(scores[i][0])
