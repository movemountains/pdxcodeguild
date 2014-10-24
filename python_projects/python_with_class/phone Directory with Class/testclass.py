__author__ = 'kalyani'
class Animal():
    is_alive = True
    def __init__(self, name, number, is_good):
        self.name = name
        self.number = number
        self.is_good = is_good

kk = Animal('panda', 12, True)
ll = Animal('Monkey', 10, False)

print kk.name, kk.number, kk.is_good, kk.is_alive
print ll.name, ll.number, ll.is_good, ll.is_alive

class Python():
    name = "Tutorials"
    mode = "difficult"

print Python.name
print Python.mode

Python.name ="Classes"
print Python.name

class Cooking():
    object1 = "chicken"
    object2 = "Fish"

    def __init__(self,name):
        self.name = name
kk = Cooking('kadja')

print Cooking.object1
print Cooking.object2
print kk.name


class Phone_book(object):
    def __init__(self, name):
        self.name = name

    def hi(self):
        print "say Hello", Phone_book.name

case = Phone_book("leela")
print case.name


class Directory(object):
    def __init__(self,name,number):
        self.name = name
        self.number = number



    def add_data(self, Directory):
        name = raw_input('enter the name')
        number = input("enter the number")
        return name, number

data1 = Directory('ll',1212)

print data1.__dict__
print data1.__dict__['name']
print data1.__dict__['number']

data2 = data1.add_data()
print data2.__dict__






