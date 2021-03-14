# functions.py

def helloworld():
	print("Hello world!")

helloworld()			# call the function twice
helloworld()

def add(x,y):
	print("The value is: ", x+y)
	return x + y

x = add(12,5)
print("The returned value printed: ", x)


# function with default parameters
def add2(x=0,y=0):
	return x + y

result =add2()		# add2() use default values
print(result)

# vary the number of arguments
def mySum(*numbers):
	res = 0
	for number in numbers:
		res += number 
	return res 

x = mySum(1,4,6,8)
print(x)
x = mySum(1,2,3,4)
print(x)