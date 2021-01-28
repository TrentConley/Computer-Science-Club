# Shift_3.py
# We will work with wrapping around, uppercase letters, and more edgecases. 

# Get a user sentence:
my_sentence = 


# get shift, and turn it into an integer

my_shift = 


# there is a lot of carryover from Shift_2, but it is more compact. 
for i in range (0, len(my_string)):
	if (ord(my_sting[i]) >= ord('a') and ord(my_sting[i]) <= ord('z')):
		# now we know that all of the letters are inbetween a and z.
		# so that we are only shifting the letters.
		# using what you know from shift_1, print each character
		# shifted over the amount stored in my_shift.
