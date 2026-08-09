### Count Heads and Tails
import random

heads = 0
tails = 0

for i in range(100):
    toss = random.choice(["H", "T"])

    if toss == "H":
        heads += 1
    else:
        tails += 1

print("Heads =", heads)
print("Tails =", tails)
### Dice Roll Simulation
import random

dice = random.randint(1, 6)

print("Dice:", dice)
### Coin Toss Simulation
import random

coin = random.choice(["Heads", "Tails"])

print("Result:", coin)