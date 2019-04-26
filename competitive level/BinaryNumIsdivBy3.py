def divide_by_three(str):
    str=str[::-1]
    oddPosition,countodd,counteven=True,0,0
    for i in str:
        if oddPosition:
            if i=="1":
                countodd+=1
            oddPosition=False
        else:
            if i=="1":
                counteven+=1
            oddPosition=True
    return True if abs(countodd-counteven)%3==0 else False            
