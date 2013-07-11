# Calculate the prime factors of the given number

n = int(raw_input("Enter a number to calculate it's prime factors: "))

def isPrime(n):
	# Check if given number is a prime
	is_prime = True
	for i in range(2,n):
 		if n % i == 0:
			is_prime = False
			break
	return is_prime

def getFactors(n,factors = []):
	for i in range(2,n):
		if n % i == 0:
			if isPrime(i) == True:
				factors.append(i)
			else:
				getFactors(i)
	return factors

print getFactors(n)
