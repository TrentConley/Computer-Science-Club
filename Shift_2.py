# You might have noticed that if the first letter was a 'z', in shift_1
# then you would get something funky. So, we need to learn how to use if statements.

# Get user input:
# only input lowercase letters for now, we will use capital letters soon

my_string = 


# Get user desired shift:
# hint: you will need to use the int function
my_shift = 


# the int will tun any string into an integer, if it is an integer. 
# you also don't have to declare a new variable every time, you can just replace
# what my_shift stores by setting it equal to something else, in this case is 
# the numerical value in my_shift. 
my_shift = int(my_shift)



for i in range (0, len(my_string)):
	ascii_a = ord('a')
	ascii_z = ord('z')
	# the following lines will declare some booleans
	# booleans are true or false statements, 
	# and you can declare them the same way you do with variables
	greater_than_a = ord(my_string[i]) >= ascii_a
	less_than_z = ord(my_string[i]) <= ascii_z
	# now we have two booleans that hold true or false
	# we can combine these two boolean like in the line below
	between_a_and_z = greater_than_a and less_than_z
	# the line above will return true only if both boolean hold true
	# and false otherwise.  

	if (between_a_and_z):
		# now we know that all of the letters that we will apply the shift to
		# are inbetween a and z.
