# str="AWAIS"
# str1=str[0]+str[str.__len__()//2]+str[str.__len__()-1]
# print(str1)


# str=input("Enter any string:    ")
# str1=str[(str.__len__()//2)-1]+str[str.__len__()//2]+str[(str.__len__()//2)+1]
# print(str1)


# s1 = "Ault"
# s2 = "Kelly"
# s3=s1[:s1.__len__()//2]+s2+s1[s1.__len__()//2:]
# print(s3)


# s1=input("enter s1: ")
# s2=input("enter s2: ")
# s3=s1[0]+s2[0]+s1[s1.__len__()//2]+s2[s2.__len__()//2]+s1[-1]+s2[-1]
# print(s3)







# str="AWAIS raza"
# str1=""
# for i in str:
#     if i.islower():
#         str1+=i
# for i in str:
#     if i.isupper():
#         str1+=i
# print(str1)





# str1 = "P@#yn26at^&i5ve"
# digit=0
# char=0
# sym=0
# for i in str1:
#     if i.isalpha():
#         char+=1
#     elif i.isdigit():
#         digit+=1
#     else:
#         sym+=1
# print("Number of digits:  ",digit)
# print("Number of characters:  ",char)
# print("Number of symbols:  ",sym)



# s1=input("Enter s1:  ")
# s2=input("Enter s2:  ")
# s3=""
# for i,j in zip(range(s1.__len__()),range(s2.__len__()-1,-1,-1)):
#     s3=s3+s1[i]+s2[j]
# print(s3)





# def comp(s1,s2):
#     flag=0
#     for i in s1:
#         for j in s2:
#             if i==j:
#                 flag+=1
#                 break
#     if flag==len(s1):
#         return True
#     else:
#         return False
# s1 = "Yn"
# s2 = "PYnative"
# print(comp(s1,s2))


# str1 = "Welcome to PAKISTAN. pakistan awesome, isn't it?"
# str2=str1.lower()
# print(str2.count("pakistan"))



# str1 = "PYnative29@#8496"
# count=0
# sum=0
# for i in str1:
#     if i.isdigit():
#         sum+=int(i)
#         count+=1
# print(sum,"   ",sum/count)


# str1 = "PYnative"
# print(*reversed(str1))
# # OR
# print(str1[::-1])

# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# a=str1.rfind("Emma",0,str1.__len__())
# print(a)



# str1 = 'Emma-is-a-data-scientist'
# a=0
# for i in range(str1.__len__()):
#     if str1[i]=='-':
#         if a!=0:
#             print(str1[a+1:i])
#         else:
#             print(str1[a:i])
#         a=i
# for i in range(str1.__len__()-1,-1,-1):
#     if str1[i]=='-':
#         print(str1[i+1:])
#         break

# str1 = 'Emma-is-a-data-scientist'
# str2=str1.split("-")
# for i in str2:
#     print(i)



