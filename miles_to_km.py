miles = float(input("How many miles?\n"))

def miles_to_km(distance): #Takes input miles and converts it to kilometers.
    km = miles * 1.609
    km = round(km, 2)
    return km
#Implement below code if you're only interested in the converter.
#print(miles, 'miles is the same as', miles_to_km(miles), 'kilometers.')