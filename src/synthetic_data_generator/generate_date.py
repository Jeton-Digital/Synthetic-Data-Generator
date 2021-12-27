import random

def generate_random_date(amount, min_year=1930, max_year=2022):

    list_random_date = []

    for i in range(amount):
        year = random.randint(min_year, max_year)
        month = random.randint(1,12)

        if month == 12 or month == 10 or month == 8 or month == 7 or month == 5 or month == 3 or month == 1:
            day = random.randint(1,31)
        else:
            if month == 2:
                if year % 4 == 0:
                    day = random.randint(1,29)
                else:
                    day = random.randint(1,28)
            else:
                day = random.randint(1,30)

        date = str(day) + "/" + str(month) + "/" + str(year)
        list_random_date.append(date)

    return list_random_date
