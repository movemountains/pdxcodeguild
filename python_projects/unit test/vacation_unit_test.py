__author__ = 'kalyani'
import unittest
from vacation import hotel_cost
from vacation import rental_car_cost



class vacationTestcase(unittest.TestCase):

    """test for hotel_cost"""


    def test_hotel_cost(self):
        self.assertTrue(hotel_cost(3.5))
        assert isinstance(hotel_cost, int)


    def test_rental_car_cost(self):
        self.assertTrue(rental_car_cost("r"))
        assert isinstance(rental_car_cost, int)

    def plane_ride_cost(city):




if __name__ == '__main__':
    unittest.main()
