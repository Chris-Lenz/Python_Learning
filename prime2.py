

def prime(number):
    x = 2
    while x < number and x > 1:
        if number % x == 0:
            return "Not Prime"
        x += 1
    return "Prime"

print (prime(int(input("Enter a number: "))))



        
