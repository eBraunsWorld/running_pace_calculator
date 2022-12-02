km = float(input("How many kilometers?\n"))

#Takes one variable to convert input kilometers into miles with only two decimal points.
def km_to_miles(distance): 
    miles = km / 1.609
    miles = round(miles, 2)
    return miles
#Implement below code if you're only interested in the conversion and not running performance.
#print(km, "kilometers is the same as", km_to_miles(km), "miles.")