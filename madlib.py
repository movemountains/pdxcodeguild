"""This is name and she goes to place and learning program with no other 
students.learning program is fun and place is a good place to start.
she goes in transportation and it takes really time hour to reach the
place."""

#print "Enter ur name:"
#print "enter the strings in quotes please"
name =raw_input("enter ur name :")
print name
place=raw_input("Enter the Place:")
print place
program=raw_input("enter the Programming Language:")
print program
noof_students=raw_input("Enter the no.of Students:")
print noof_students
emotion=raw_input("How is the Learning:")
print emotion
transport=raw_input("How did you come trimet or car:")
print transport
time=raw_input("Enter the time to travel:")
print time

print """This is %r and she goes to %r and learning program with
%r other students.learning program is %r and %r is a good place to start.
she goes in %r and it takes really %r hour to reach the 
place. """  % (name.upper(),place.upper(),noof_students,emotion.upper(),
place.upper(),transport.upper(),time)

