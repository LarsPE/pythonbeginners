# exceptions.py

try:
	x = int(input("First number: "))
	y = int(input("Second number: "))
	print(x / y)
except:
	print("There was an error in the calculation")