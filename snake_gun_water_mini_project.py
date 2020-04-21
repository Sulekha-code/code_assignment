n=int(input("no of chance:"))
computer_point = 0
draw_point = 0
user_point = 0
import random
y=("snake","gun","water")
i=0
while(i<10):
    z=random.choice(y)
    x=input("enter snake or water or gun:")
    if x=="snake":
        if z=="water":
            print("user won game")
            user_point=user_point+1
        elif z=="gun":
            print("computer won game")
            computer_point=computer_point+1
        elif z=="snake":
            print("game drawn")
            draw_point=draw_point+1
    elif x=="water":
        if z=="snake":
            print("computer won game")
            computer_point=computer_point+1
        elif z=="gun":
            print("user won game")
            user_point=user_point+1
        elif z=="water":
            print("game drawn")
            draw_point=draw_point+1
    elif x=="gun":
        if z=="snake":
            print("user won game")
            user_point=user_point+1
        elif z=="gun":
            print("game drawn")
            draw_point=draw_point+1
        elif z=="water":
            print("computer won")
            computer_point=computer_point+1
    i= i+1
print("User won",user_point,"attempts")
print("Computer won",computer_point,"attempts")
print("tie",draw_point,"attempts")
if(user_point>=computer_point):
    print("User is winner")

