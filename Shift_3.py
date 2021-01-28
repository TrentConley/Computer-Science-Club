# Shift_3.py
# We will work with wrapping around, uppercase letters, and more edgecases. 

# Get a user sentence:
my_sentence = 


# get shift, and turn it into an integer

my_shift = 


# there is a lot of carryover from Shift_2, but it is more compact. 
for i in range (0, len(my_string)):
	ascii_a = ord('a')
	ascii_z = ord('z')
	greater_than_a = my_sting[i] >= ascii_a
	less_than_z = my_sting[i] <= ascii_z
	# now we have two booleans that hold true or false
	# we can combine these two boolean like in the line below
	between_a_and_z = greater_than_a and less_than_z
	# the line above will return true only if both boolean hold true
	# and false otherwise.  

	if (my_sting[i] >= ord('a') and my_sting[i] <= ord('z')):
		# now we know that all of the letters are inbetween a and z.
		# so that we are only shifting the letters.
		# using what you know from shift_1, print each character
		# shifted over the amount stored in my_shift.
