# Find next prime number until user requests stop
from primefactors import isPrime

cont = True
currPrime = 2

def getNextPrime(n):
	gotPrime = False
	while gotPrime == False:
		gotPrime = isPrime(n)
		if gotPrime == False:
			n += 1
		else:
			return n

while cont == True:
	print(getNextPrime(currPrime))
	
	currPrime += 1

	user_cont = raw_input("Find next Prime number (y/n): ")
	if(user_cont.lower() == "n" or user_cont.lower() == "no"):
		cont = False
