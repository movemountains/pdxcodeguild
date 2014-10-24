__author__ = 'kalyani'

class Phone_dir(object):
    """ Creates a phone directory with class """
    customer_count = 0
    def __init__(self, name, number, address,zipcode,email):
        self.name = name
        self.number = number
        self.address = address
        self.zipcode = zipcode
        self.email = email
        Phone_dir.customer_count += 1

    def display_status(self):
        print "Phone Directory"
        print "***************"
        print 'Name :', self.name
        print 'phone-number:', self.number
        print 'Address:', self.address
        print 'Zipcode:', self.zipcode
        print 'email:', self.email
        print




kala = Phone_dir('kala', 12345, 'ss st', 98762, 'ss.gmail.com')
mala = Phone_dir('Mala',34234, 'll st', 90012, 'mm.gmail.com')
kala.display_status()
mala.display_status()
print Phone_dir.__doc__








