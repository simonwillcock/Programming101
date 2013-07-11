# Enter a number and the Fibonacci sequence will be generated to that number or the Nth number

previous =  [0,1]

n = raw_input("How many Fibonacci numbers would you like to generate: ")

print(previous[0]),
print(previous[1]),

for i in range(1,int(n) - 1):
	current = sum(previous)
	print current,
	previous[0] = previous[1]
	previous[1] = current
	