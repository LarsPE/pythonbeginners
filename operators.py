# operators.py

# modulus
print(10 % 3)

# exponentiation
print(10**2)

# floor division
print(10//3)


x = 10
y = 20

print(x == y)
print(x < y)
print(x <= y)
print(x != y)


# user input
name = input("your name: ")
print(f"Hello {name}")

age = input("your age: ")
print("{name}, your age is {age}")
print(type(age))

age = int(age)		# typecast to int. input always give string
print(type(age))