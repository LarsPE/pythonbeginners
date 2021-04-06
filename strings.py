#strings - sequences of characters
#string is a list and list functions can be used

text = "Just a text for testing purposes"
print(len(text))			#print length
print(text[1])				#indexing
print(text[5:])				#slicing
print(text[:9])
print(text[1:4])

for letter in text:
	print(letter)

newText = "hello world\nThis is a new day\nAnd a new line here...."
print(newText)

#string formatting
name = "Lars"
age = 45
print("My name is %s and I am %d year old" % (name, age))
print("My name is {} and I am {} year old".format(name, age))

moreText = "This is some more text today"
print(moreText.upper())
print(moreText.lower())
print(moreText.title())		#first letter uppercase in each word

tekst = "I am Lars and my life is beautiful ! Because of my job"
print(tekst.count('my'))
print(tekst.count(' '))