'''
l1=set("hello world")
print(l1)
l1.pop()
print(l1)

a={1,2,3,4,5,6}
b={7,8,9.1,2,3}
a.union(b)
print(a)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}


print(A.intersection(B))

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A-B)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A.symmetric_difference(B))
#op{1, 2, 3, 6, 7, 8}

set1 = {1, 5, 9, 0}
set2= {2, 4, -5}

print(set1.isdisjoint(set2))


a=int(input("enter value::"))
if(a==5):
    print("a is",5)
if(a>3 and a<8):
    print("a is in 3-8")

#check whether one no is odd or even
#check no is positive or negative

a=5
if(a%2==0):
    print('even number')
else:
    print('odd number')

#check no is positive or negative
a=16
if(a>0):
    print("positive")
else:
    print("neagative") 

a=input("enter string:")
if(a==a[::-1]):
    print("Palindrome")
else:
    print("not a palidrome ")d


#program to check mark and grades
a=int(input("enter value:"))
if(a==100):
    print("grade a")
elif(a>=90 and a<=99):
    print("grade b")
elif(a>=80 and a<=89):
    print("grade c")
elif(a>=70 and a<=79):
    print("grade d")
elif(a>=0 and a<=49):
     print("grade f")

else:
    print("invalid")

a=input("enter string:")
if(a[0]==a[-1] and a[-1]==a[int(len(a)/2)]):
   print("same")
else:
    print("different")'''

#Hacker rank program
n=int(input("enter an integer"))
if(n%2!=0):
    print("weird")
elif(n%2==0 and n>=2 and n<=5):
    print("not weird")
elif(n%2==0 and n>=6 and n<=20):
    print("wierd")
elif(n%2==0 and n>=20):
    print("not weird")
    







   

