def combinations(amt):
    denominations=[2000,500,200,100,50,20,10,5,2,1]
    if amt<1:
        return
    combi={}
    for d in denominations:
        if amt//d>0:
            combi[d]=amt//d
            amt%=d
    print(combi)
