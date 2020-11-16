from design import design
from box import print_msg_box
from birthmonth import month_of_birth
from todaymonth import today_month
from dayoftheYear import day_year
import time

exit_press = True
design()
# Loop our program using While loop...
while exit_press:
    print_msg_box(msg="""Follow this order: Month Date Year
Example: October 20 2000""")
    birth_month, birth_date, birth_year = [str(x) for x in input("Enter Birthday: ").split()]
    recent_month, recent_date, recent_year = [str(x) for x in input("Enter Today's date: ").split()]

    birth_month = birth_month.capitalize()
    recent_month = recent_month.capitalize()

    print("Processing...")
    time.sleep(2)
    # Check if our birth date and recent date is in range of calendars date.
    if int(birth_date) > 31:
        print_msg_box(msg="Invalid Birth date", title="Process Failed!")
        exit()
    elif int(recent_date) > 31:
        print_msg_box(msg="Invalid Today's date", title="Process Failed!")
        exit()
    else:
        pass

    if int(len(birth_year)) != 4:
        print_msg_box(msg="Invalid Birth year", title="Process Failed!")
        exit()
    elif int(len(recent_year)) != 4:
        print_msg_box(msg="Invalid Today's year", title="Process Failed!")
        exit()
    else:
        pass
    # Formula to get the total age...
    total_age = (int(recent_year) - int(birth_year)) - 1
    # Check if we're going to update the age...
    if month_of_birth(birth_month=birth_month) < today_month(recent_month=recent_month):
        total_age += 1
    elif month_of_birth(birth_month=birth_month) == today_month(recent_month=recent_month):
        if int(birth_date) <= int(recent_date):
            total_age += 1
        else:
            pass
    else:
        pass
    print_msg_box(msg=f"""Your Birthday is {birth_month} {birth_date},{birth_year}
The Date today is {recent_month} {recent_date},{recent_year}
Your age is {total_age}.
{day_year(year=int(birth_year), month=month_of_birth(birth_month), day=int(birth_date))}""", title="Process Success!")
    time.sleep(1)
    exit_key = input("Type 'x' to exit or any key to try again.\n")
    exit_key = exit_key.lower()
    if exit_key == "x":
        exit_press = False
    else:
        exit_press = True
