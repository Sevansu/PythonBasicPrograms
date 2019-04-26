import math

arr = []
def prime_gon(num):
    if arr:
        return arr.pop(0)
    else:
        for i in range(2,int(1e9)):
            b = True
            for j in range(2,int(math.sqrt(i)+1)):
                if(i%j==0):
                    b = False
                    break
            if(b):
                if(len(arr)==num):
                    arr.append(0)
                    break
                else:
                    arr.append(i)
        return arr.pop(0)

"""if _name_ == '__main__':
    print(prime_gon(3))
    print(prime_gon(1))
    print(prime_gon(1))
    print(prime_gon(2))
    print(prime_gon(2))
    print(prime_gon(3))
    print(prime_gon(3))
    print(prime_gon(3))"""
