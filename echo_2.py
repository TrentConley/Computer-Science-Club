# Using what you learned from echo_1, get a user input for 
# a long sentence prompting them accordingly. 
# Enter code below: 
my_string = 


# This is how to get the character of location i of a string
# The location of a string will always start at 0. 
i = 0
my_character = ''

length = len(my_string)
# you can find the length of a character by tying len() with your variable inside
# the parentheses

# single quotation marks represent a character. we have set it to nothing for now. 

# you can access any character of a string by typing brackets after the string, with 
# a number (or variable that holds a number) inside to indicate the position. 
# the line below will print the first character of the string because 

print(my_string[0]) 

# now onto for loops

for i in range (0,length):
	my_character = my_string[i]
	print (my_character)

# above is how to make a for loop. 
# "i" is a temporary variable (meaning that it gets discarded after the for loop) 
# and is used to store the integer value of the current position 
# in the range of the for loop. You could use any other variable name in place of 
# "i" such as "count" or "x" or "number".
# You usually want to start off with for i in range (0, num):
# num1 stands for the amount of iterations that will take place (because num - 0 = num)
# if you said range (1, num), then there would be num - 1 iterations that take palce
# Also make sure to indent everything inside of the for loop by pressing tab. 


num1 = (8/2) - (3*3)
# this should equal -5 if I can do algebra 1 correctly. 
print (num1)
# the line above is to show you how simple math works in python. A general rule of thumb 
# is to use lots of parentheses. 

# All of the numbers above are integers, so when you do division, for example 5/2, you
# should get 2 because it rounds down. If you want to get the exact amount, then you should 
# use what are called doubles. You can make a double by just typing .0 at the end of the 
# integer. 
num2 = 5.0/2.0
print (num2)
# this should yeild 2.5

# Using what you know about math and for loops, try to make a for loop that will print
# half of the characters in a string below.  








