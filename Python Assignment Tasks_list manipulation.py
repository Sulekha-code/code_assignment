'''
#python syntax
#print HEllo world
a="Hello world"
print(a)

#comments in python

"""
multiline docstring."""
print("Hello, World!")


#python variables
x=5
y="sulekha"
print(x,y)


#add variable to another vaiable
x=5
y=6
c=x+y
print(c)

#python numbers examples
x = 1
y =3.2
z = 1+1j

print(type(x))
print(type(y))
print(type(z))

#create integers
x = 1
y = 65656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

#create floating numbers
x = 12e3
y = 13E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


#create complex numbers
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))
'''
'''
#python casting
#int
x = int(3)
y = int(25.8)
z = int("3")
print(x)
print(y)
print(z)

#float value
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

#string value
x = str("sulekha")
y = str(2.0)
z = str(3.0)
print(x)
print(y)
print(z)


#Python Strings
x="sulekha"
print(x[-1])

#get characters from position 2 to 5
x="sulekha"
print(x[2:5])

#remove whitespace from beginning
x=" sulekha"
y=x.strip()
print(y)

#Return length of string
x="sulekha"
y=len(x)
print(y)

#convert string to upper  case
a = "SULEKHA"
b=a.lower()
print(b)

#convert string to lower case
a = "SULEKHA"
b=a.upper()
print(b)

#replace strings
a="sulekha"
b=a.replace("u","e")
print(b)

#split string
a="Hello world"
b=a.split()
print(b)

#Python Operators
#addition opearators
x=3
y=8
z=x+y
print(z)

#subtraction
x=8
y=3
z=x-y
print(z)

#multiplication
x = 5
y = 3

print(x * y)

#modulus
x = 5
y = 2

print(x % y)

#=================#
#python lists
#create lists
a=["apple", "banana", "cherry"]
print(a)

a= ["apple", "banana", "cherry"]
print(a[1])

a= ["apple", "banana", "cherry"]
a[1] = "blackcurrant"
print(a)

#get length of list

a= ["apple", "banana", "cherry"]
b=len(a)
print(b)

#append
#add item in list
a= ["apple", "banana", "cherry"]
a.append("orange")
print(a)

#remove
a= ["apple", "banana", "cherry"]
a.remove("banana")
print(a)
'''
'''#pop
a= ["apple", "banana", "cherry"]
a.pop()
print(a)
#del
a= ["apple", "banana", "cherry"]
del a[0]
print(a)

a = ["apple", "banana", "cherry"]
a.clear()
print(a)

#using list constructor
a = list(("apple", "banana", "cherry"))
print(a)

a=[1,2,3,4,5,6,7]
x=sum(a)
print(a)
b=len(x)
print(b)
c=a/b

print(c)
#smallest largest and middle value sum

a=[4,5,6,1,2.3,4,5,6,6,9]
b= a[0]
c = a[-1]
d =a[int(len(a)/2)]

print((b+c+d)/3)

#middle value and middle character

a=["hello","python","world","computer","value"]
b=a[int(len(a)/2)]
print(b)
b=b[int(len(b)/2)]
print(b)
print(a[0][0]+a[0][-1]+a[-1][0]+a[-1][-1])'''

'''
#    0     1 2 3   4        -1                      
a=[[1,2,3],4,5,6,[8,9],[[44,55,66],[66,77],["hello","python","welcome"]]]
#b= [[44, 55, 66], [66, 77], ['hello', 'python', 'welcome']]
#c= ['hello', 'python', 'welcome']
print("a=",a)

print(a[0][2])
print(a[0][-1])

#tasks #55 #3 #5 #9 #77 #44 #welcome #come #yth #llo #"python",welcome

print(a[5][0][1])
print(a[0][-1])
print(a[2])
print(a[4][-1])
print(a[-1][1][-1])
print(a[-1][0][0])
print(a[-1][-1][-1])
print(a[-1][-1][-1][3:])
print(a[-1][-1][-2][1:-2])
b=a[-1]
#print("b=",b)
c=b[-1]
#print("c=",c)
d=c[0]
#print(d[2:])
print("\""+c[1]+"\""+","+c[2])
#ell
print(a[-1][-1]
      a=[[1,2,3],4,5,6,[8,9],[[44,55,66],[66,77],["hello","python","welcome"]]]
#wce
b=a[-1]
#print("b=",b)
c=b[-1]
#print("c=",c)
d=c[-1]
print(d[0]+d[3]+d[-1])


#   0      1 2 3   4        -1
a=[[1,2,3],4,5,6,[8,9],[[44,55,66],[66,77],["sulekha","anupama","sidharth"]]]
#b=[[44,55,66],[66,77],["sulekha","anupama","sidharth"]]]
#c=["sulekha","Anupama","sidharth"]

##tasks #55 #3 #5 #9 #77 #44 #sidharth #kha  #apm   #shth  # ule

print(a[-1][0][1])
print(a[0][-1])
print(a[2])
print(a[4][-1])
print(a[-1][0][0])
print(a[-1][-1][-1])
print(a[-1][-1][0][4:])
print(a[-1][-1][1])
#d=a[-1][-1][1]
#print(d[0]+d[3]+d[-2])
#sdat
