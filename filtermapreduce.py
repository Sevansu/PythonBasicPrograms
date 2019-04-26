from functools import reduce

#use of filter and lambda

num=[3,2,6,8,4,9,7,5]

even=list(filter(lambda n:n%2==0,num))

print(even)


#if you have to change value then use map
#use of map and reduce


lst=[1,2,3,4,5,6,7,8,9,10,11,12,13]

odd=list(filter(lambda n:n%2!=0,lst))#filter

print(odd)

double=list(map(lambda n:n*2,odd))#map

print(double)

sum=reduce(lambda a,b:a+b,double)

print(sum)


