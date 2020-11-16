from box import print_msg_box


def month_of_birth(birth_month):
    # Check the month if available...
    if birth_month == "Jan" or birth_month == "January":
        x = 1
        return x
    elif birth_month == "Feb" or birth_month == "February":
        x = 2
        return x
    elif birth_month == "March":
        x = 3
        return x
    elif birth_month == "April":
        x = 4
        return x
    elif birth_month == "May":
        x = 5
        return x
    elif birth_month == "June":
        x = 6
        return x
    elif birth_month == "July":
        x = 7
        return x
    elif birth_month == "Aug" or birth_month == "August":
        x = 8
        return x
    elif birth_month == "Sept" or birth_month == "September":
        x = 9
        return x
    elif birth_month == "Oct" or birth_month == "October":
        x = 10
        return x
    elif birth_month == "Nov" or birth_month == "November":
        x = 11
        return x
    elif birth_month == "Dec" or birth_month == "December":
        x = 12
        return x
    else:
        print_msg_box(msg="Invalid Birth month", title="Process Failed!")
        exit()
