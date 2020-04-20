
# Python Program to find the factors of a number

# This function computes the factor of the argument passed
'''def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 320

print_factors(num)


def print_fibo(n):
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(0,n-2):
            c = a+b
            print(c,end=" ")
            a = b
            b = c
            
a = int(input("Enter a numbers of fibonacci elements:"))
print_fibo(a)


def print_function(n):
    if(n%2==0):
        print("Even numbers")

    else:
        print("odd numbers")
        
a=int(input("enter number:"))
print_function(a)

#prime number
def print_function(n):
    s=""
    for i in range(2,n-2):
        if n%i==0:
            sulekha="Not prime number"
            break
    else:
        sulekha="prime number"
    return sulekha

a=int(input("enter value"))
sid = print_function(a)
print(sid)

#postive negative
def print_function(c,d):
    for i in range(c,d):
          if(i>0):
              print("positive number")
          else:
              print("Negative number")

a=int(input("enter number"))
b=int(input("enter number"))
print_function(a,b)

#get two numbers from user and do below process
#(a + b)(a - b)
def calculate_function(a,b):
    return(a+b)*(a-b)
d=calculate_function(5,8)
print(d)


#get three numbers from user and do below process
#(a + b)(a - b)(a-c)
def function(a,b,c):
    d=(a+b)*(a-b)*(a-c)
    return(d)
x=int(input("enter number"))
y=int(input("enter number"))
z=int(input("enter number"))
d=function(x,y,z)
print(d)

#get a string from user and write a function to
#return concatenation of first letter
#middle letter and last letter of a string
def calculate(b):
    n=a[0]+a[int(len(a)/2)]+a[-1]
    return(n)
a=input("enter string value")
n=calculate(a)
print(n)

