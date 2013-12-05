#!usr/bin.env python

# Ex. 1: Can you implement the following grading scheme in Python? ou print the middle letter of the fourth sentence?

score = 46
grade = 'X'
if score >= 90:
	grade = 'A'
elif score >= 80:
	grade = 'B'
elif score >= 70:
	grade = 'C'
elif score >= 60:
	grade = 'D'
else:
	grade = 'F'
print('You score was '+str(score)+', so you the grade: '+grade+'.')


print("======================================")

# Ex. 2: Can you spot the reasoning error in the following code?

# Solution: If one of the if-statements in an if-elif-else contruction evaluates to True,
# the rest of the construction will not be executed anymore. In case the score=60,
# if will assign the lowest grade and abort the construction without even checking 
# whether one of the higher grades might be assigned.

print("======================================")

# Ex. 3:  In 1939 Ernest Vincent Wright published a 50,000 word novel called
# Gadsby that does not contain the letter 'e'. Since 'e' is the most
# common letter in English, that's not easy to do.
# Define a variable sentence and write some Python code that will
# print to screen whether sentence contains an 'e'. If it contains at
# least 3 instances of 'e', make it print only the words that have
# no 'e' and compute the percentage of the words in the sentence
# that do contain an 'e'.


sentence = "In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter 'e'"
if "e" in sentence:
	print("There is at least one letter e in the sentence.")
	nr_e = sentence.count("e")
	if nr_e > 3:
		print("There are at least three letters e in the sentence.")
		words = sentence.split()
		no_es = 0
		for word in words:
			if "e" not in word:
				no_es+=1
				print("* "+word)
		percentage = (float(no_es)/len(words))
		print "Percentage of words without an e: "+str(percentage)+"%"

print("======================================")

# Ex. 4: Write Python code that defines a list and selects the unique
# elements from the original and puts these in a new variable.
# Print the unique elements. (Hint: they don't have to be in the same order.)



uniques = set(orig_list)
print("Unique elements: "+str(uniques))

print("======================================")

# Ex. 5: Write Python code that defines two numbers and prints the largest of
# them. Use an if-then-else tree.


nr1 = 3
nr2 = 4

if nr1 > nr2:
	print(str(nr1))
elif nr1 == nr2:
	print("There equal!")
else:
	print(str(nr2))

print("======================================")

# Ex. 6: ROT13 is a weak form of encryption that involves "rotating"
# each letter in a word by 13 places. To rotate a letter means to
# shift it through the alphabet, wrapping around to the beginning
# if necessary, so a shifted by 3 is d and a shifted by 1 is z.
# Define a string called rotate_word and an integer variable called
# amount. Now write a Python script that contains the letters
# from the rotate_word, but "rotated" by the given amount. Check
# your code using the following examples: 'cheer' rotated by 7 is
# 'jolly' and 'melon' rotated by -10 is 'cubed'. Use a list of
# alphabetical characters (['a', 'b', ..., 'z'). Hint: you retrieve
# the index of an item in a list using the index()function.

rotate_word = "cheer"
amount = 7
lookup = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encoded_word = ""
for char in rotate_word:
	print("* Orig letter was: "+char)
	orig_index = lookup.index(char)
	print("* Orig index was: "+str(orig_index))
	new_index = orig_index+amount
	if new_index >= len(lookup):
		new_index-=len(lookup)
	print("* New index is: "+str(orig_index))
	new_char = lookup[new_index]
	print("* New char is: "+str(new_char))
	encoded_word+=new_char
print("The encoded word: "+encoded_word)

print("======================================")