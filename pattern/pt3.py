n=int(input("Enter the number of row:"))

for i in range(n,0,-1):
    for j in range(i,0,-1):
        print('*',end='')
    print()


for i in range(0,n):
    for j in range(0,n):
        if i==0 or j==n-1 or i==j:
            print('*',end='')
        else:
            print(end=" ")
    print()
