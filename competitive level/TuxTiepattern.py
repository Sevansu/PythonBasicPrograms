def pattern_generator():
    n=int(input("Enter Number Of Lines :"))
    if n<=1:
        print("Please give number greter than 1")
    elif n%2==0:
        print("Please Give Odd number only")
    else:
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i<=n//2+2:
                    print("*", end="")if(j<=i and j%2==i%2) or (j>=n-i and j%2==i%2) else print(" ",end="")
                else:
                    print("*", end="") if (j <=n+1-i and j % 2 == i % 2) or (j >= n - (n+1-i) and j % 2 == i % 2) else print(" ", end="")
            print()﻿
