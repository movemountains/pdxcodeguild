__author__ = 'kalyani'
__author__ = 'kalyani'
#import test


class Contact():

    """a phone directory using class"""
    def __init__(self, first_name, last_name, number):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.address = ''
        self.zipcode = 0

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name, self.number)

d = Contact('kk', 'll', 1234)
t = Contact('gg', 'hh', 332)

class Directory():

    """this is a directory that stores Contact instances."""

    def __init__(self):
        self.contact_dict = {'first_name':' ', 'last_name':' ','phone_number':0}

    #Check to see the User wants to continue the program or not

    def response(self):
        response = raw_input("continue 'y' or not 'n':").lower()
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
        self.first_name = raw_input('first name please: ')
        self.last_name = raw_input('last name please: ')
        self.phone_number = input('phone number please: ')
        self.new_contact = Contact(self.contact_dict.first_name, self.contact_dict.last_name, self.contact_dict.phone_number)
        self.contact_dict[self.first_name] = self.new_contact
        print self.contact_dict
        #print(self.contact_dict.keys())
        #for value in self.contact_dict.values():
        #print '{} {} {} '.format(self.first_name, self.last_name, self.phone_number)
        #self.response()
        return
    #Edit the Phone-Book

    def edit_number(self):
        print
        self.ur_change = input("""Enter
                         1.for first_name>>
                         2 for last_name>>
                         3 for phone_number>>""")

        if self.ur_change == 1:
            self.first_name = raw_input("Enter the first_name of the phone holder>>")
            self.changed_first_name = raw_input("enter the name to change>>")
            #print self.contact_dict.keys(0)
            #print self.contact_dict.keys(1)
            #print self.contact_dict.keys(2)
            #self.contact_dict.keys(0) = self.contact_dict[self.changed_first_name]
            self.contact_dict.__setitem__(self.first_name, self.changed_first_name)
            print self.contact_dict

        if self.ur_change == 2:
            self.lastname= raw_input("Enter the last_name you want to change>>")
            self.changed_last_name = raw_input("Enter the last_namer>>")
            self.contact_dict.__setitem__([self.lastname][0], self.changed_last_name)
            print self.contact_dict
        if self.ur_change == 3:
            self.phonenumber =input("Enter the number you want to Change>>")
            self.new_number = input("Enter the new number>>")
            self.contact_dict.__setitem__([self.phonenumber][0], self.new_number)
            print self.contact_dict
        #print(self.contact_dict[self.user_prompt].number)
        #print '{} {}'.format(self.user_prompt, self.changed_number)
        #print(self.contact_dict)
        #self.response()

    #search for an entry

    def find_entry(self):

        self.search_item = raw_input("Enter the key to be searched:")
        #if self.search_item in self.contact_dict.keys():
        if self.contact_dict.has_key(self.search_item):
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
        # for i in self.contact_dict.values():
        #     print '{} {} {} '.format(i.first_name, i.last_name, i.number)
        print(self.contact_dict)
        #self.response()

if __name__ == '__main__':
    c = Directory()
    c.intentions()


#response()




