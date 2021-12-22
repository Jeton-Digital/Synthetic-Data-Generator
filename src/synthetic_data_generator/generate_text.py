from names import get_full_name
import random
from barnum import gen_data
from faker import Faker


def generate_random_name(amount):
    list_random_name = []

    for i in range(amount):
        name = get_full_name()
        list_random_name.append(name)

    return list_random_name

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

def generate_random_company_name(amount):

    list_random_company = []

    for i in range(amount):
        company_name = gen_data.create_company_name()
        list_random_company.append(company_name)

    return list_random_company

def generate_random_address(amount):

    list_random_address = []

    for i in range(amount):

        zip_code, city, state = gen_data.create_city_state_zip()
        street = gen_data.create_street()

        address = city + " " + street + " " + state + " " + zip_code
        print(address)
        list_random_address.append(address)

    # fake = Faker()

    # for i in range(amount):
    #     address = fake.address()
    #     print(address)
    #     list_random_address.append(address)

    return list_random_address




