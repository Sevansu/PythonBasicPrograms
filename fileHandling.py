f=open('MyData.txt','r')
print(f.read())
print(f.readline()) #print 1 blank line
print(f.readline()) #print 1 blank line

f1=open('WData.txt','a')
f1.write("data is inserting")
f1.write("data is appending")

f1=open('WData.txt','r') #use rb instead of rto read from image which is in binary format
print(f1.read())
f1=open('WData.txt','w')

for i in f:    '''for the copy of file 2 line of code'''
    f1.write(i)
f1=open('WData.txt','r')
print(f1.read())

