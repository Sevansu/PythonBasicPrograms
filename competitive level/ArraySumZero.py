def zeroSumSubset(*L):
    arr=sorted(L)
    for i in range(len(arr)-2):
        left,right=i+1,len(arr)-1
        while right>left:
            sum_of_three=arr[right]+arr[left]+arr[i]
            if sum_of_three==0:
                return True
            elif sum_of_three>0:
                right-=1
            elif sum_of_three<0:
                left+=1
    return False
