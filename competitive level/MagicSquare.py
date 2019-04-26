num = int(input("Enter your intial number to form magic square of 4x4 \n"))
a,z = num,0
magic_sqr = [[a,a+14,a+13,a+3],[a+11,a+5,a+6,a+8],[a+7,a+9,a+10,a+4],[a+12,a+2,a+1,a+15]]
for z in range(len(magic_sqr)):
    print("%4d  %4d  %4d  %4d" %(magic_sqr[z][0],magic_sqr[z][1],magic_sqr[z][2],magic_sqr[z][3]))
