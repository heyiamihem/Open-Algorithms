import math

def noOfDivisors(n):
	count = 0
	for i in range(1,math.ceil(math.sqrt(n))):
		if(n%i==0):
			count = count+1
	count=count*2
	if(n%math.ceil(math.sqrt(n))==0 and math.sqrt(n)%1 == 0):
		count = count+1
	return count

x = int(input("Give the value : "))
print(f"Number of Divisors of {x} is : {noOfDivisors(x)}")