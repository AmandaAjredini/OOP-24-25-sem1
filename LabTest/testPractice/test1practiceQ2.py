

my_str = "Monty Python"
encrypted = ""
count = 0

for char in my_str:
    encrypted += chr(ord(char) + count)
    count += 1

print(encrypted)