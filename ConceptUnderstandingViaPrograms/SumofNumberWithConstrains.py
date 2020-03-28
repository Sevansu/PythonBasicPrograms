'''Write a module that gets a sequence of integers from the user, and, when complete, displays a report
showing the sum, number of integers entered and an average.
Here are some details:
- The number of integers entered is variable. The user enters a carriage return(\r) (no data entry) to
signify the end of entry.
- If the user enters anything other than an integer or empty value (carriage return only), a
message must be displayed indicating “Invalid entry” and the user must re-enter a valid value.
- After each entry, the user should see a message to enter an integer.Note:-To get output in end type \r'''

y=[]
sum=0
while True:
    value = input('Enter the number : ')
    if (value.isdigit()):
        y.append(int(value))
    elif (value != None):
        for i in y:
            sum += i
            avg = sum / len(y)
        print ("sum of given number is ",sum,"And Number of integer entered is ",len(y),"And average number of given number is ", avg)
        break
    else:
        print("Warning !!! Enter only interger number")
        break

        

    


