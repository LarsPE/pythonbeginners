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