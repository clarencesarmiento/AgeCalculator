from box import print_msg_box


def today_month(recent_month):
    # Check the month if available...
    if recent_month == "January" or recent_month == "Jan":
        y = 1
        return y
    elif recent_month == "February" or recent_month == "Feb":
        y = 2
        return y
    elif recent_month == "March":
        y = 3
        return y
    elif recent_month == "April":
        y = 4
        return y
    elif recent_month == "May":
        y = 5
        return y
    elif recent_month == "June":
        y = 6
        return y
    elif recent_month == "July":
        y = 7
        return y
    elif recent_month == "August" or recent_month == "Aug":
        y = 8
        return y
    elif recent_month == "September" or recent_month == "Sep":
        y = 9
        return y
    elif recent_month == "October" or recent_month == "Oct":
        y = 10
        return y
    elif recent_month == "November" or recent_month == "Nov":
        y = 11
        return y
    elif recent_month == "December" or recent_month == "Dec":
        y = 12
        return y
    else:
        print_msg_box(msg="Invalid today's month", title="Process Failed!")
        exit()
