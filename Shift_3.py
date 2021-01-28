# Shift_3.py
# We will work with wrapping around, uppercase letters, and more edgecases. 

# Get a user sentence:
my_sentence = 


# get shift, and turn it into an integer you can also enter a really big number
# the computer should be able to do all calculations almost instantly. 

my_shift = 

if (my_shift >= 26):
	my_shift = my_shift%26

# the percent sign, or modulo, will take the remainder of a number
# this way, we know that my_shift is less than 26


# there is a lot of carryover from Shift_2, but it is more compact. 
new_sentence = ''
# instead of printing while going, I am adding creating a new sentence as I go
for i in range (0, len(my_string)):
	if (ord(my_sentence[i]) >= ord('a') and ord(my_sentence[i]) <= ord('z')):
		# now we know that all of the letters that we will apply the shift to
		# are inbetween a and z.
		# the next if statement will allow for 
		if (ord(my_stentence[i]) + my_shift > ord('z')):
			new_shift = 

# Now, try and do the same thing but with uppercase letters. 
# Enter code below:
# Note: it should look very similar to the loop above. 

		