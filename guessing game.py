import random
guess = 0
n = 1
randn = random.randint(1,10)
while n >= 1:
    guess = input ("Enter a number between 1 and 10: ")
    if guess == "quit":
        break
    elif int(guess) > 10 or int(guess) < 1:         
        print ("Number must be between 1 and 10, please try again.")
    elif int(guess) > int(randn):
        print ("To high, guess lower")
    elif int(guess) < int(randn):
        print ("To low, guess higher")
    elif int(guess) == int(randn):
        print ("good guess, " + str(guess) + " = " + str(randn) + "."  "It took you " + str(n) + " guesses.")
        randn = random.randint(1,10)
        n = 0
   
    n = n + 1
        
    
    
    
    

