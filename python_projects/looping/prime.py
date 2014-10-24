c=0
i=1
input=input("Enter the number to check for prime or not:")

while i <= input:
    if input%i == 0:
       c+=1
       print c
       print i


