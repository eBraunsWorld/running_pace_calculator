minutes_seconds = input("In mm:ss format, how much time did your run take?\n")
minutes_seconds = minutes_seconds.split(":")
minutes = int(minutes_seconds[0])
seconds = int(minutes_seconds[1])
def seconds_conversion(seconds):
    minute_portion = seconds/60
    minute_portion = round(minute_portion, 2)
    return minute_portion
decimal_time = minutes + seconds_conversion(seconds)

