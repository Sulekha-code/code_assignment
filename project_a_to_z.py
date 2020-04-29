def print_a():
    print("printing a")
    for row in range(5):
        for col in range(4):
            if row in (0,2,4)and col in (0,1,2):
                print("*",end=" ")
            elif col==3:
                print("*",end=" ")
            elif row==3 and col==0:
                 print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
print_a()

def print_b():
    print("printing b")
    for row in range(5):
        for col in range(4):
            if col==0:
                print("*",end=" ")
            elif row in(2,4) and col in(0,1,2,3):
                print("*",end=" ")
            elif row==3 and col==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
print_b()



def print_c():
    print("printing c")
    for row in range(4):
        for col in range(3):
            if row in(0,2) and col==2:
                print("*",end=" ")
            elif row in(0,2) and col==0:
                print("*",end=" ")
            elif row in(0,2) and col==1:
                print("*",end=" ")
            elif row==1 and col==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
print_c()




def print_d():
    print("printing d")
    for row in range(5):
        for col in range(4):
            if col==3:
                print("*",end=" ")
            elif row in(2,4) and col in(0,1,2):
                print("*",end=" ")
            elif row==3 and col==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
print_d()


def print_e():
    print("printing e")
    for row in range(5):
        for col in range(4):
            if row==0 and col in(0,1,2):
                print("*",end=" ")
            elif row==1 and col in(0,1,2):
                print("*",end=" ")
            elif row==2 and col==0:
                print("*",end=" ")
            elif row==3 and col in(0,1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
print_e()


def print_f():
    print("printing f")
    for row in range(5):
        for col in range(3):
            if col==1:
                print("*",end=" ")
            if row==0 and col in(1,2,3):
                print("*",end=" ")
            elif row==2 and col in(0,1):
                print("*",end=" ")
            elif row==1 and col==2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
print_f()

def print_g():
    print("printing g")
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
print_g()

def print_h():
    print("printing h")
    for row in range(5):
        for col in range(4):
            if col==0:
                print("*",end=" ")
            elif row==2 and col in(1,2,3):
                print("*",end=" ")
            elif row in(2,3,4) and col==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print() 
print_h()


def print_i():
    print("printing i")
    for row in range(5):
        for col in range(4):
            if row in(2,3,4) and col==2:
                print("*",end=" ")
            elif row==0 and col==2:
                print("*",end=" ") 
            elif row==4 and col in(1,2,3,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print() 
print_i()

def print_j():
    print("printing j")
    for row in range(5):
        for col in range(4):
            if row in(2,3,4) and col==2:
                print("*",end=" ")
            elif row==0 and col==2:
                print("*",end=" ") 
            elif row in(3,4) and col==0:
                print("*",end=" ")
            elif row==4 and col==1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print() 
print_j()


def print_k():
    print("printing k")
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

print_k()

def print_l():
    print("printing k")
    for row in range(5):
        for col in range(4):
            if col==2:
                print("*",end=" ")
        
        print()
print_l()

def print_m():
    print("printing m")
    for row in range(4):
        for col in range(4):
            if row in(1,2,3)and col in(1,2,3):
                print("*",end=" ")
            elif row==1 and col==0 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            
        print()
print_m()


def print_n():
    print("printing n")
    for row in range(4):
        for col in range(4):
            if row in(1,2,3)and col in(1,2):
                print("*",end=" ")
            elif row==1 and col==0 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            

        print()

print_n()
  
def print_o():
    print("printing o")
    for row in range(4):
        for col in range(4):
            if(row in (1,2,3) and col in(0,2)):
                print("*",end=" ")
            elif col ==1 and row in (1,3) :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

print_o()



def print_p():
    print("printing p")
    for row in range(4):
        for col in range(4):
            if(col ==0 or (row in(1,0) and col in (1,2))):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

print_p()



def print_q():
    print("printing q")
    for row in range(4):
        for col in range(4):
            if(col ==3 or (row in(1,0) and col in (1,2))):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

print_q()


def print_r():
    print("printing r")
    for row in range(4):
        for col in range(4):
            if(col ==0 or (row ==1 and col ==1)or (row ==0 and col ==2)):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

print_r()

def print_s():
    print("printing s")
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

print_s()



def print_t():
    print("printing t")
    for row in range(4):
        for col in range(4):
            if(col ==1 or (row ==3 and col in(1,2))or (row ==1 and col in(0,2))):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

print_t()


def print_u():
    print("printing u")
    for row in range(4):
        for col in range(4):
            if((col ==0 or col == 2) and row in range(1,4)):
                print("*",end=" ")
            elif(row == 3 and col in (1,3)):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

print_u()

#printing v
def print_v():
    print("printing v")
    for row in range(5):
        for col in range(5):
             if row ==1 and col in(0,4):
                 print("*",end=" ")
             elif row==2 and col in(1,3):
                 print("*",end=" ")
             elif row==3 and col == 2:
                 print("*",end=" ")
             else:
                 print(" ",end=" ")
        print()
print_v()

#printing w
def print_w():
    print("printing w")
    for row in range(4):
        for col in range(4):
            if row in(0,1,2,3)and col in(0,2):
                 print("*",end=" ")
            elif row==2 and col==1:
                 print("*",end=" ")
            else:
                 print(" ",end=" ")
        print()

print_w()

#printing x
def print_x():
   print("printing x")
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
	   
print_x()



#printing y
def print_y():
    print("printing y")
    for row in range(4):
        for col in range(4):
            if row == 0 and col in(0,3):
                 print("*",end=" ")
            elif row==1 and col in (1,2):
                 print("*",end=" ")
            elif (row==2 and col == 1) or (row==3 and col == 0):
                 print("*",end=" ")
            else:
                 print(" ",end=" ")
        print()

print_y()

#printing w
def print_z():
    print("printing z")
    for row in range(4):
        for col in range(4):
            if row in (1,3) and col in range(0,3):
                 print("*",end=" ")
            elif row==2 and col==1:
                 print("*",end=" ")
            else:
                 print(" ",end=" ")
        print()

print_z()

