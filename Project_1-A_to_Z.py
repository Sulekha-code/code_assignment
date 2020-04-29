print("Welcome to pattern Printing:\n\n")
height = 0
width =0
# Function to print the pattern of 'A' 
def printA() :
    n = int(width / 2)
    for i in range(height) : 
        for j in range(width+1):
            if (j == n or j == (width - n)
		or (i == int(height / 2) and j > n 
		and j < (width - n))) :
                print("*",end='')
            else:
                print(" ",end='')
        print("")
        n-=1 
	 
# Function to print the pattern of 'B'  

def printB(): 
	half = (int(height / 2)) 
	for i in range(height) : 
		print("*",end='') 
		for j in range(width) : 
			if ((i == 0 or i == height - 1 or i == half) 
				and j < (width - 2)):
				print("*",end='') 
			elif (j == (width - 2) 
					and not(i == 0 or i == height - 1 
						or i == half)):
				print("*",end='') 
			else:
				print(" ",end='') 
		 
		print("")
# Function to print the pattern of 'C' 
def printC(): 
	for i in range(height) : 
		print("*",end='') 
		for j in range(height - 1): 
			if (i == 0 or i == height - 1): 
				print("*",end='') 
			else:
				continue 
		print("")
		
# Function to print the pattern of 'D' 
def printD():
        for i in range(height) :
            print("*",end='')
            for j in range (height):
                if ((i == 0 or i == height - 1 
                    and j < height - 1)):
                    print("*",end='') 
                elif (j == height - 1 and i != 0
                      and i != height - 1):
                    print("*",end='') 
                else:
                    print(" ",end='')
            print("")
            

# Function to print the pattern of 'E' 
def printE():
        for i in range(height) : 
                            print("*",end='') 
                            for j in range (height) : 
                                    if ((i == 0 or i == height - 1) 
                                            or (i == int(height / 2) 
                                            and j <= int(height / 2))):
                                        print("*",end='') 
                                    else:
                                        continue 
                             
                            print("")
# Function to print the pattern of 'F' 
def printF():  
            for i in range(height) : 
                    print("*",end='') 
                    for j in range (height) : 
                            if ((i == 0) or (i == int(height / 2) 
                                                            and j <= int(height / 2))):
                                    print("*",end='') 
                            else:
                                    continue 
                     
                    print("")
printF()



# Function to print the pattern of 'G' 
def printG():
            global width
            width-=1 
            for i in range(height) : 
                    for j in range(width) : 
                            if ((i == 0 or i == height - 1) 
                                    and (j == 0 or j == width - 1)):
                                    print(" ",end='') 
                            elif (j == 0): 
                                    print("*",end='') 
                            elif (i == 0 and j <= height): 
                                    print("*",end='') 
                            elif (i == int(height / 2)
                                            and j > int(height / 2)):
                                    print("*",end='') 
                            elif (i > int(height / 2) 
                                            and j == width - 1): 
                                    print("*",end='') 
                            elif (i == height - 1 
                                            and j < width): 
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    print("") 
	 


# Function to print the pattern of 'H' 
def printH(): 
            for i in range(height) : 
                    print("*",end='') 
                    for j in range(height) : 
                            if ((j == height - 1) 
                                    or (i == int(height / 2))): 
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    print("") 
	 
 

# Function to print the pattern of 'I' 
def printI():   
            for i in range(height) : 
                    for j in range(height): 
                            if (i == 0 or i == height - 1):
                                    print("*",end='')
                            elif (j == int(height / 2)): 
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    print("") 
	 
 

# Function to print the pattern of 'J' 
def printJ(): 
    for i in range(height) :
        for j in range(height) :
            if (i == height - 1 and (j > 0 and j < height - 1)):
                print("*",end='') 
            elif ((j == height - 1 and i != height - 1) 
                   or (i > (int(height / 2)) - 1 
                   and j == 0 and i != height - 1)):
                print("*",end='') 
            else:
                print(" ",end='') 
                             
        print("") 
	 
 

# Function to print the pattern of 'K' 
def printK():
            global height
            half = height // 2
            dummy = half 
            for i in range(height) : 
                    print("*",end='') 
                    for j in range(half+1) : 
                            if (j == abs(dummy)): 
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    print("") 
                    dummy-=1 
	 
 

# Function to print the pattern of 'L' 
def printL():  
	for i in range(height) : 
		print("*",end='') 
		for j in range(height) : 
			if (i == height - 1):
				print("*",end='') 
			else:
				print(" ",end='') 
		 
		print("")

 

# Function to print the pattern of 'M' 
def printM(): 
    counter = 0 
    for i in range(height) : 
                    print("*",end='') 
                    for j in range(height+1) : 
                            if (j == height):
                                    print("*",end='') 
                            elif (j == counter 
                                            or j == height - counter - 1):
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    if (counter == int(height / 2)) : 
                            counter = -99999 
                    else:
                            counter+=1 
                    print("") 
	 
 

# Function to print the pattern of 'N' 
def printN(): 
    counter = 0 
    for i in range(height) : 
                    print("*",end='') 
                    for j in range(height+1) : 
                            if (j == height): 
                                    print("*",end='') 
                            elif (j == counter):
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    counter+=1 
                    print("") 
	 
 

# Function to print the pattern of 'O' 
def printO(): 
            space = int(height / 3) 
            width = int(height / 2) + int(height / 5) + space + space 
            for i in range(height) : 
                    for j in range(width+1) : 
                            if (j == width - abs(space) 
                                    or j == abs(space)): 
                                    print("*",end='') 
                            elif ((i == 0 
                                            or i == height - 1) 
                                            and j > abs(space) 
                                            and j < width - abs(space)): 
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    if (space != 0 
                            and i < int(height / 2)) : 
                            space-=1 
                     
                    elif (i >= (int(height / 2) + height / 5)): 
                            space-=1 
                    print("") 
	 
 

# Function to print the pattern of 'P' 
def printP():  
            for i in range(height) : 
                    print("*",end='') 
                    for j in range(height) : 
                            if ((i == 0 or i == int(height / 2)) 
                                    and j < height - 1): 
                                    print("*",end='') 
                            elif (i < int(height / 2) 
                                            and j == height - 1 and i != 0): 
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    print("") 
	 
 

# Function to print the pattern of 'Q' 
def printQ(): 
            printO() 
            d = height 
            for i in range (int(height / 2)) : 
                    for j in range(d+1) : 
                            if (j == d): 
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    print("") 
                    d+=1 
	 
 

# Function to print the pattern of 'R' 
def printR(): 
            half = (int(height / 2)) 
            for i in range(height) : 
                    print("*",end='') 
                    for j in range(width) : 
                            if ((i == 0 or i == half) 
                                    and j < (width - 2)): 
                                    print("*",end='') 
                            elif (j == (width - 2) 
                                            and not(i == 0 or i == half)): 
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    print("") 
	 
 

# Function to print the pattern of 'S' 
def printS():   
            for i in range(height) : 
                    for j in range(height): 
                            if ((i == 0 or i == int(height / 2) 
                                    or i == height - 1)): 
                                    print("*",end='') 
                            elif (i < int(height / 2) 
                                            and j == 0): 
                                    print("*",end='') 
                            elif (i > int(height / 2) 
                                            and j == height - 1): 
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    print("") 
	 
 

# Function to print the pattern of 'T' 
def printT():  
            for i in range(height) : 
                    for j in range(height+1) : 
                            if (i == 0):
                                    print("*",end='') 
                            elif (j == int(height / 2)): 
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    print("") 
	 
 

# Function to print the pattern of 'U' 
def printU():  
            for i in range(height) : 
                    if (i != 0 and i != height - 1): 
                            print("*",end='') 
                    else:
                            print(" ",end='') 
                    for j in range(height)  : 
                            if (((i == height - 1) 
                                    and j >= 0 
                                    and j < height - 1)): 
                                    print("*",end='') 
                            elif (j == height - 1 and i != 0 
                                            and i != height - 1): 
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    print("") 
	 
 

# Function to print the pattern of 'V' 
def printV(): 
            counter = 0 
            for i in range(height) : 
                    for j in range(width+1) : 
                            if (j == counter 
                                    or j == width - counter - 1): 
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    counter+=1 
                    print("") 




# Function to print the pattern of 'W' 
def printW(): 
            counter = int(height / 2) 
            for i in range(height) : 
                    print("*",end='') 
                    for j in range(height+1) : 
                            if (j == height):
                                    print("*",end='') 
                            elif ((i >= int(height / 2)) 
                                            and (j == counter 
                                                    or j == height - counter - 1)): 
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    if (i >= int(height / 2)) : 
                            counter+=1
                    print("") 
             
     

# Function to print the pattern of 'X' 
def printX(): 
            counter = 0 
            for i in range(height+1) : 
                    for j in range(height+1) : 
                            if (j == counter 
                                    or j == height - counter): 
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    counter+=1 
                    print("") 
	 
 

# Function to print the pattern of 'Y' 
def printY(): 
            counter = 0 
            for i in range(height) : 
                    for j in range(height+1) : 
                            if (j == counter 
                                    or j == height - counter 
                                            and i <= int(height / 2)):
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    print("") 
                    if (i < int(height / 2)):
                            counter+=1 
	 
 

# Function to print the pattern of 'Z' 
def printZ(): 
            counter = height - 1 
            for i in range(height) : 
                    for j in range(height) : 
                            if (i == 0 or i == height - 1 
                                    or j == counter): 
                                    print("*",end='') 
                            else:
                                    print(" ",end='') 
                     
                    counter-=1 
                    print("") 
	 
 






# to create a user-defined sized alphabet's pattern 

while(1):
    # Number of lines for the alphabet's pattern 
    height = int(input("Enter the size:"))
    # Number of character width in each line 
    width = (2 * height) - 1
    ch = input("Enter a character frm A-Z , Enter * to break:")

    if(ch =="A"):
        printA()
    elif(ch =="B"):    
        printB()
    elif(ch =="C"):
        printC()
    elif(ch =="D"):
        printD()
    elif(ch =="E"):
        printE()
    elif(ch =="F"):
        printF()
    elif(ch =="G"):
        printG()
    elif(ch =="H"):
        printH()
    elif(ch =="I"):
        printI()
    elif(ch =="J"):
        printJ()
    elif(ch =="K"):
        printK()
    elif(ch =="L"):
        printL()
    elif(ch =="M"):
        printM()
    elif(ch =="N"):    
        printN()
    elif(ch =="O"):
        printO()
    elif(ch =="P"):
        printP()
    elif(ch =="Q"):
        printQ()
    elif(ch =="R"):
        printR()
    elif(ch =="S"):
        printS()
    elif(ch =="T"):
        printT()
    elif(ch =="U"):
        printU()
    elif(ch =="V"):
        printV()
    elif(ch =="W"):
        printW()
    elif(ch =="X"):
        printX()
    elif(ch =="Y"):
        printY()
    elif(ch =="Z"):
        printZ()
    elif(ch =="*"):
        break
    else:
        print("Invalid")
    


