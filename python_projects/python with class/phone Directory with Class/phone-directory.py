__author__ = 'kalyani'
#test record

phone_book = {'jones': ['tom', '0987987']}
#to-do: clean up the prompt format (tabbing, e.g.)
#to-do error handling

intention = input ('what would you like to do? Type 1 for search, 2 for add, 3 for remove, or 4 for exit:')
'1. search'
'2. add'
'3. remove'
'4. exit'

#to-do handle user input errors
if intention == 1:
    who_are_you_looking_for = raw_input('search by last name :').lower()
    print(phone_book[who_are_you_looking_for])

#get new data from the User
if intention == 2:
    first_name=raw_input("Enter ur first_name:")
    last_name=raw_input("Enter ur Last_name:")
    phone_number=raw_input("Enter ur Phone_number:")
    new_entry = {first_name: [last_name, phone_number]}
    phone_book.update(new_entry)
    print phone_book

#error handling

if intention == 3:
    who_do_you_want_to_remove = raw_input ('search by last name').lower()
    removed_person= phone_book.pop(who_do_you_want_to_remove)
    print(removed_person)
    print phone_book
#Quit the program


if intention == 4:
    print ("control_c to exit")

