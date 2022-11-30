def add_time(start, duration, day=None):
    week_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", ]

    x = start.split(" ")

    start_split = x[0].split(":")
    duration_split = duration.split(":")

    # convert strings to integers
    start_split = list(map(int, start_split))
    duration_split = list(map(int, duration_split))

    # add hours and minutes and put them into variable
    total_hours = start_split[0] + duration_split[0]
    total_minutes = start_split[1] + duration_split[1]
    period = x[1]

    # divide minutes by 60 and get remainder
    m = divmod(total_minutes, 60)
    minutes = str(m[1]).zfill(2)

    total_hours = total_hours + m[0]  # total hours + remainder from minutes
    # divide hours by 12 and get remainder
    hours = divmod(total_hours, 12)
    hours = list(hours)
    if hours[1] == 0:
        hours[1] = 12

    hour = hours[1]

    days_later = int()

    day_num = int()

    # change AM/PM
    if total_hours >= 12:
        repeat = total_hours // 12
        for i in range(repeat):
            if period == "AM":
                period = "PM"
            else:
                period = "AM"
                days_later += 1

    if days_later > 0:
        try:  # format the day string
            day = day.lower()
            day_num = week_days.index(day)  # find day of the week in a list
            day_num += (days_later + 1)
        except:
            pass

        while day_num > 0:  # cycle through days of the week
            for i in week_days:
                day = i.capitalize()
                day_num -= 1
                if day_num == 0:
                    break

        if days_later == 1:
            days_later = "(next day)"
        elif days_later > 0:
            days_later = f"({days_later} days later)"

    time = f"{hour}:{minutes} {period}"

    if day is None and days_later == 0:
        new_time = time
        return new_time
    elif day is None:
        new_time = f"{time} {days_later}"
        return new_time
    elif days_later == 0:
        new_time = f"{time}, {day}"
        return new_time
    else:
        new_time = f"{time}, {day} {days_later}"
        return new_time
