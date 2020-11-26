firstnum = int (input ("Input first number: "))
secondnum = int (input ("input second number: "))
remainder = firstnum % secondnum
print (remainder)
if remainder != 0:
	print ("the number is not evenly divisible")
else:
	print ("the number is evenly divisible")
