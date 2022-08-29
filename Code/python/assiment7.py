n=5
for i in range(n,0,-1):
    for j in range(0,n-i+1):
        print(" ",end='')
    for k in range(0,i-1+1):
        print("* ",end='')
    print()
for i in range(1,n+1):
    for j in range(0,n-i+1):
        print(" ",end='')
    for k in range(0,i-1+1):
        print("* ",end='')
    print()
     