#   Sum of previous Two numbers give next numbers in list
#Fibonacci series 0 1  1 3 5 8 13 21

#For example if we start
# 0 and 1 next number will be 0+1=1
#Than 0,1,1 will give next number
#.....a b c 
#Then 0,1,1,2,5 will give next number but as we need previous two number will make 
#a=b and b=c so will get o/p as 1+1=2and the 2+1=3 and loo will continue till number its given 


#Fabonicci series
'''a1=int(input("enter a number"))
b1=int(input("enter a number"))
a=0
b=1
print(a,b,end=' ')
for i in range(15,20):
      c=a1+b1 #1
      print(c,end=' ')
      c=d 
      b=c
      
#Factorial number#
#6=6*5*4*3*2*1
n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
      
      
#Armstong number 153=1*1*1+5*5*5+3*3*3
#num=sum
#153=153%10=3 is remainder so we got unit place
#153//10=15

#Armstrong number#

num=int(input("enter a number"))#153
sum=0
a=num
while(num>0):   
    dg=num%10       #153%10  #15%10   #1%10
    sum=sum+dg*dg*dg# sum=27#sum=125+27# sum=1+125+27
    num=num//10 #15    
if(sum==a):
    print("Armstrong number")
else:
    print("not an armstrong number")
    


#program4

#list of armstrong numbers between two ranges

#ip 197  ===> not armstrong
#ip 370  ==> armstrong
a=int(input("enter a number"))
b=int(input("enter a number"))
c=[]
for num in range(a,b+1):
    a=num
    sum=0
    while(num>0):
        dg=num%10
        sum=sum+dg*dg*dg
        num=num//10     
    if(sum==a):
        c.append(a)
print(c)


a=int(input("enter starting number:"))
b=int(input("enter ending number:"))
c=[]
for n in range(a,b+1):
    s = str(n)
    l = len(s)
    sum = 0
    for i in s:
        sum = sum+(int(i)**l)
    if(sum == n):
        c.append(n)
print(c)

n = int(input("enter a number:"))#123
s = str(n)#"123"
l = len(s)#3
sum = 0
for i in s:
    sum = sum+(int(i)**l)
if(sum == n):
    print("armstrong")
else:
    print("Not armstrong")

#sum of digits 

#ip: 145 ===> 10,even (1+4+5)
#ip:379 ===> 19,odd (3+7+9)
    

num=int(input("enter 1st number:"))
sum=0
while(num>0):
    dg=num%10
    sum=sum+dg #0+5+4+1=10
    num=num//10
if (sum%2==0):
    print("even number")
else:
    print("odd number")


#program6

#product of digits

#ip: 145 ===> 20  (1*4*5)
#ip:379 ===> 189  (3*7*9)
#ip: 210 ===> 0 ===> 2 , zero replaced with 1
# 222 ===> 8

num=int(input("enter 1st number:"))
product=1
while(num>0):
    dg=num%10
    product=product*dg  #0+5+4+1=10
    num=num//10
print(product)

#program7

#add all odd numbers, ever numbers in a number separately, check whether both are equal or not

#ip: [2,3,4,5,6,7,10,4,10,3,5,6,7,7,8,9,1,2,3,4,5]
# add all the odd numbers  add all the even numbers 
#check whether both are equal number

a=[2,3,4,5,6,7,10,4,10,3,5,6,7,7,8,9,1,2,3,4,5]
b=[]
c=[]
evensum = 0
oddsum = 0
for i in a:
    if(i%2==0):
        b.append(i)
        evensum= evensum+i 
    else:
        c.append(i)
        oddsum= oddsum+i 
print("even numbers",b)
print("odd numbers",c)
print("even sum",evensum)
print("odd sum",oddsum)
if(evensum==oddsum):
    print("Equal")
else:
    print("Not equal")

#program1

#check whether a no is prime or not

#i/p = 33
#non prime

n=int(input("enter 1st number:"))
if(n>1):
    for i in range(2,n-1):
        if(n%i):
            print("Not prime")
            break
    else:
        print("prime number")
#program2

#check list of prime numbers within a range

#input1 22
#input2 35
#output: 23,29,31 (prime no between two ranges)

a=int(input("enter starting number:"))
b=int(input("enter ending number:"))
c=[]
d=[]
for i in range(a,b+1): 20 4o
    for n in range(2,i):2,20
        if(i%n==0):20%2=
            c.append(i)
            break
    else:
        d.append(i)
print("not prime",c)
print("prime number",d)

#program8

#add all positive numbers, negative numbers in a number separately, check whether both are equal or not

#ip: [2,3,-4,5,6,-7,10,4,-10,3,-5,6,-7,7,8,-9,1,2,3,4,-5]
# add all the +ve numbers  add all the -ve numbers 
#check whether both are equal number


a=[2,3,-4,5,6,-7,10,4,-10,3,-5,6,-7,7,8,-9,1,2,3,4,-5]
c=[]
d=[]
positivenumber=0
Negativenumber=0
for i in a:
    if(i>0):
        c.append(i)
        positivenumber=positivenumber+i
    else:
        d.append(i)
        Negativenumber=Negativenumber+i
print("positive numbers",c)
print("Negative numbers",d)
print("postivenumber",positivenumber)
print("Negativenumber",Negativenumber)
if(positivenumber==Negativenumber):
    print("Equal")
else:
    print("Not Equal")'''
        
#program9 (*)
#fizzbuzz

#ip 2  15
#op
#%3 ==> fizz
#%5 ==> buzz
#%3 and %5 ==> fizzbuzz
#na
#2  na
#3  fizz
#4  na
#5  buzz
#6  fizz
#7  na
#8  na
#9  fizz
#10  buzz
#11  na
#12  fizz
#13  na
#14  na
#15  fizzbuzz


x=int(input("enter starting number:"))
y=int(input("enter ending number:"))
for i in range(x,y):
    if i%3==0 and i%5==0:
               print(i,"fizzbuzz")
    elif i%3==0:
        print(i,"buzz")
    elif i%5==0:
        print(i,"fizz")
    else:
        print(i,"na")

