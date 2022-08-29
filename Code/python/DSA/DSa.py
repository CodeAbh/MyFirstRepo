# n=5
# for i in range(1,n+1):
#     print(' '*(n-i),end='')
#     for j in range(1,2*i):
#         if i%2==0:
#             print("-",end='')
#         else:
#             print("*",end='')

#     print()

# for i in range(n-1,0,-1):
#     print(' '*(n-i),end='')
#     for j in range(1,2*i):
#         if i%2==0:
#             print("-",end='')
#         else:
#             print("*",end='')

#     print()


# n=5
# for i in range(1,n+1):
#     print(" "*(i-1),end='')
#     for j in range(1,2*n-2*i+2):
#         if j==1 or j==2*n-2*i:
#             print('*',end='')

#         else:
#             print("-",end='')
#     print()

# n=10
# for i in range(1,n+1):
#     for j in range(1,2*n+1):
#         if j <= n-i+1 or j>=n+i:
#           print("* ",end='')
#         else:
#             print('  ',end='')

#     print()


# for i in range(n,0,-1):
#     for j in range(1,2*n+1):
#         if j <= n-i+1 or j>=n+i:
#           print("* ",end='')
#         else:
#             print('  ',end='')

#     print()



# n=int(input('enter number: '))
# result=1
# for i in range(n,1,-1):
#   result=result*i
# print(result)


# def factorial(n):
#   result=1
#   for i in range(2,n+1):
#     result=result*i

#   return result



# def combination(n,r):
#     result=factorial(n)//(factorial(r)*factorial(n-r))
#     return result



# def Extra_element(A,B):
#     for i in range(0,len(A)):
#       if A[i]!=B[i]:
#         return i

# A=[]
# B=[]
# result=Extra_element(A,B)
# print(result)



def Extra_element(A,B):
    for i in range(0,len(A)):
      if i>len(B)-1 or A[i]!=B[i]:
        return i

A=[3,5,7,9]
B=[3,5,7]
result=Extra_element(A,B)
print(result)
    














