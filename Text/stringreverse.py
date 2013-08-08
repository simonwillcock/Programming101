""" This program will print the given string in reverse """

def reverse(string):
	reversedString = ""
	for c in string[::-1]:
		reversedString += c
	return reversedString

user_string = str(input("Enter the string you would like reversed: "))
print(reverse(user_string))