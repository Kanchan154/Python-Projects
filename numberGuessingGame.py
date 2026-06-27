import random
num=random.randint(1,100)
print(num)
inputnum=int(input("enter a number:"))
while num!=inputnum:
    print("wrong try again")
    inputnum=int(input("enter a number:"))
print("you have entered a right number")