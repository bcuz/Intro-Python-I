# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
	if num % 2 == 0:
		return 'Even'
	else:
		return 'Odd'

# Read a number from the keyboard
num = input("Enter a number: ")
# what if someone enters a word :)
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

print(is_even(num));