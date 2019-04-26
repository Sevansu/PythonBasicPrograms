def triplet():
    num=int(input("enter no. of triplets : "))
    m=3;
    pri=[[3,4,5,12]];                                                           # primitive pythagorean triplet will be in pri=[]
    norm=[];                                                                      # elements obtained from primitive pythagorean triplet will store in norm
    p=0;                                                                             # no. of elements in norm []
    counter=[2];                                                                                                        
    count=1;
    flag=1
    
    while count<=num:
        n=m%2+1;                                                                # value of n will be odd or even for m even or odd respectively
        while n<m and count<=num:
            a=m**2-n**2;
            b=2*m*n;
            c=m**2+n**2;
            for i in range(0,len(pri)):                                     # this loop checks for non primitive triplets
                if ((counter[i]*(pri[i][3])) < (a+b+c)) :
                    d=counter[i]*pri[i][0]
                    e=counter[i]*pri[i][1]
                    f=counter[i]*pri[i][2]
                    s=d+e+f
                    for k in norm:
                        if k==([d,e,f,s]):
                            flag=0
                            break
                    if flag:
                        norm.append([])
                        for j in range(0,3):
                            norm[p].append(counter[i]*pri[i][j])
                        norm[p].append(sum(norm[p]))
                        p+=1;
                        counter[i]+=1;
                        count+=1;
                        if count>=num or (counter[i]*pri[i][3] > (a+b+c)) :
                            break
    
            count+=1;
            pri.append([a,b,c,(a+b+c)])
            counter.append(2)
            n+=2;
        m+=1;
    for i in norm:
        pri.append(i)
 
    pri.sort(key=lambda x : x[3])                                   # this function will sort according to sum of triplet in ascending order
    
    for i in range(0,num):
        print(f"Triplet  {i+1} : {pri[i]}  sum={pri[i][3]}")
triplet()﻿
