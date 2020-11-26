number = input("input a number: ")
number = int (number)
remainder = number % 2
remainder2 = number % 4
print (remainder)
if remainder2 == 0:
	print ("The number is divisible by 4")
elif remainder == 0:
	print ("The number is even")
else:
	print ("the number is odd")
