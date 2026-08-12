# Python Loop Snippets

# 1. For loop
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)


# 2. Loop with range()
for i in range(1, 6):
    print("Number:", i)


# 3. While loop
count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# 4. List comprehension
squares = [x * x for x in range(1, 6)]
print("Squares:", squares)
