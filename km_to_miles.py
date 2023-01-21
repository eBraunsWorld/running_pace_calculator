while True:
    try:
        km = float(input("Enter kilometers: "))
        if km <= 0:
            raise ValueError
        def km_to_miles(distance):
            miles = km / 1.609
            miles = round(miles , 2)
            return miles
        print(km, "kilometers is the same as", km_to_miles(km), "miles.")
        break
    except ValueError:
        print("ERROR: Type only positive numbers.")