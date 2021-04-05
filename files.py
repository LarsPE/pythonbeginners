#modes to handle file
#w - write
#r - read
#a - append
#file = open('myfile.txt', )
#file.close()

with open('file.txt', 'r') as f:
	#all of my code
	content = f.read()

print(content)