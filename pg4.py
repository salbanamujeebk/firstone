# a=int(input("enter the litres"))
# if a>0 and a<=100:
#     c = a*15
# if a>=101 and a<=200:
#     c = 100*15+14*(a-100)
# if a>=201:
#     c = 100*15+100*14+12*(a-200)
# print("the total is : ",c)




# a=int(input("enter the litres"))
# if a>0 and a<=100:
#     c = a*15
# if a>=101 and a<=200:
#     c = 100*15+14*(a-100)
# if a>=201:
#     c = 100*15+100*14+12*(a-200)
# print("the total is : ",c)




# a=int(input("enter a number : "))
# if a<0:
#     print(a,"is negative")
# elif a>0:
#     print(a,"is positive")
# else:
#     print("zero")

# print('%s and %s are friends'%(f1,f2))



# a=int(input("enter a number : ")).split()
# b=int(input("enter another number : "))
# c=input("enter the operation : ")
# if c=="+":
#     d=a+b    
# elif c=="-":
#     d=a-b    
# elif c=="*":
#     d=a*b  
# elif c=="/":
#     if b!=0:  
#         d=a/b
#     else:
#         print("Not divisible")
#         exit()       
# else:
#     print("invalid")
# print("The result of %s %s %s is : %s"%(a,c,b,d))





# intersection_result = list(set(list1).intersection(list2))
# abc=[10,20,30,40,50,60]
# pqr=[50,10,80,90]
# xyz=set(abc).intersection(pqr)
# print(xyz)



# a=input("enter your first list: ").split()
# b=input("enter your second list : ").split()
# c=set(a).intersection(b)
# print(list(c))



# a=[25,54,87]
# s=[]
# for i in a:
#     j=i**2
#     s.append(j)
# print("list of squares is :",s)



# z="salbana"
# for i in z:
#     if i=="b":
#         print("if block")
#     else:
#         print(i)



# print(range(15))
# print(list(range(15)))
# print(list(range(15,20,)))
# print(list(range(15,20,2)))


# for i in range(15):
#     print(i)

# for i in (range(15,50)):
#     print(i)

# a=[]
# for i in range(0,15):
#     a.append(i)
# print(a)



# t=("python","loops","sequence","condition","range")
# for i in range(len(t)):
#     print(t[i].upper())
    

# q=[]    
# t=("python","loops","sequence","condition","range")
# for i in range(len(t)):
#     print(t[i].upper())
#     c=t[i].upper()
#     q.append(c)
# print(q)


# a=10
# for i in range(0,10):
#     for j in range(0,i+1):
#         print('* ',end="")
#     print()



# b=int(input("enter a range"))
# for i in range(0,b):
#     for j in range(0,b-i):
#          print('* ',end="")
#     print()





# a=1,5,8,2
# c=sorted(a,reverse=True)
# print(c)



# list=[]
# n=int(input("enter the range : "))
# for i in range(n):
#     a=int (input(f"enter the elements  {i+1}:"))
#     list.append(a)
# while True:
#     s = int(input("enter the range of largest number : "))
#     if s>n:
#         break
#     else:
#         q=sorted(list,reverse=True)[:s]
#         print(f"The {s} largest numbers are: {q}")




 



# a=5
# for i in range(0,5):
#     for j in range(0,i+1):
#         print('* ',end="")
#     print()
# for i in range(1,a):
#     for j in range(0,a-i):
#          print('* ',end="")
#     print()



# for i in range(65,70):
#     for j in range(65,i+1):
#         print(chr(j),end=" ")
#     print() 



# a=5
# for i in range(0,5):
#     for j in range(0,i+1):
#         print('* ',end="")
#     for j in range(0,i+1):
#         print('* ',end="")
#     print()






# n=5
# k=n-1
# for i in range(0,n):
#     for j in range(0,k):
#         print(end="")
#     k=k-1
#     for j in range(0,i+1):
#         print("* ",end="")
#     print()


# # count=1
# while count<=5:
#     print(count)
#     count+=1


# counter=0
# while counter <10:
#     counter=counter+3
#     print("python loops")
# else:
#     print("invalid")
        




# list=[]
# n=int(input("enter the range : "))
# for i in range(n):
#     a=int (input(f"enter the elements  {i+1}:"))
#     list.append(a)
# while True:
#     s = int(input("enter the range of largest number : "))
#     if s>n:
#         break
#     else:
#         q=sorted(list,reverse=True)[:s]
#         print(f"The {s} largest numbers are: {q}")


# a=int(input("enter the n number"))
# while a!=-1:
#     a=int(input("enter the number"))

# total=0
# a=int(input("enter the number"))
# while a!=0:
#     total += a
#     a=int(input("enter the number"))
# print("the total is : ",total)
        
   


# a=int(input("enter the number"))
# for i in range(a):
#     for j in range(a-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*  ",end=" ")
#     print()

# for a in "python loops":
#     if a=="o" or a=="p"or a=="l":
#         continue
#     print("current letter:",a)

# a="salbana"
# for i in a:
#     if i=="b":
#         break
#     print(i)

# a="salbana"
# for i in a:
#     if i=="l":
#         continue
#     print(i)


# for i in range(10):
#     pass


