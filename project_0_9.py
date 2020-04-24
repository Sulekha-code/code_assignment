print("printing 1")
#Printing A
for row in range(5):
    for col in range(5):
        if col==2:
            print("*",end=" ")
        elif row==0 and col==1:
             print("*",end=" ")
        elif row==1 and col==0:
             print("*",end=" ")
        elif row==4:
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("printing 2")
#Printing 2
for row in range(5):
    for col in range(5):
        if  col==2: 
            print("*",end=" ")
        elif row==0 and col in(0,1):
             print("*",end=" ")
        elif row==4:
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("printing 3")
for row in range(5):
    for col in range(3):
        if  col==2: 
            print("*",end=" ")
        elif row==0 and col in(0,1):
             print("*",end=" ")
        elif row==2 and col in(0,1):
             print("*",end=" ")
        elif row==4 and col in(0,1):
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("printing 4")
for row in range(5):
    for col in range(3):
        if  col==2: 
            print("*",end=" ")
        elif row in(0,1,2) and col==0:
             print("*",end=" ")
        elif row==2 and col in(0,1):
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("printing 5")
for row in range(5):
    for col in range(3):
        if row in(0,2,4)and col in(0,1,2): 
            print("*",end=" ")
        elif row==1 and col==0:
             print("*",end=" ")
        elif row==3 and col==2:
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  

print("printing 6")
for row in range(5):
    for col in range(3):
        if col==0: 
            print("*",end=" ")
        elif row in(0,2,4) and col in(0,1,2):
             print("*",end=" ")
        elif row==3 and col==2:
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 
print("printing 7")
for row in range(5):
    for col in range(3):
        if col==2: 
            print("*",end=" ")
        elif row==0 and col in(0,1,2):
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("printing 8")
for row in range(5):
    for col in range(3):
        if col==0 or col==2: 
            print("*",end=" ")
        elif row in(0,2,4) and col==1:
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("printing 9")
for row in range(5):
    for col in range(3):
        if col==2: 
            print("*",end=" ")
        elif row==1 and col==0:
            print("*",end=" ")
        elif row in(0,2,4) and col in(0,1):
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 

