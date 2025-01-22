def format_time(date_time):
    date, time = date_time.split()

    day, month, year = date.split("/")
    hours, mins, secs = time.split(":")

    if int(day) > 31 or int(day) < 1:
        print("Day is invalid")
        return
    elif int(month) > 12 or int(month) < 1:
        print("Month is invalid")
        return
    elif int(year) < 1 or int(year) > 3000:
        print("Year is invalid")
        return
    
    if int(hours) > 24 or int(hours) < 0:
        print("Hour is invalid")
        return
    elif int(mins) > 59 or int(mins) < 0:
        print("Minute is invalid")
        return
    elif int(secs) < 0 or int(secs) > 59:
        print("Second is invalid")
        return

    print("-> " + date)
    print("-> " + time)
    print("-> " + month)

    if int(hours) < 11:
        print("-> p.m")
    else:
        print("-> a.m")



format_time("21/02/2020 18:06:00")
print()
format_time("37/05/1950 12:00:00")
print()
format_time("01/01/1900 25:06:00")