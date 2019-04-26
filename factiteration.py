number=int(input("Enter the number:"))
result=1
for i in range(number,0,-1):   # here -1 is step from n to 0
    result=result*i
print("Factorial of ",number," is ",result)
