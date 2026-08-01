### Find the Second Largest Number
numbers = [10, 45, 20, 80, 60]

numbers.sort()

print("Second Largest:", numbers[-2])
### Count Frequency of Characters
text = input("Enter a string: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
###Pattern Printing
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
###Find Missing Number
numbers = [1, 2, 3, 5]

n = 5

expected = n * (n + 1) // 2
actual = sum(numbers)

print("Missing Number:", expected - actual)
###Find Common Elements in Two Lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = []

for i in list1:
    if i in list2:
        common.append(i)

print(common)
###Count Words in a Sentence
sentence = input("Enter a sentence: ")

words = sentence.split()

print("Number of words:", len(words))