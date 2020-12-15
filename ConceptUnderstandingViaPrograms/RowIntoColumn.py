input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
print(dimensions)
rowNum=dimensions[0]
print(rowNum)
colNum=dimensions[1]
print(colNum)
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]#this will print list of 0's of size row*col 
print(multilist)

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print(multilist)
