import sys

def canArrangeWord(num,strList):
    if num==len(strList):
        for strList in range(len(strList)):
            for i in range(3):
                s=str(strList)
                p=str(strList+i)
                if (s[(strList)-1]==p[0]):
                    print("1")
                else:
                    print("0")
    else:
        print("Something went wrong")
        sys.exit()

num=int(input("num="))
strL=input("strList=")
strList=list(strL.split(" "))
canArrangeWord(num,strList)




                
                

