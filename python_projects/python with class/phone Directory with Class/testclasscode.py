__author__ = 'kalyani'
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

class ElectricCar(Car):
    def __init__(self,model,color,mpg):
        self.battery_type = battery_type

    def display_car(self):
        "this is a %s model %s color %d mpg",
        self.model,self.color,self,mpg
        return super(EletricCar,self).init_(model,color,mpg)


    def drive_car(self):
        self.condition = 'used'
        print self.condition

my_car = Car("DeLorean", "silver", 88)
ElectricCar = Car
print dir(ElectricCar)
my_car.drive_car()