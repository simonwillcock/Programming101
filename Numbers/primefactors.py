# Calculate the prime factors of the given number


def isPrime(n):
	# Check if given number is a prime
	is_prime = True
	for i in range(2,n):
 		if n % i == 0:
			is_prime = False
			break
	return is_prime

def getPrimeFactors(n,factors = []):
	for i in range(2,n):
		if isPrime(i) == True:
			if n % i == 0:
				factors.append(i)
				if isPrime(n/i) != True:
					getPrimeFactors(n/i)
					break
	return factors

if __name__ == "__main__":
	n = int(raw_input("Enter a number to calculate it's prime factors: "))
	if isPrime(n) == True:
		print(n)
	else:
		print(getPrimeFactors(n))
