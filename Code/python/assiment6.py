n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for k in range(1,i+1):
        print("*",end="")
    print()
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for k in range(1,i+1):
        print("*",end="")
    print()