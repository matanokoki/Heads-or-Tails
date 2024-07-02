import random

name = input("Who are you? \n> ")
print(f"Hello, {name}!")

print("Tossing a coin...")
results = []
for i in range(3):
    result = "Heads" if random.choice([True, False]) else "Tails"
    results.append(result)
    print(f"Round {i+1}: {result}")

heads_count = results.count("Heads")
tails_count = results.count("Tails")
print(f"Heads: {heads_count}, Tails: {tails_count}")

if heads_count > tails_count:
    print("You won!")
else:
    print("You lost!")
