initialize = 4
counter = 1

input=input("get a number to check for prime:")
while initialize <= input:
    if initialize % 2  == 0 or initialize % 3 == 0 or initialize % 5 == 0 or initialize % 7 == 0:
        #print(str(initialize)+" is not a prime number")
        initialize += 1
    else:
        print(str(initialize)+" is a prime number")
        initialize += 1
