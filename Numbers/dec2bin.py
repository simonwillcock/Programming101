# user can convert a number between decimal and binary


def decimalToBinary(n):
	
	return 0

def binaryToDecimal(n):
	count = 0
	total = 0
	for i in n:
		total += (int(i) * 2**count)
		print(i + " * " + str(2**count))
		count += 1
	return total

valid_input = False

while valid_input == False:

	format = str(raw_input("Convert Decimal or Binary? "))
	format = format.lower()


	if format == "decimal" or format == "dec" or format == "d":
		# Convert decimal to binary
		valid_input = True

	elif format == "binary" or format == "bin" or format == "b":
		# Convert binary to decimal
		valid_input = True
		print(binaryToDecimal(str(raw_input("Binary Number: "))))

	else:
		valid_input = False

# 1 2 4 8 16 32 64
# 0 1 0 1