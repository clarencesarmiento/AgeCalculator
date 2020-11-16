def day_year(year, month, day):
    if month == 1:
        month += 12
        year -= 1
    elif month == 2:
        month += 12
        year -= 1
    cent = (year // 100)
    cent_year = (year % 100)
    day_of_the_week = (day + ((26 * (month + 1)) // 10) + cent_year + (cent_year // 4) + (cent // 4) + (
            5 * cent)) % 7
    if day_of_the_week == 0:
        return "Day you're born is Saturday."
    elif day_of_the_week == 1:
        return "Day you're born is Sunday."
    elif day_of_the_week == 2:
        return "Day you're born is Monday."
    elif day_of_the_week == 3:
        return "Day you're born is Tuesday."
    elif day_of_the_week == 4:
        return "Day you're born is Wednesday."
    elif day_of_the_week == 5:
        return "Day you're born is Thursday."
    elif day_of_the_week == 6:
        return "Day you're born is Friday."
