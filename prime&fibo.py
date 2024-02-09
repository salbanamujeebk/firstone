# a=int(input("enter a number"))
# if a/a==1 and a/1==a:
#     print("it is a prime number")
# else:
#     print("it is not a prime number")





# num=int(input("enter the number"))
# if num>1:
#     for i in range(2,int(num/2+1)):
#         if num%i==0:
#             print(num,"is not a prime number")
#             break
#     else:
#         print(num,"is a prime number")
# else:
#     print(num," is not a prime number")


a=int(input("enter first range: "))
b=int(input("enter second range: "))
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
