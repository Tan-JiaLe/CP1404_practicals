NAME_FILE = 'name.txt'
NUMBER_FILE = 'numbers.txt'

# 1.
out_file = open(NAME_FILE, 'w')
name = input("Your name: ")
while name != '':
    out_file.write(f"{name}\n")
    name = input("Your name: ")
out_file.close()

# 2.
in_file = open(NAME_FILE, 'r')
for name in in_file.readlines():
    name = name.strip()
    print(f"Your name is {name}.")
in_file.close()

# 3.
in_file = open(NUMBER_FILE, 'r')
first_two_numbers = in_file.readlines()[:2]
result = int(first_two_numbers[0]) + int(first_two_numbers[1])
print(result)
in_file.close()

# 4.
total = 0
in_file = open(NUMBER_FILE, 'r')
for line in in_file.readlines():
    number = int(line)
    total += number
print(total)
in_file.close()