#Can you Guess The Number
#NOTE: You have only three chances to guess it right


from random import *

y=randint(0,50)
a=3
print("Enter a number between 1 to 50")
while(1):
    x=int(input())
    if(x>50):
        print("You entered number not in range")
        break
    if(x==y):
        print("You guess it right. The number is "+str(y))
        break
    else:
        a=a-1
        if(a==0):
            print("Oops!! You lose")
            break
        print("Wrong !! You have now "+str(a)+" chances left")
        
print("The Number is: "+str(y))

#completed
