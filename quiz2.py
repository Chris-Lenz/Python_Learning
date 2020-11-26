def lucky_number(name):
  number = len(name) * 9
  lucky = ("Hello " + name + ". Your lucky number is " + str(number))
  return (lucky)
	    
print(lucky_number("Kay"))
#print(lucky_number("Cameron"))
