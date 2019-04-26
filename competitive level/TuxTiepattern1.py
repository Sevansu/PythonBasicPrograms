try:
  n=abs(int(input("Enter number of lines:")))
  if n&1:
    for i in range(1,n+1):
      for j in range(1,n+1):
        print([' ','*'][(j<=i or j>n-i if i<=(n+1)/2 else j<=n-i+1 or j>=i) and (i&1)==(j&1)],end=' ')
      print('')
  else:print("Invalid input. Input must be an odd number")
except:print("Invalid input. Input must be an odd number")
