__author__ = 'kalyani'
#import test


class Contact():

    """create a phone directory using class having first_name ,last_name and phone_number as inputs"""
    def __init__(self, first_name, last_name, number):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.address = ''
        self.zipcode = 0

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

d = Contact('kk', 'll', 1234)
t = Contact('gg', 'hh', 332)

class Directory():

    """this is a directory that stores Contact instances."""

    def __init__(self):
        self.contact_dict = {}

    #Check to see the User wants to continue the program or not

    def response(self):
        response = raw_input("continue 'y' for yes or not for 'n':").lower()
        if response == 'y':
            self.intentions()
        else:
            exit()


    #Phone_directory menu options

    def intentions(self):
        intentions = input("Enter\n "
                         "1-- for add_entry>>\n "
                         "2-- for edit>>\n "
                         "3-- for find>>\n "
                         "4-- for delete>>")
        if intentions == 1:
            self.add_entry()
        if intentions == 2:
            self.edit_number()
        if intentions == 3:
            self.find_entry()
        if intentions == 4:
            self.remove_entry()

        self.response()


    #Enter a new_data into a Phone_book

    def add_entry(self):
        first_name = raw_input('first name please: ')
        last_name = raw_input('last name please: ')
        phone_number = input('phone number please: ')
        new_contact = Contact(first_name, last_name, phone_number)
        self.contact_dict[new_contact.first_name] = new_contact
        print(self.contact_dict.keys())
        for i in self.contact_dict.values():
            print '{} {} {} '.format(i.first_name, i.last_name, i.number)
        #self.response()
        return
    #Edit the Phone-Book

    def edit_number(self):
        self.user_prompt = raw_input("Enter the name of the phone holder:")
        self.changed_number = input("enter the number to change")

        self.contact_dict[self.user_prompt].number = self.changed_number
        #print(self.contact_dict[self.user_prompt].number)
        print '{} {}'.format(self.user_prompt, self.changed_number)
        #print(self.contact_dict)
        #self.response()

    #search for an entry

    def find_entry(self):

        self.search_item = raw_input("Enter the key to be searched:")

        if self.search_item in self.contact_dict.keys():
        #if self.search_item in self.contact_dict.values():
            print self.contact_dict.__getitem__(self.search_item)
            print 'True'
        else:
            print 'False'
            print "you are not in the directory"
        #self.response()

    #delete an entry

    def remove_entry(self):
        key = raw_input("Enter the Key to be deleted:")
        del self.contact_dict[key]
        for i in self.contact_dict.values():
            print '{} {} {} '.format(i.first_name, i.last_name, i.number)
        #print(self.contact_dict)
        #self.response()

if __name__ == '__main__':
    c = Directory()
    c.intentions()


#response()




