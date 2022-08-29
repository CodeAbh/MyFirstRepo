# f=open("C:/Users/abhinay/Desktop/python/FILES/num.txt","r")


# data=f.readline()
# data1=f.readline()

# print(data,end='')
# print(data1,end='')
# print(f.readline(),end='')



# f=open('C:/Users/abhinay/Desktop/python/FILES/num.txt', 'w')

# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)


# f=open('C:/Users/abhinay/Desktop/python/FILES/num.txt', 'w')
# f.write('csd\n')
# f.write('100\n')
# f.close


# f=open("C:/Users/abhinay/Desktop/python/FILES/num.txt",'a')

# f.write('csd\n')
# f.write('100\n')
# f.write('csd\n')
# f.write('100\n')
# f.close()

l=['Abhinay\n','Kumar\n','Shrivastava\n']
f=open('C:/Users/abhinay/Desktop/python/FILES/num.txt', 'w')
f.writelines(l)

f.close

