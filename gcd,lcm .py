###Find the LCM of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Find GCD
small = min(a, b)

for i in range(small, 0, -1):
    if a % i == 0 and b % i == 0:
        gcd = i
        break

# Find LCM
lcm = (a * b) // gcd

print("GCD =", gcd)
print("LCM =", lcm)
---------------------------------------------------
###Find the GCD of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Store original values
x = a
y = b

# Find GCD
while b != 0:
    a, b = b, a % b

gcd = a

# Find LCM
lcm = (x * y) // gcd

print("GCD =", gcd)
print("LCM =", lcm)
---------------------------------------------------------
###Generate Multiplication Table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")