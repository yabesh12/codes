N = 17

for i in range (1,N+1):
    if (i == N):
        print(i,end="")
    elif (i % 3==0) and (i % 5 ==0):
        print ("FizzBuzz,", end="")
    elif (i%3==0):
        print ("Fizz,",end="")
    elif (i%5==0):
        print ("Buzz,",end="")
    else:
        print(i, end=",")   
    
        