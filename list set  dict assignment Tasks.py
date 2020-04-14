'''#Tasks 12/04/2020
#creation an empty list
l1=[]
print(l1)


#create an Empty tuple
l1=()
print(l1)

#create an Empty set
l1={}
print(l1)


#TASK 2
##create empty list#concatenate it with [5,6,8,9]
L1=[]
L1= L1+[5,6,8,9]
print(L1)
##add 8,9,1,5,6,7,8 
L1.append(8)
print(L1)
L1.append(9)
print(L1)
L1.append(1)
print(L1)
L1.append(5)
print(L1)
L1.append(6)
print(L1)
L1.append(7)
print(L1)
L1.append(8)
print(L1)
###find no of occurence of 8#
L2=L1.count(8)
print(L2)
##find average of the list#
L2=len(L1)
print(L2)
##find sum of list
L2=sum(L1)
print(L2)
Average=sum(L1)/len(L1)
print("Average is",Average)
#find sum of list + min ele + max ele of list
L3=min(L1)
L4=max(L1)
L5=sum(L1)
print(L3+L4+L5)
##find mean median of list
Mean=sum(L1)/len(L1)
print("Mean is",Mean)
#Median={(n+1)/2}th
L2=len(L1)
print(L2)
L1.sort()
median_position = int((L2+1)/2)
median = L1[median_position]
print(median)
##remove duplicates from concatenated list
L2=set(L1)
print(L2)
L3=list(L2)
print(L3)
#give output in tuple format
L2=tuple(L1)
print(L2)


#TASK3#
#create two empty sets
#empty curly braces will make empty dictionary in python.To make a set
#without elements we use set()
set1={}
print(type(set1))
set1=set()
print(type(set1))
l1=7,8,9,1,2,3,4,5
set1.update(l1)
print(set1)
set2={}
print(type(set2))
set2=set()
print(type(set2))
l2=4,5,6,0
set2.update(l2)
print(set2)
##check whether set2 is subset of set 1 ?
print(set1)
print(set2)
#set1={1, 2, 3, 4, 5, 7, 8, 9}
#set2={0, 4, 5, 6}
#Returns true if all elements of set X present in set Y
z=set1.issubset(set2)
print(z)
##check whether both are disjoint ?

print(set1.isdisjoint(set2))
#remove 8 from set1#discard 0 from set2#
set1.remove(8)
print(set1)

##discard 0 from set2#
set2.remove(0)
print(set2)

##find sum(set1 union set2)
set1.union(set2)
print(set1)
z=sum(set1)
print(z)



#TASK 3

#create two tuples (1,4,5,6,7) (5,6,7,8,9)
l1=(1,4,5,6,7)
l2=(5,6,7,8,9)
l1=set(l1)
l2=set(l2)
print(l1)
print(l2)
##concatenate two tuples after duplicate removal from both
l1=tuple(l1)
l2=tuple(l2)
print(l1)
print(l2)
sum=l1+l2
print(sum)

#find the index value of 9#
#sum=(1, 4, 5, 6, 7, 5, 6, 7, 8, 9)
print(sum[9])
#find common elements between above elements with {0,4,5}
l3={0,4,5}
sum=set(sum)
print(sum)
print(sum.intersection(l3))

#multiple above tuple 3 times#
sum1=tuple(sum)
print(sum1)
result=sum1*3
print(result)


#TASK4
#create a dictionary
a={1:["english","maths",{"science":["bio-zoology","bio-botany","physics"]}],2:(10,20,40,"python program")}
print(a[1])
b=a[1]
print(b)
#b=['english', 'maths', {'science': ['bio-zoology', 'bio-botany', 'physics']}]
c=a[2]
print(c)
#c=(10, 20, 40, 'python program')
print(b[0])#english
print(b[1])#maths
print(b[2])#'science': ['bio-zoology', 'bio-botany', 'physics']}

##extract botany
print(b[2])#["science"][1][4:])
print(b[0]+b[1],b[2]["science"].key)'''


a={1:["english","maths","science",["bio-zoology","bio-botany","physics"]],2:(10,20,40,"python_program")}
#zoology
print(a[1][3][0][4:])
#zoo
print(a[1][3][0][4:7])
#thon
print(a[2][3][2:6])
#10,20,30
print(a[2][0:3])



