def hotel_cost(num_nights, star_rating) : # function created with the parentheses num_nights and star_rating
    try: 
        if star_rating == 5 : # each star_rating will determine the cost of the hotel
            y = num_nights * 150
            return y

        elif star_rating == 4 : 
            y = num_nights * 120
            return y

        elif star_rating == 3 :
            y = num_nights * 90
            return y

        elif star_rating == 2 :
            y = num_nights * 70
            return y

        elif star_rating == 1 :
            y = num_nights * 50
            return y
        
    except ValueError:
        print("Unrecognized option.")
        hotel_cost(num_nights, star_rating)   #if wrong values entered, user needs to input again

    
def plane_cost(city_flight):   # functions created for flight cost of each city. Each city assigned to a cost
    if city_flight == "PARIS":
        y = 77
        return y
    
    elif city_flight == "CANCUN":
        y = 338
        return y
    
    elif city_flight == "NEW YORK" :
        y = 249
        return y
    
    elif city_flight == "TOKOYO":
        y = 497
        return y




def car_rental(rental_days, per_day = 25) : #function created to calculate the total rental with a per day cost
    y = rental_days * per_day
    return y


def holiday_cost():
    y = hotel_cost(num_nights, star_rating) + plane_cost(city_flight) + car_rental(rental_days, per_day = 25) # total costs calculated using nested function
    return y

def destinations() : #destination function for each city choice
    print("")
    print("Please select from the following holiday destinations:")
    print("Paris")
    print("Cancun")
    print("New York")
    print("Tokoyo")
    print("Exit")
    print("")

def calculations() : #calculation function for calculate individual costs or total
    print("")
    print("Please select what holiday expense you wish to calculate:")
    print("F = Flight cost")
    print("H = Hotel cost")
    print("C = Car rental cost")
    print("T = Total holiday cost")
    print("R = Return to main menu")
    print("")

city_flight = "" #empty variable to assign in while loop 


print("")
print("""This program will calculate your the costs of your:
- Hotel stay
- Plane trip
- Car rental and
- Total for the holiday""")
destinations()

while city_flight != "Exit":
        city_flight = input("Please enter your chosen holiday destination: ").upper()

        while city_flight in ("PARIS" , "TOKOYO", "CANCUN", "NEW YORK") : #while loop which will check if input is one of the city destinations
            calculations()
            
            calculate = input("Please enter what you wish to calculate: ").upper() #user asked to select which cost to calculate
            
            if calculate == "F" :
                
                if city_flight == "PARIS": #plane_cost function used to calculate flight cost and f string printed 
                    print("")
                    print(f"The cost of your flight in {city_flight} is £{plane_cost(city_flight)}")

                elif city_flight == "CANCUN":
                    print("")
                    print(f"The cost of your flight in {city_flight} is £{plane_cost(city_flight)}")

                elif city_flight == "TOKOYO" :
                    print("")
                    print(f"The cost of your flight in {city_flight} is £{plane_cost(city_flight)}")

                elif city_flight == "NEW YORK" :
                    print("")
                    print(f"The cost of your flight in {city_flight} is £{plane_cost(city_flight)}")

            elif calculate == "H" :

                while True:
                    try:
                        num_nights = float(input("Please enter the number of nights you wish to spend: ")) 
                        star_rating = float(input("Please enter the star rating of the hotel you wish to stay at (1 to 5): ")) #input star rating of hotel and number of nights to use the hotel_cost function

                        if star_rating == 1 or 2 or 3 or 4 or 5 :
                            print(f"The cost of your {star_rating} star hotel stay in {city_flight} is £{hotel_cost(num_nights, star_rating)}") #prints f string
                            break
                    
                    except ValueError: 
                        print("You have not entered a valid input!")
                        continue
                    
            
            elif calculate == "C" :
                rental_days = float(input("Please enter the number of days you wish to rent a car: ")) #input the number of days car will be rented and uses car_rental function
                print("")
                print(f"The cost of your car rental for {rental_days} days in {city_flight} is £{car_rental(rental_days, per_day = 25)}") #prints f string

            elif calculate == "T" :
                plane_cost(city_flight)
                star_rating = float(input("Please enter the star rating of the hotel you wish to stay at (1 to 5): ")) #inputs all the necessary info to calculate holiday_cost using function
                num_nights = float(input("Please enter the number of nights you wish to spend: "))
                rental_days = float(input("Please enter the number of days you wish to rent a car: "))

                print("")
                print(f"""The breakdown of your holiday cost to {city_flight}): 

                The cost of your flight is £{plane_cost(city_flight)}.
                The cost of your {star_rating} star hotel stay is £{hotel_cost(num_nights, star_rating)}.
                The cost of your car rental for {rental_days} day is £{car_rental(rental_days, per_day = 25)}.
                
                The cost total cost of your holiday to {city_flight} is £{holiday_cost()}.""") # prints holiday breakdown using f string
    
            elif calculate == "R" :
                destinations() #returns to main menu using destination function
                break

            else:
                print("Unrecognized option.") #wrong input will loop calculations function
    

        if city_flight == "EXIT" : #exits holiday calculator
            print("")
            print("Thank you for your time. Goodbye")
            break


        else: 
            print("")
            print("Unrecognized option.") #wrong input loops destinations function

            


        




   

