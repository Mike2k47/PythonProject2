import random

numbers = []

for i in range(5):
    number = random.uniform(0, 10)
    numbers.append(number)

print("Random numbers:", numbers)

minimum = min(numbers)
maximum = max(numbers)

print("Minimum value:", minimum)
print("Maximum value:", maximum)