number = input ("Input a number: ")
number = int(number)
list = range (1,number)
for element in list:
    if number % element == 0:
            print (element)
