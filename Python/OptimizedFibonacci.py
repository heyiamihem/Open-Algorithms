# Fibonacci numbers till n using direct formula. 
import math 
# Function to calculate fibonacci numbers
def fibonacci(n): 
	for i in range(n): 
		# Direct formula calculation
		fib = ((pow((1 + math.sqrt(5)), i) -
				pow((1 - math.sqrt(5)), i)) /
			(pow(2, i) * math.sqrt(5))); 
				
		print(int(fib), end = " "); 

# Input from user
n = int(input("Enter a position:"))
fibonacci(n)
