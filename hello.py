# hello.py
# hello world to screen and print formatting

print("Hello world")

name = "Kim"
print("Hello, %s." %name)	# not recommended to use


age = 33
print("Hello, {}. You are {} years old".format(name, age))


print("You are now {1} years old, {0}".format(name, age))

# f-strings
hisName = "Erik"
hisAge = 24
print(f"Hello {hisName}. Today you are {hisAge} years old.")