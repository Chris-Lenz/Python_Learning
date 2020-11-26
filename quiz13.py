# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
    km = miles*1.6
    return(km)

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance (my_trip_miles)
print ("the distance in kilometers is: " + str(my_trip_km ))
print (my_trip_km  * 2)

        

