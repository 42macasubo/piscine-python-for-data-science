import sys

if len(sys.argv) == 1:
	print()
	exit()
try:
	assert len(sys.argv) == 2, "more than one argument is provided"
	assert sys.argv[1].isdigit(), "argument is not an integer"
	print("I'm Even." if int(sys.argv[1]) % 2 == 0 else "I'm Odd.")
except AssertionError as error:
	print(error)
