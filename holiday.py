#This is a holiday planned for a single user living in the city of Leeds, England, UK. 
#This user will be buying tickets for a single holiday.
#This user will be departing from Leeds Bradford Airport.
#This programme uses a combination of user-defined functions, conditional statements, list and user inputs 
#to calculate the total cost of the holiday.

#listing potential holiday destinations:
def city_flight_options(): 
    print("Destination options: ")
    print("Amsterdam")
    print("Barcelona")
    print("Dublin")
    print("Geneva")

#Obtaining user inputs for destination city, nights spent in a hotel, and days needed for car rental:  
print("This programme will compile the cost of your holiday based on your destination city.")

city_flight_options()
city_flight = input("Please choose your destination city: ")
num_nights = int(input("For how many nights will you be staying at a hotel? "))
rental_days = int(input("Please enter the number of days for which you'll be hiring a car: "))

print(f"Your chosen city is {city_flight}.")

#Calculating car expenses using car_rental_daily and rental_days as arguments:
car_rental_daily = 25 #base daily car rental rate
def car_rental(rental_days, car_rental_daily): 
    total = rental_days * car_rental_daily
    return(total)

#Calculating hotel expenses using num_nights and hotel_rate as arguments:
hotel_rate = 150 #base daily rate for a hotel stay
def hotel_cost(num_nights, hotel_rate):
    total = num_nights * hotel_rate
    return(total)

#Calculating flight expenses using a flight price list and city_flight as arguments: 
flight_price = [173, 200, 375, 430] #list of flight-prices
def plane_cost(city_flight): 
    if city_flight == "Amsterdam": 
        return flight_price[0]
    elif city_flight == "Barcelona": 
        return flight_price[1]
    elif  city_flight == "Dublin": 
        return flight_price[2]
    elif city_flight == "Geneva":
        return flight_price[3]
    else: 
        print("Your selection was not valid.")
        
#Calculating subtotals by calling on the plane_cost, hotel_cost, and car_rental functions:

print(f"Your flight expenses come to: £{plane_cost(city_flight)}.")

print(f"The total cost of your hotel expenses is: £{hotel_cost(num_nights, hotel_rate)}.")

print(f"The total cost of your car expenses is: £{car_rental(rental_days, car_rental_daily)}. ")

#Calculating total expenses drawing on above user-defined arguments as arguments:
    
def holiday_cost(car_rental, hotel_cost, plane_cost): 
    total = car_rental + hotel_cost + plane_cost
    return(total)


print(f"The total cost of your holiday is: £{holiday_cost(car_rental(rental_days, car_rental_daily), hotel_cost(num_nights, hotel_rate), plane_cost(city_flight))}.")
