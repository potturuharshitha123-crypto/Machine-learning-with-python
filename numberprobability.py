###Guess the Number
import random

number = random.randint(1, 10)

guess = int(input("Guess a number (1-10): "))

if guess == number:
    print("Correct!")
else:
    print("Wrong")
    print("Number was", number)
###Draw a Card
import random

cards = ["A", "2", "3", "4", "5",
         "6", "7", "8", "9",
         "10", "J", "Q", "K"]

print(random.choice(cards))
###Probability of Drawing an Ace
total_cards = 52
aces = 4

probability = aces / total_cards

print(probability)