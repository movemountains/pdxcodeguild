__author__ = 'kalyani'


#def add_entry(name,number):
def add_entry():
    counter = 0
    phone = {}
    while counter < 3:
        name = raw_input('name:')
        number = input("number:")
        counter += 1
        phone[name]= number
        print phone


name_data = raw_input("enter the name:")

def response():
    response = raw_input("continue press 'yes' or 'y' or press 'no' or 'n' to exit:" ).lower()
    if response == 'yes' or 'y':
        check_entry()
    else:
        exit()

response()

def check_entry():
    if phone.has_key(name_data):
        print phone[number]
    else:
        print"there is no name "

