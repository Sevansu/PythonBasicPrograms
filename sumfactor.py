import sys
number=int(input())
copy=number
lst=[]
if number <= 10**5:
    for i in range(1,number-1):
        if number%i==0:
            lst.append(i)
    if sum(lst)==copy:
        print("1")
    else:
        print("0")
else:
    sys.exit()
