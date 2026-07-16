actual = [10, 20, 30]
predicted = [12, 18, 29]

cost = 0
for a, p in zip(actual, predicted):
    cost += (a - p) ** 2

cost = cost / len(actual)
print("Mean Squared Error:", cost)