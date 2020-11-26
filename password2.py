import random
import string
list = (string.ascii_letters + string.digits + string.punctuation)
pwd = ""
n = 8 + random.randint(0,5)
print(pwd)
while n > 1:
    char = random.choice(list)
    pwd += char
    n=n-1
print("Pasword =: " + pwd)

        

