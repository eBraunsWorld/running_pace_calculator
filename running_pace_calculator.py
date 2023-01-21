print("Welcome to the Running Pace Calculator made by Erik Braun \n(@eBraunsWorld on GitHub; email: e.braun308@gmail.com).\n")

#Gather preferred units for user's run.
while True:
    try:
        unit = input("Enter units: \n 1 - miles\n 2 - kilometers\n")
        if unit == "1":
            unit = "mi"
        elif unit == "2":
            unit = "km"
        else:
            raise ValueError
        break
    except ValueError:
        print("ERROR: Only type 1 for miles, or 2 for kilometers.")

#Receive total distance traveled in units above.
while True:
    try:
        distance = float(input("How far did you run in " + unit + "?\n"))
        if distance <= 0:
            raise ValueError
        break
    except ValueError:
        print("ERROR: Only type positive numbers.")

#Functions for pace conversion
def seconds_conversion(seconds): #Determines the decimal portion of seconds within a minute for use in pace calculation.
    minute_portion = seconds/60
    minute_portion = round(minute_portion, 2)
    return minute_portion
def pace_calculator(time, length_of_run): #Pace calculation using decimal_time
    pace = decimal_time / distance
    pace = round(pace, 2)
    pace_string = str(pace)
    pace_string = pace_string.split(".")
    pace_minutes = pace_string[0]
    pace_seconds = pace_string[1]
    pace = pace_minutes + ':' + pace_seconds
    return pace

#Split time input for calculation.
while True:
    minutes_seconds = input("In mm:ss format, how much time did your run take?\n")
    try:
        minutes_seconds = minutes_seconds.split(":")
        minutes = int(minutes_seconds[0])
        seconds = int(minutes_seconds[1])
        break
    except ValueError:
        print("ERROR: Only enter time in mm:ss using positive whole numbers.")

decimal_time = minutes + seconds_conversion(seconds)

#Results display
unit_preference = input("How would you like your results?\n1 - minutes/mile\n2 - minutes/kilometer\n")

#Straight case where unit input is same as desired result units.
if unit == "mi" and unit_preference == "1":
    pass
elif unit =="km" and unit_preference == "2":
    pass

#Mixed case where unit input is different from desired result units.
elif unit == "mi" and unit_preference == "2": #Uses miles to kilometer converter.
    def miles_to_km(distance): #Takes input miles and converts it to kilometers.
        distance = distance * 1.609
        distance = round(distance, 2)
        return distance
    distance = miles_to_km(distance)
    unit = "km"
elif unit == "km" and unit_preference == "1": #Uses kilometer to miles converter.
    def km_to_miles(distance): 
        distance = distance / 1.609
        distance = round(distance, 2)
        return distance
    distance = km_to_miles(distance)
    unit = "mi"
else:
    print("Please indicate your result preference using 1 for minutes/miles and 2 for minutes/kilometer.")
    print("This program will now end. Please try again.")

print("For your " + str(distance) + unit + " run, your pace was", pace_calculator(decimal_time, distance), "minutes per", unit + ".")