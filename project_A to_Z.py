print("printing A")
#Printing A
for row in range(7):
    for col in range(5):
        if((col==0 or col==4)and row!=0)or((row==0 or row==3)
                                           and(col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("printing B")
#printing B
for row in range(7):
    for col in range(5):
            if((col==0 or col==4)or((row==0 or row==3 or row==6))):
               print("*",end="")
            else:
                print(end=" ")
    print()
print("printing C")
#printing C
for row in range(7):
    for col in range(5):
            if((col==0)or((row==0 or row==6)and(col>0))):
               print("*",end="")
            else:
                print(end=" ")
    print()

print("printing D")
#printing D
for row in range(7):
    for col in range(5):
            if((col==0)or(col==4 and(row!=0 and row!=6))or((row==0 or row==6)and(col>0 and col<4))):
               print("*",end="")
            else:
                print(end=" ")
    print()

print("printing E")
#printing E
for row in range(7):
    for col in range(5):
            if((col==0)or((row == 0 or row ==3 or row ==6))and col>0):
               print("*",end="")
            else:
                print(end=" ")
    print()

#printing F
print("printing F")
for row in range(7):
    for col in range(5):
            if((col==0)or((row == 0 or row ==3))and col>0):
               print("*",end="")
            else:
                print(end=" ")
    print()
    
print("printing G")
#printing G
print("printing G")
for row in range(7):
    for col in range(5):
            if col==0 or (col==4 and (row!=1 and row!=2))or((row==0 or row==6)and(col>0 and col<4))or(row ==3 and col==3):
               print("*",end="")
            else:
                print(end=" ")
    print()
    

#printing H
    
print("printing H")
for row in range(7):
    for col in range(5):
            if((col==0)or(col==4) or((row ==3)and col>0 and col<4)):
               print("*",end="")
            else:
                print(end=" ")
    print()

#printing I
for row in range(7):
    for col in range(5):
            if col==2 or((row ==0 or row==6)and col!=2):
               print("*",end="")
            else:
                print(end=" ")
    print()
    
#printing J
for row in range(7):
    for col in range(5):
        if col==2 or((row ==0 or row==6)and (col!=3 and col!=4)):
               print("*",end="")
        else:
            print(end=" ")
    print()

#printing k
for row in range(7):
    for col in range(5):
        if(row in(0,6))and(col in(0,4)):
            print("*",end=" ")
        elif(row in(1,5))and(col in(0,3)):
             print("*",end=" ")
        elif(row in (2,4))and(col in(0,2)):
             print("*",end=" ")
        elif(row==3)and(col in(0,1)):
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#printing L            
for row in range(7):
    for col in range(5):
         if(col==0):
             print("*",end=" ")
         elif(row==6) and (col in(1,2,3,4)):
             print("*",end=" ")
         else:
             print(" ",end=" ")
    print()
#printing M
for row in range(7):
    for col in range(5):
         if(col in(0,4)):
             print("*",end=" ")
         elif(row==1) and (col in(1,3)):
             print("*",end=" ")
         elif(row==2)and (col==2):
             print("*",end=" ")
         else:
             print(" ",end=" ")
    print()
#printing N
for row in range(7):
    for col in range(5):
         if(col in(0,4)):
             print("*",end=" ")
         elif(row==1) and (col in(1,3)):
             print("*",end=" ")
         elif(row==2)and (col==2):
             print("*",end=" ")
         else:
             print(" ",end=" ")
    print()
#printing N
for row in range(5):
    for col in range(5):
         if(col in(0,4)):
             print("*",end=" ")
         elif(row==1)and(col==1):
             print("*",end=" ")
         elif(row==2)and (col==2):
             print("*",end=" ")
         elif(row==3)and (col==3):
             print("*",end=" ")
         elif(row==4)and (col==4):
             print("*",end=" ")
         else:
             print(" ",end=" ")
    print()
#printing 0
for row in range(7):
    for col in range(5):
         if(col in(0,4)):
             print("*",end=" ")
         elif(row in(0,6)):
             print("*",end=" ")
         else:
             print(" ",end=" ")
    print()
#printing P
for row in range(7):
    for col in range(5):
         if col==0:
             print("*",end=" ")
         elif row in(0,3)and col!=4:
             print("*",end=" ")
         elif row in(0,1,2)and col==3:
             print("*",end=" ")
         else:
             print(" ",end=" ")
    print()
#printing Q

'''#Example just for understanding
for row in range(8):
    for col in range(5):
        if(row==0):
            print(col,end=" ")
        else:
            print("*",end=" ")
    if(row!=0):
        print(row-1,end=" ")
    print()'''
        

#printing Q
for row in range(7):
    for col in range(5):
         if row in(0,6):
             print("*",end=" ")
         elif (col in(0,4)and (row != 0 or row !=6)):
             print("*",end=" ")
         elif ((row==5 and col ==3)or (row==4 and col ==2)):
             print("*",end=" ")
         else:
             print(" ",end=" ")
        
    print()
#printing R
for row in range(6):
    for col in range(5):
         if row == 0 or col==0:
             print("*",end=" ")
         elif row==1 and col==4:
             print("*",end=" ")
         elif row==2 and col in(1,2,3,4):
             print("*",end=" ")
         elif row==3 and col==2:
             print("*",end=" ")
         elif row==4 and col==3:
             print("*",end=" ")
         elif row==5 and col==4:
             print("*",end=" ")
         else:
             print(" ",end=" ")
        
    print()
#printing S
for row in range(5):
    for col in range(4):
         if row in (0,2,4) and col in(0,1,2,3):
             print("*",end=" ")
         elif row==1 and col==0:
             print("*",end=" ")
         elif row==3 and col==3:
             print("*",end=" ")
         else:
             print(" ",end=" ")
        
    print()
#printing T
for row in range(6):
    for col in range(5):
         if row == 0 or col==2:
             print("*",end=" ")
         else:
             print(" ",end=" ")
        
    print()
#printing U
for row in range(5):
    for col in range(5):
         if row ==4 or col in(0,4):
             print("*",end=" ")
         else:
             print(" ",end=" ")
    print()
#printing V
for row in range(4):
    for col in range(7):
         if row ==0 and col in(0,6):
             print("*",end=" ")
         elif row==1 and col in(1,5):
             print("*",end=" ")
         elif row==2 and col in(2,4):
             print("*",end=" ")
         elif row==3 and col==3:
             print("*",end=" ")
         else:
             print(" ",end=" ")
    print()
#printing W
for row in range(5):
    for col in range(5):
        if row in(0,1,2,3,4)and col in(0,4):
             print("*",end=" ")
        elif row==2 and col==2:
             print("*",end=" ")
        elif row==3 and col in(1,3):
             print("*",end=" ")
        else:
             print(" ",end=" ")
    print()
#printing X
for row in range(5):
    for col in range(5):
        if row in(0,4)and col in(0,4):
             print("*",end=" ")
        elif row ==1 and col in(1,3):
             print("*",end=" ")
        elif row==2 and col==2:
             print("*",end=" ")
        elif row==3 and col in(1,3):
             print("*",end=" ")
        else:
             print(" ",end=" ")
    print()

#printing Y
for row in range(5):
    for col in range(5):
        if row==0and col in(0,4):
             print("*",end=" ")
        elif row ==1 and col in(1,3):
             print("*",end=" ")
        elif row==2 and col==2:
             print("*",end=" ")
        elif row==3 and col==2:
             print("*",end=" ")
        elif row==4 and col==2:
             print("*",end=" ")
        else:
             print(" ",end=" ")
    print()

##printing Z
for row in range(5):
    for col in range(5):
        if row in (0,4)and col in(1,2,3):
             print("*",end=" ")
        elif row ==1 and col==3:
             print("*",end=" ")
        elif row==2 and col==2:
             print("*",end=" ")
        elif row==3 and col==1:
             print("*",end=" ")
        else:
             print(" ",end=" ")
    print()
