
import random
secret = random.randint(1,10)
#print secret
counter=0

def response():
    response = raw_input("Enter 'y' or 'n':").upper()
    if response() == 'y':
	print "continue"
        myfunction()
    else:
        print "Thanks for Playing"
        exit() 

 
def myfunction():
    value = input("Enter a number:")
    return value

#guess=myfunction()

while counter < 5:    
    guess = myfunction()
    print guess
    if guess > secret:
        print "too high"
        counter += 1
    if guess < secret:
        print "too low"
        counter += 1
    if guess == secret:
       print "u got the secret" 
       break

response()
