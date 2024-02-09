# def square(num):
#     return num**2
# a=int(input("enter the  number"))
# object=square(a)
# print("square of given number is:",object)

# def fun(string):
#     return len(string)
# a=input("enter your string:")
# print(fun(a))



# def a(n1,n2=20):
#     print("number 1 is: ",n1)
#     print("number 2 is: ",n2)
# a(30)


# def a(n1,n2):
#     print("number 1 is: ",n1)
#     print("number 2 is: ",n2)
# a(30,20)



# def value1(a,b):
#     return a+b

# def value2(a,b):
#     return a-b

# def value3(a,b):
#     return a*b

# def value4(a,b):
#     return a/b


# while True:
#     print("1: addition "
#           "\n2: substraction "
#           "\n3: multiplication"
#           "\n4: division"
#           "\n5: Exit")
    
#     b=int(input("enter your choice : "))
#     if b==5:
#         break
#     elif b==1:
#         x=int(input("enter your first number"))
#         y=int(input("enter your second number"))
#         sum=value1(x,y)
#         print("the sum of these numbers: ",sum)
#     elif b==2:
#         x=int(input("enter your first number"))
#         y=int(input("enter your second number"))
#         sub=value2(x,y)
#         print("the substraction of these numbers: ",sub)
#     elif b==3:
#         x=int(input("enter your first number"))
#         y=int(input("enter your second number"))
#         mul=value3(x,y)
#         print("the product of these numbers: ",mul)
#     elif b==4: 
#         x=int(input("enter your first number"))
#         y=int(input("enter your second number"))
#         div=value4(x,y)
#         print("the division of these numbers: ",div)
    





# a=(input("enter your string")) 
# b=a[::-1]
# print(b)
# if a==b:
#     print("paliandrome")
# else:
#     print("not paliandrome")




# def name(b):
#     return b[::-1] 
# a=input("enter your string : ")
# c = name(a)
# if a==c:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")




# def name(b):
#     if a%2==0:
#         print("it is an even number")
#     else:
#         print("it is an odd number")
# a=int(input("enter your number: "))
# b=name(a)




# def name(b,c,d):
#     return max (b,c,d)
# b=int(input("enter your first number"))
# c=int(input("enter your second number"))
# d=int(input("enter your third number"))
# e=name(b,c,d)
# print(f"{e} is the greatest number")



# a=int(input("enter the year"))
# if a%4==0:
#     print("it is a leap year")
# else:
#     print("it is not a leap year")




# ----->prime in given range<-----

# a=int(input("enter first range: "))
# b=int(input("enter second range: "))
# for i in range(a,b+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)




# ------->fibonacci<-------


# a=int(input("enter the numbers:"))
# b=0
# c=1
# d=b+c
# print(d)
# b=c
# c=d

# x=int(input("enter the range: "))
# a=0
# b=1
# print(a,b,end=" ")
# for i in range(3,x+1):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c


# ---->factorial<------


# a=int(input("enter the number: "))
# b=1
# while(a>0):
#     b=b*a
#     a=a-1
# print(b)



# a=int(input("enter a number: "))
# b=1
# if(a>0):
#     for i in range(a):
#         b=b*a
#         a=a-1
# print(b)


# --->leap year using function<---


# def leap(a):
#     if a%4==0:
#         print(a,"is a leap year")
#     else:
#         print(a,"is not a leap year")
# a=int(input("eter the year"))
# b=leap(a)



# ----->waterbill using function<-----


# def name(a):
#     if  a<=100:
#         c = a*15   
#     elif  a<=200:
#         c = 100*15+14*(a-100)
        
#     elif a>=201:
#         c = 100*15+100*14+12*(a-200)
#     print("the total is: ",c)
# a=int(input("enter the litres"))
# b=name(a)



# def name(**x):
#     print("first name is:" +x["fname"])
#     print("last name is:" +x["lname"])
# name(fname="james",lname="john")



# a=lambda b,c:b+c
# d=int(input("enter a number"))
# q=int(input("enter a number"))
# print("the product is: ",a(d,q))


# def word():
#     string="python function"
#     x=5
#     def number():
#         print(string)
#         print(x)
#     number()
# word()


# def fact(x):
#     if x==1:
#         return 1
#     else:
#         return(x*fact(x-1))
# a=int(input("enter the number"))
# print("the factorial is: ",fact(a))



# a=[1,2,3,4,5,6]
# def name(numbers):
#     for i in numbers:
#         print(i)
# name(a)



# d={}
# def create():
#     a=int(input("enter the number of pairs; "))
#     for i in range (a):
#         p=input("enter the key: ")
#         q=input("enter the value: ")
#         d[p]=q
#     print("created")
# def update():
#     p=input("enter the key: ")
#     if p in d:
#         q=input("enter the value: ")
#         d[p]=q
#     else:
#         print("invalid")   
# def delete():
#     p=input("enter the key: ")
#     if p in d:
#         d.pop(p)

# def display():
#     print(d)
# while True:
#     print("1: creation "
#           "\n2: update"
#           "\n3: delete"
#           "\n4: display"
#           "\n5: Exit")
#     x=int(input("enter your choice"))
#     if x==1:
#         create()
#     elif x==2:
#        update()
#     elif x==3:
#        delete()
#     elif x==4:
#         print(d)
#     elif x==5:
#         break



# d={}
# def create():
#     a=int(input("enter the number of pairs; "))
#     for i in range (a):
#         p=input("enter your a/c No: ")
#         q=input("enter your savings: ")
#         d[p]=q
#     print("created")
# def deposite():
#     p=input("enter the key: ")
#     if p in d:
#         d[p]=q
#         q=input("enter the value: ")
#     print("deposite added")
# def withdrawal():
#     p=input("enter the key: ")
#     if p in d:
#         d[p]=q
#         q=input("enter the value: ")
    
# while True:
#     print("1: creation "
#             "\n2: deposite"
#             "\n3: withdrawal"
#             "\n4: display"
#             "\n5: Exit")
#     x=int(input("enter your choice"))
#     if x==1:
#         create()
#     elif x==2:
#         deposite()
#     elif x==3:
#         withdrawal()
#     elif x==4:
#         print(d)
#     elif x==5:
#         break




# a=[]
# b=int(input("enter your number"))
# a.append(b)
# print(a)
# for i in a:
#     print(i)



# -----> multiplication table of a number <-------


# a=(input("enter a number: "))
# print(a[1])



n=int(input("Enter number"))
# sum=0
# for digit in str(n):
#     sum=sum+int(digit)
# print("Sum of digits",sum)

    
    
for n>9



