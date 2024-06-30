# list1 = [100, 200, 300, 400, 500]
# list2=list1[::-1]
# print(list2)

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3=[]
# k=0
# for i,j in zip(list1,list2):
#     list3.append(i+j)
#     k+=1
#
# print(list3)

# a=[1,2,3,4,5,6,7,8,9,10]
# for i in range(a.__len__()):
#     a[i]**=2
# print(a)

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# list3=[]
# for i in list1:
#     for j in list2:
#         list3.append(i+j)
# 
# print(list3)


# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# list2.reverse()
# for i,j in zip(list1,list2):
#     print(i,"  ",j)

# t= ("Mike", "", "Emma", "Kelly", "", "Brad")
# t=list(t)
# while "" in t:
#     t.remove("")
# t=tuple(t)
# print(t)


# t1= (5, 10, 15, 20, 25, 50, 20)
# t1=list(t1)
# q=t1.index(20)
# t1[q]=200
# t1=tuple(t1)
# print(t1)

# list1 = [5, 20, 15, 20, 25, 50, 20]
# while 20 in list1:
#     list1.remove(20)
# print(list1)

# tr=("AWAIS",)
# print(tr)

# tuple1 = (10, 20, 30, 40)
# a,b,c,d=tuple1
# print(a)
# print(b)
# print(c)
# print(d)


# tuple1 = (11, 22, 33, 44, 55, 66)
# tuple2=tuple1[3:5]
# print(tuple2)

# tuple1 = (11, [22, 33], 44, 55)
# tuple1[1][0]=222
# print(tuple1)

# tuple1 = (50, 10, 60,10,10, 70, 50)
# a=tuple1.count(10)
# print(a)

# def f(*d):
#     for i in d:
#         print(i,end=",")
#     print("\b\n")
# f(20,23,23,34,45,656)
# f((3,2,"asd"),23.34,"asgg",34,45,"AWAIS")
# f(20,23)

# def show_employee(x,y=9000):
#     print("Name: "+x+"\n"+"Salary: "+str(y))
# f=show_employee
# f("Ben", 12000)
# f("Jessa")

# def sum(x):
#     if x==0:
#         return 0
#     else:
#         return x+(sum(x-1))
# print(sum(10))

# def f(a,b):
#     def n():
#         return a+b
#     return 5+n()
#
# print(f(3,4))


# def main():
#     a=[]
#     for i in range(4,30,2):
#         if i%2==0:
#             a.append(i)
#     print(a)
# main()

# x = [4, 6, 8, 24, 12, 2]
# print(max(x))

#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("\n")


# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i>500:
#         break
#     if i%5==0:
#         if i>150:
#             continue
#         print(i)


# for i in range(1,6):
#     k=6-i
#     for j in range(1,6-i+1):
#         print(k,end=" ")
#         k-=1
#     k=0
#     print("\n")

# list1 = [10, 20, 30, 40, 50]
# for i in range(list1.__len__()-1,-1,-1):
#     print(list1[i])
# list1.reverse()
# list1=list1[::-1]
# for i in list1:
#     print(i)



# for i in range(-10,0):
#     print(i)
# else:
#     print("Done............")

# ***************PRIME NUMBERS**************
# s,e=input().split()
# s=int(s)
# e=int(e)
# for x in range(s,e):
#     flag=0
#     for i in range(2,x):
#         if x%i==0:
#             flag=1
#     if flag!=1:
#         print(x)

# **********FABONACIIIII*********
# a=0
# b=1
# print(0)
# print(1)
# for i in range(8):
#     n=a+b
#     print(n)
#     a=b
#     b=n

#***********FACTORIAL**************
# f=int(input())
# fac=1
# for i in range(1,f+1):
#     fac*=i
# print(fac)



# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(my_list.__len__()):
#     if i%2!=0:
#         print(my_list[i],end=" ")
# ********REVERSE**************
# a=int(input())
# b=0
# while a>0:
#     r=a%10
#     b=b*10+r
#     a//=10
# print(b)



# b=0
# sum=0
# for i in range(5):
#     b=b*10+2
#     sum+=b
# print(sum)




# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


# for i in range(9):
#     if i<=4:
#         print("*"*(i+1))
#     else:
#         print('*'*(9-i))
