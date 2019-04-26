def spiral_matrix(N):
    try: 
        if N<=0:
            return
##########initialising a matrix and variables##################
        import math
        direction=1
        mat_range=math.sqrt(N)
        mat_range=math.ceil(mat_range)+2
        L,R,T,B=map(int,[(mat_range//2)-1]*4)   #these four variable denote direction(left,right,top and bouttom)
        mat=[['' for i in range(mat_range)]for j in range(mat_range)]   #matrix
        mat[R][L]=1                                                     #initialise center of matrix with 1
        count=2                                                         #starting count from 2
##################### apending the matrix based on direction of control flow ###############
        for i in range(N):

            if(direction==0):
                for i in range(T,B):
                    if count<=N:
                        mat[i+1][L]=count
                        count+=1    
                R+=1

            elif(direction==1):
                for i in range(L,R+1):
                    if count<=N:
                        mat[B][i+1]=count
                        count+=1
                T-=1

            elif(direction==2):
                for i in range(B,T,-1):
                    if count<=N:
                        mat[i-1][R+1]=count
                        count+=1
                L-=1

            else:                      
                for i in range(R,L-1,-1):
                    if count<=N:
                        mat[T][i]=count
                        count+=1
                B+=1     
            direction=(direction+1)%4    
############# Taking transpose of matrix and printing column-wise#######

        mat=[list(x) for x in zip(*mat)]           
        for j in range(mat_range):
            for line in mat:
                print('{:<8}'.format(line[j]),end='')    
            print("\n")
            
    except:
        print("Given input is not allowed")

number=int(input("Enter some non-zero positive number:::::>"))
spiral_matrix(number)
