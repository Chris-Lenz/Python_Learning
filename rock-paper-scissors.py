import random
choice = "empty"
ranq = "empty"
list = ("rock", "paper", "scissors", "quit")
list2 = ("rock", "paper", "scissors")
while choice != "quit":
    choice = input ("input Rock, Paper or Scissors - enter quit to quit:  ")
    ranq = random.choice(list2)
    if choice == "quit":
        print ("Quit")
    elif choice not in list:
        print (choice + " is not a valid choice.")
    elif choice == ranq:
        print ("you have tied " + choice + " = " + ranq)
    elif choice == "rock" and ranq != "paper":
        print ("WIN " + choice + " beats " + ranq)
    elif choice == "paper" and ranq != "scissors":
        print ("WIN " + choice + " beats " + ranq)
    elif choice == "scissors" and ranq != "rock":
        print ("WIN " + choice + " beats " + ranq)
    else:
        print ("LOSE: " + ranq + " beats " + choice)
       
       
       
       
