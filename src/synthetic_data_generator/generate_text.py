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


def generate_random_company_name(amount):

    list_random_company = []

    for i in range(amount):
        company_name = gen_data.create_company_name()
        list_random_company.append(company_name)

    return list_random_company

def generate_random_address(amount):

    list_random_address = []

    for i in range(amount):

        zip_code, _, state = gen_data.create_city_state_zip()
        street = gen_data.create_street()

        address =  " " + street + " " + state + " " + zip_code
        list_random_address.append(address)

    # fake = Faker()

    # for i in range(amount):
    #     address = fake.address()
    #     print(address)
    #     list_random_address.append(address)

    return list_random_address

def generate_random_email(amount, keywords = None):

    list_random_email = []

    if keywords:
        
        for i in range(amount):
            k_word = tuple(keywords[i].split())
            email = gen_data.create_email(name = k_word)
            list_random_email.append(email)
    else:
        for i in range(amount):
            email = gen_data.create_email()
            list_random_email.append(email)


    return list_random_email

def generate_random_website(amount, keywords = None):

    list_random_website = []
    if keywords:
        for i in range(amount):
            k_word = tuple(keywords[i].split())
            user_choices = ["%s.%s" % (k_word[0], k_word[1]), "%s" % k_word[0], "%s.%s" % (k_word[0][:1], k_word[1]), "%s%s" %(random.choice(gen_data.latin_words), random.randint(0,9999))]
            domain = random.choice(gen_data.email_domains)
            website = ("%s.%s" % (random.choice(user_choices), domain)).lower()
            list_random_website.append(website)

    else:
        for i in range(amount):
            choices = ["%s.%s" % (random.choice(gen_data.latin_words), random.randint(0,9999)), "%s" %(random.choice(gen_data.latin_words))]
            domain = random.choice(gen_data.email_domains)
            website = ("%s.%s" % (random.choice(choices), domain)).lower()
            list_random_website.append(website)

    return list_random_website

def generate_random_industry(amount, sector = None):

    dict_industry_sector = {
        'Technology' : ['Software', 'Hardware', 'Electronics', 'Graphics', 'Application', 'Virtual', 'Electronic', 'Data'],
        'Telecommunications' : ['Telecom', 'Internet', 'Network'],
        'Consulting' : ['Research', 'Analysis', 'Contract', 'Solutions'],
        'Construction' : ['Architecture', 'Building'],
        'Health' : ['Medicine'],
        'Entertainment' : ['Adventure']
    }

    list_random_industries = []

    industries = dict_industry_sector.keys()     

    if sector:
        for i in range(amount):
            industry_found = False
            for industry in industries:
                if sector[i] in dict_industry_sector[industry] and not industry_found:
                    list_random_industries.append(industry)
                    industry_found = True
            
            if not industry_found:
                list_random_industries.append(random.choice(industries))

    else:      
        for i in range(amount):
            industry = random.choice(industries)
            list_random_industries.append(industry)

    return list_random_industries

def generate_random_sector(amount, keywords = None):
    sectors = ['Telecom', 'Software', 'Hardware', 'Electronics', 'Research', 'Architecture', 'Building', 'Medicine',
    'Graphics', 'Analysis', 'Contract', 'Solutions', 'Internet', 'Application', 'Virtual', 'Network', 'Electronic', 'Data', 'Adventure']

    list_random_sector = []
    if keywords:
        for i in range(amount):
            sector_found = False
            for word in keywords[i].split():
                if word in sectors and not sector_found:
                    list_random_sector.append(word)
                    sector_found = True
            
            if not sector_found:
                sector = random.choice(sectors)
                list_random_sector.append(sector)
    else:
        for i in range(amount):
            sector = random.choice(sectors)
            list_random_sector.append(sector)

    return list_random_sector

def generate_random_job_title(amount):

    list_random_job_title = []
    for i in range(amount):
        job_title = gen_data.create_job_title()
        list_random_job_title.append(job_title)

    return list_random_job_title

def generate_random_region(amount):

    list_random_region = []

    regions = ['US','EU','AS']
    for i in range(amount):
        list_random_region.append(random.choice(regions))
    
    return list_random_region

def generate_random_country(amount, region_list = None):

    countries_by_region = {
        'EU' : ["Andorra", "Albania", "Armenia", "Austria", "Bosnia and Herzegovina", "Belgium", "Bulgaria", "Belarus", "Switzerland", "Cyprus", "Czech Republic", "Germany", "Denmark", "Estonia", "Spain", "Finland", "Faroe Islands", "France", "France, Metropolitan" , "United Kingdom", "Georgia"],
        'US' : ["Antigua and Barbuda", "Anguilla", "Barbados", "Bermuda", "Brazil", "Canada", "Colombia", "United States"],
        'AS' : ["Afghanistan", "Antarctica", "Australia", "Azerbaijan", "Bangladesh", "Vietnam", "Vanuatu"] 
    }

    list_random_country = []
    if region_list:
        for i in range(amount):
            country = random.choice(countries_by_region[region_list[i]])
            list_random_country.append(country)
    else:
        regions = ['EU', 'US', 'AS']
        
        for i in range(amount):
            region = random.choice(regions)

            country = random.choice(countries_by_region[region])
            list_random_country.append(country)

    return list_random_country

def generate_random_phone_number(amount):

    list_random_phone_number = []
    faker = Faker()

    for i in range(amount):
        phone_number = faker.phone_number()
        list_random_phone_number.append(phone_number)
    
    return list_random_phone_number


        




