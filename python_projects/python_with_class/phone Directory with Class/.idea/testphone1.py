__author__ = 'kalyani'
#import test


class Contact():


    """a phone directory using class"""
    def newclass(**kwargs):

        def set(key,value):
            kwargs[key]= value
        return kwargs
    # def __init__(self, first_name, last_name, number):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.number = number
    #     self.address = ''
    #     self.zipcode = 0

d = newclass(
    first_name ='kk',
    last_name ='ll',
    phone_number =1234)
#t = Contact('gg', 'hh', 332)

class Directory():

    """this is a directory that stores Contact instances."""

    def __init__(self):
        self.contact_dict = {}



    def add_entry(self):
        first_name = raw_input('first name please: ')
        last_name = raw_input('last name please: ')
        phone_number = input('phone number please: ')
        new_contact = Contact(first_name, last_name, phone_number)
        self.contact_dict[new_contact.first_name] = new_contact
        print self.contact_dict
        print



    def edit_number(self):
        self.user_prompt = raw_input("Enter the name of the phone holder:")
        self.change = input("enter the number to change")
        self.contact_dict[self.user_prompt].number = self.change
        print(self.contact_dict[self.user_prompt].number)


    #search for an entry
    def find_entry(self):
        search_item = raw_input("Enter the key to be searched:")
        if search_item in self.contact_dict.keys():
            print 'True'
        else:
            print 'False'

    #delete an entry
    def remove_entry(self):
        key = raw_input("Enter the Key to be deleted:")
        del self.contact_dict[key]
        print(self.contact_dict)



k = d()
k.add_entry()
k.edit_number()
k.find_entry()
k.remove_entry()
#print(k.__dict__['contact_dict'] .__dict__)

print
print "The Class name is ", Contact.__name__
print "The Doc string is ", Contact.__doc__
print " The module is   ",Contact.__module__
print Contact






