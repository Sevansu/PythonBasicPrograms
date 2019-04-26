''' Error 1) compile time error 2) run time error 3)Logical error
   Exception handling for run time error'''

a=5
b=2

try:
    print("Resource(file or database) open")
    print(a/b)
    s=int(input("Enter a number : "))
    print(s)
    
except ZeroDivisionError as e:
    print("Hey,you can not divide number by zero ::::>",e)

except ValueError as e:
    print("Invalid input :::::>",e)
    
finally:
    print("Resource(file or database) close")
    
print("Bye")
