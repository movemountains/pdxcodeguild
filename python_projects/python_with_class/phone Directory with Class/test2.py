__author__ = 'kalyani'


class Contact():

    """create a phone directory using class with inputs like first_name,last_name,phone_number,address and zipcode"""
    def __init__(self, first_name, last_name, number,address,zipcode):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.address = address
        self.zipcode = zipcode

    # this one returns the dictionary values form the contact instance
    def __str__(self):
        return "{} {} {} {} {} ".format(self.first_name, self.last_name, self.number, self.address, self.zipcode)

d = Contact('kk', 'll', 1234,'first ave', 97004)
t = Contact('gg', 'hh', 332,'main st', 97234)

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
        intentions = input("""Enter
                         1-- for add_entry>>
                         2-- for edit>>
                         3-- for find>
                         4-- for delete>>""")
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
        address = raw_input('address please:')
        zipcode = input('zipcode:')
        new_contact = Contact(first_name, last_name, phone_number, address, zipcode)
        self.contact_dict[new_contact.first_name] = new_contact
        print self.contact_dict[new_contact.first_name]
        print(self.contact_dict.keys())

    # Update the phone book with changes
    def edit_number(self):
        self.user_prompt = raw_input("Enter the name of the phone holder:")
        self.changed_number = input("enter the number to change")

        self.contact_dict[self.user_prompt].number = self.changed_number
        for i in self.contact_dict.values():
            print'{} {} {} {} {} '.format(i.first_name, i.last_name, i.number, i.address, i.zipcode)


    #search for an entry in the Phone_book

    def find_entry(self):
        self.search_item = raw_input("Enter the key to be searched:")
        if self.contact_dict.has_key(self.search_item):
            print self.contact_dict.__getitem__(self.search_item)
            print 'True'
        else:
            print 'False'
            print "you are not in the directory"

    #delete an entry from the phone_book

    def remove_entry(self):
        key = raw_input("Enter the Key to be deleted:")
        del self.contact_dict[key]
        for i in self.contact_dict.values():
            print '{} {} {} {} {}'.format(i.first_name, i.last_name, i.number, i.address, i.zipcode)

if __name__ == '__main__':
    c = Directory()
    c.intentions()





