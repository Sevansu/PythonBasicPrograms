def lcm_find():                      
    my_list=[]                         #List to store number
    mul=1                              #Local variable
    N=int(input("Enter how many number of input"))    
    for i in range(N):
        my_list.append(abs(int(input("Enter {} number".format(i+1)))))  #Appending list with absolute number of input
    if 0 in my_list:                                                    #Check for 0 ,if list contain 0 then return
        print("\nRemove 0 from your input .")
        return
    while True:
        n=mul*max(my_list)             #multiply local variable mul with largest element of list
        count=0
        for i in range(len(my_list)):  #start dividing largest number with each element in the list
            if(n%my_list[i]==0):       # and increament the count
                count+=1
        if(count==len(my_list)):       #if count is equal to length of list,i.e all elements divides the max number 
            print("LCM is:=",n)       # so print LCM and break the loop
            break
        mul+=1   
