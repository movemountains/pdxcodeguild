__author__ = 'kalyani'

class Student:

    """ A Program using Class to compute avg and total """
    # Initialise a Student counter
    student_counter = 0
    total = 0  #Initialise a total as 0
    def __init__ (self, name, mark1, mark2):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.total = 0
        Student.student_counter += 1

    def compute_total(self):
        Student.total = 0
        Student.total = Student.total + self.mark1 + self.mark2
        #print Student.total
        return Student.total


kk = Student('kk', 78, 67)
print kk.compute_total()
mm = Student('mm', 90, 95)
print mm.compute_total()
print(kk.__doc__)
#kk = Student('kk', 78, 67, total1)
#mm = Student('mm', 90, 95, total2)
print (kk.name, kk.mark1, kk.mark2)
print (mm.name, mm.mark1, mm.mark2)
print 'The Class name is ', Student.__name__
print 'The Doc string is ', Student.__doc__
print 'The module is ', Student.__module__
print 'The counter is ', Student.student_counter