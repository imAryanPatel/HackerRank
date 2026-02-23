def timeConversion(s):
    period = s[-2:]        
    time_part = s[:-2]       
    hour = int(time_part[:2])

    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return f"{hour:02d}{time_part[2:]}"
