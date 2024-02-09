# dict1={
#     "name":"John",
#     "email":"john@gmail.com",
#     "phone":7789564210
# }




# q={"a","b","c","d","e"}
# w={"c","e","a"}
# s={"a","c","d"}
# p={"a","c","d"}
# print(q>s)
# print(s<q)
# print(q>w)
# print(s==p)


# dict={"name":"salbana","place":"kodiyathur","phone":7845123698}
# print(dict)
# print(dict["name"])
# dict["email"]="salbana@gmail.com"
# print(dict)
# dict["name"]="aswathy"
# print(dict)
# del dict["name"]
# print(dict)
# for i in dict:
#     print(dict[i])

# a=[1,2,3,4,5]
# b=[x**2 for x in a]
# print(b)

# list=[x**2 for x in [1,2,3]]
# print(list)


# a=[1,2,3,4,5,6,7,8,9,10]
# b=[ i for i in a if i%2==0]
# print(b)


# q=['a','b','c','d']
# w=[[j for j in range(3,10)]for i in range(5)]
# print(w)



# line=[1,2,3,4,5]
# set={i*3 for i in line}
# print(set)


# l=[1,2,3,4,5]
# s={i*3 for i in line if i%2==0}
# print(s)


# key=['a','b','c','d']
# value=[1,2,3,4]
# d={i:j for(i,j) in zip(key,value)}
# d=dict(zip(key,value))
# print(d)


# a={x.upper():x*3 for x in 'coding'}
# print(a)

# a="ABC"
# dic={x:{y:x+y for y in a}for x in a}
# print(dic)


# i=10
# if(i<15):
#     print("10 is less than 15")
# print("i am not in if")


# j=int(input("enter a number : "))
# if(j<15):
#     print("%s is smaller than 15"%j)
# else:
#     print("%s is greater than 15"%j)


# k=int(input("enter a number : "))
# if(k<15):
#     print(k,"is smaller than 15",)
# else:
#     print(k,"is greater than 15",)



# i=20
# if(i==10):
#     if(i<15):
#         print("i is smaller than 15")
#     if(i<12):
#         print("i is smaller than 12 too")
#     else:
#         print("i is greater than 15")
# else:
#     print("not equal")



# i=20
# if(i==20):
#     print("i is 10")
# elif(i==15):
#     print("i is 15")
# elif(i==20):
#     print("i is 20")
# else:
#     print("i is not present")


# i=int(input("enter your mark:"))
# if i>100:
#        print("invalid")
# elif i>=90 :
#     print("A+")
# elif(i>=80):
#     print("B+")
# elif(i>=70):
#     print("C+")
# elif(i>=60):
#     print("D+")
# else:
#      print("fail")







# i=int(input("enter a number"))
# j=int(input("enter a number"))
# k=int(input("enter a number"))
# if(i>j):
#     if(i>k):
#         print(i,"is is greater")
# if(j>i):
#     if(j>k):
#         print(j,"is greater")
#     else:
#         print(k,"is greater")   
     


i=int(input("enter a number"))
j=int(input("enter a number"))
k=int(input("enter a number"))
# if i>j and i>k:
#      print(i,"is greatest number")
# elif j>i and j>k:
#      print(j,"is greatest number")
# else:
#      print(k,"is greatest number")

c = min(i,j,k)
print(c)














        








