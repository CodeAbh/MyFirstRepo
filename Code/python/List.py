# l=[10,20,30,40]
# print(type(l))
# print(l)


# l=list(range(1,10))
# print(l)

# l2=list(range(8,81,8))
# print(l2)

# s='Abhinay'
# l3=list(s)
# print(l3)

# l=eval(input('enter list: '))
# print(type(l))
# print(l)

# l=list(input('enter list: '))
# print(type(l))
# print(l)


# l=[10,20,30,30.5]
# print(l)
# for ele in l:
#     print(ele)

# n=len(l)
# print(n) 
# i=1
# while i<=n:
#     print(l[i-1])
#     i=i+1


# l=[10,20,10.5]
# x=0
# n=len(l)
# for ele in l:
#     print("{} present at {} and {} index".format(ele,x,x-n))
#     x=x+1

# l=[10,20,10.5]
# x=0
# n=len(l)
# while x<n:
#     print("{} present at {} and {} index".format(l[x],x,x-n))
#     x=x+1


# st='1050'
# x=eval(st)
# y=list(st)
# print(x)
# print(y)
# print(type(x))
# print(type(y))

# l=[10,20,10,20.5,10,10,10,10]
# print(l.count(10))
# print(l.count(20))
# x=l.count(30)
# print(x)


# l=[10,20,10,20.5,10]
# print(l.index(10))
# print(l.index(10))
# print(l.index(20))
# print(l.index(20.5))
# x=l.index(30)
# print(x)

# l=[10,20,10,20.5,10]
# print(l.index(10,1,6))
# print(l.index(20,2))
# x=l.index(30)
# print(x)


# l=[10,20,10.5]
# print(l)
# l.append('csd')
# print(l)


# n1=int(input("enter first number: "))
# n2=int(input("enter second number: "))
# result=[]
# for ele in range(n1,n2+1):
#     if ele%2==0:
#       result.append(ele)

# print(result)


# l=[10,20,10.5]
# print(l)
# l.insert(1,30)
# print(l)
# l.insert(10,40)
# print(l)
# l.insert(4,50)
# print(l)

# l1=[20,30,'abc','pqr']
# l2=['csd','aks','pqr']
# print(l1)
# l1.extend(l2)
# print(l1)


emp=['abc','pqr','xyz','lmn']
new_emp=['abc1','pqr1','xyz1','lmn1']
print(emp)
for ele in new_emp:
    emp.extend(ele)

print(emp)