top=-1;
start=0;
array=[2]
def prime_generator(total):
    global top,start,array;
    if start==0:                                         # start is a counter which counts for number of times prime_generator function gets called
        top=-1                                             # top determines the next element to be printed
        start=total+1
        count=1;                                         # count is a counter that determines that desired number of prime numbers get stored 
        num=3;
        while(count<total):
            flag=1                                          # flag is a counter to check whether a number is prime or not
            for div in  range(2,num//2):     # this for loop  runs only 1/4 times of number because number gets incremented by 2 
                                                                 # everytime & it ranges to half of number
                if num%div==0:
                    flag=0;
                    break;
            if flag:
                array.append(num)
                count+=1
            num+=2                                       # num gets incremented by 2
    start-=1
    if start>0:
        top+=1
        return(array[top])
    else:
        return 0﻿
