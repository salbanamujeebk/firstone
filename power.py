# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# # print(a**b)
# c=a**b
# # print('the answer is : ',c)
# # print("the power of {} and {} is {}".format(a,b,c))
# print(f"the power of {a} and {b} is {c}")



# z=int(input("enter a number"))
# x=int(input("enter a number"))
# q=z/x3,
# p



# q=[1,2,3,4]
# s=q.pop()
# print(s)
# print(q)

# p=["a","b","c"]
# # p.remove("b")
# # print(p)
# p.reverse()
# print(p)

# slicing::
# a=input("enter your string")
# b=a[::-1]
# print(b)

# a=[1,2,3,4,5]
# b=a*2
# print(b)

# x=[7,5,4,8]
# y=[1,2,3,4,]
# q=x+y
# print(x)
# print(q)


# z=[1,2,3,4]
# v=len(z)
# print(v)


# a=[1,2,3,4,5,6,7,8,9,1,2,3]
# b=[]
# for i in a:
#     b.append(i)
# print(b)
# print(25 in a)
# print(max(a))
# print(min(a))





# abc=[10,20,30,40,50,60]
# pqr=[50,10,80,90]
# xyz=set(abc).intersection(pqr)
# print(xyz)

# list=[1,2,3,4,5,6,7,8,9,10]
# list1=[]
# for i in list:
#     if i%2==0:
#         list1.append(i)
# print(list1)

# a=(1,2,3,4)
# # print(a*3)
# for i in a:
#     print(i)

# b=(1,2,3,4,3)
# print(b.count(3))
# print(b.index(4))

a=set(["sunday","monday","tuesday","wednesday","wednesday","thursday"])
print(a)
print(type(a))
for i in a:
    print(i)


a=set([1,2,3,4])
a.add(5)
print(a)


w={1,2,3,4,5}
w.add(6)
print(w)
for i in w:
    print(i)



a=10,5,11
c =sorted(a)
print(c)




list=[]
n=int(input("enter the range : "))
for i in range(n):
    a=int (input(f"enter the elements  {i+1}:"))
    list.append(a)
while True:
    s = int(input("enter the range of largest number : "))
    if s>n:
        break
    else:
        q=sorted(list,reverse=True)[:s]
        print(f"The {s} largest numbers are: {q}")

