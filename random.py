import random

# Define the characters to choose from
characters = "abcdefghijklmnopqrstuvwxyz0123456789"

# Generate 1000 random 6-digit alphanumeric strings and store them in a list
random_strings = [''.join(random.choice(characters) for _ in range(6)) for _ in range(100000)]

# Create a text file and write the random strings to it, one per line
with open("random_strings.txt", "w") as file:
    for string in random_strings:
        file.write(string + "\n")
