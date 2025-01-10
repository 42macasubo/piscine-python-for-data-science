import sys

if len(sys.argv) == 1:
	exit()

try:
	assert len(sys.argv) == 2, "more than one argument is provided"
	print("I'm Even." if int(sys.argv[1]) % 2 == 0 else "I'm Odd.")
except AssertionError as error:
	print(error)
except ValueError:
	print("AssertionError: argument is not an integer")
