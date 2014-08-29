phbook=[]

fname=raw_input("fname:")#get Firstname
lname=raw_input("lname:")#get Lastname
phno=raw_input("phno:")#get Phone number
add=raw_input("add:")# get  address
phbook.extend([fname,lname,phno,add])#add all the values to phonebook
print phbook
xx=raw_input("enter fname or lname or phno or address to be added to list:")
phbook.append(xx)#new item is added to phonebook
print phbook
search=raw_input("Enter the index of the list to be deleted in integer:")
rm = int(search)
print phbook.pop(rm)#delete the item in the list by index
print phbook
data=raw_input("Enter the item to be removed from the list:")
print phbook.remove(data)#delete the item in the list by values
print phbook
rep=raw_input("enter any data to check for repeatation in list:")
print phbook.count(rep)
print phbook



