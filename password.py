import random
pwd = ""

list = [1,2,3,4,5,6,7,8,9,0,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
n = 7 + random.randint(0,5)
while n > 1:
    char = str(random.choice(list))
    if char.isdigit():
        pwd += char
    else:        
        if random.randint (1,10) % 2 == 0:
            char = char.upper()
        pwd += char
   
    n=n-1
print(pwd)

        

