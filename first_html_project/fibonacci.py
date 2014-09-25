
first_no = 0
second_no = 1
counter = 0
input=input("Enter a number to get fibonacci series:")
while counter < input:
    if counter == 0:
        fibonacci =1
        print fibonacci
        counter+=1
    else:
        fibonacci = first_no + second_no
        print fibonacci
        first_no = second_no
        second_no = fibonacci
        counter += 1

"""
1,1,2,3,5...
"""




