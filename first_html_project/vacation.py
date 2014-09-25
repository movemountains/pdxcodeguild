__author__ = 'kalyani'
__author__ = 'kalyani'
def hotel_cost(nights):
    return 120 * nights


def plane_ride_cost(city):
    if city == 'Charlotte':
        return 183
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburgh':
        return 222
    elif city == 'Los Angeles':
        return 475
    else:
        exit()
def rental_car_cost(days):
    car_cost=40*days

    if days >= 7:
        discount = 50
        car_cost -= discount

    elif days >= 3:
        discount = 20
        car_cost -= discount

    else:
        return car_cost



def trip_cost(city,days):
    print hotel_cost(days)
    print rental_car_cost(days)
    print plane_ride_cost(city)
    return hotel_cost(days)+rental_car_cost(days)+plane_ride_cost(city)

if __name__ == '__main__':
    place = 'Tampa'
    stayed_days= 4
    #place = raw_input("Enter a city Los Angeles or Tampa or Pittsburgh or Charlotte:")
    #stayed_days = input("Enter a no.of nights in "
                    #"Hotel (From 1 to 7):")
    print trip_cost(place,stayed_days)
