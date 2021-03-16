# exceptions.py

try:
	x = int(input("First number: "))
	y = int(input("Second number: "))
	print(x / y)
except:
	print("There was an error in the calculation")

# in above code we will get error if divided by 0
# or text is written. Then the except will be executed.

try:
	x = int(input("First number: "))
	y = int(input("Second number: "))
	print(x / y)
except ValueError:
	print("Please enter a valid number next time")
except ZeroDivisionError:
	print("Cannot divide by zero")
finally:
	print("DONE !")


#####################################

def some_function():
	if True:
		raise Exception ("Something went terribly wrong")


some_function()