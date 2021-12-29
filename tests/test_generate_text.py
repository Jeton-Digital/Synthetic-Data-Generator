import importlib.util
from test_generate_text_utils import *

spec = importlib.util.spec_from_file_location("module.name", "../src/synthetic_data_generator/generate_text.py")
generate_text = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generate_text)

def test_generate_random_name(amount):
    name_list = generate_text.generate_random_name(amount)

    assert len(name_list) == amount, "Should be %s".format(amount)
    assert not_contain_numeric(name_list), "Names can not contain numeric values"


def test_generate_random_company_name(amount):
    company_list = generate_text.generate_random_company_name(amount)

    assert len(company_list) == amount, "Should be %s".format(amount)

def test_generate_random_address(amount):
    address_list = generate_text.generate_random_address(amount)

    assert len(address_list) == amount, "Should be %s".format(amount)

def test_generate_random_email(amount):
    company_names = generate_text.generate_random_company_name(amount)

    email_list = generate_text.generate_random_email(amount, company_names)

    assert len(email_list) == amount, "Should be %s".format(amount)
    assert email_contains_at(email_list), "Email should contains @"

def test_generate_random_website(amount):

    company_names = generate_text.generate_random_company_name(amount)

    website_list = generate_text.generate_random_website(amount,company_names)

    assert len(website_list) == amount, "Should be %s".format(amount)

def test_generate_random_region(amount):

    region_list = generate_text.generate_random_region(amount)
    assert len(region_list) == amount, "Should be %s".format(amount)

def test_generate_random_country(amount):

    region_list = generate_text.generate_random_region(amount)
    country_list = generate_text.generate_random_country(amount,region_list)

    assert len(country_list) == amount, "Should be %s".format(amount)

def test_generate_random_phone_number(amount):
    phone_number_list = []

    phone_number_list = generate_text.generate_random_phone_number(amount)

    assert len(phone_number_list) == amount, "Should be %s".format(amount)

def test_generate_random_job_title(amount):

    job_title_list = generate_text.generate_random_job_title(amount)
    assert len(job_title_list) == amount, "Should be %s".format(amount)

def test_generate_random_industry(amount):

    company_names = generate_text.generate_random_company_name(amount)

    sector_list = generate_text.generate_random_sector(amount, company_names)

    industry_list = generate_text.generate_random_industry(amount, sector_list)


    assert len(industry_list) == amount, "Should be %s".format(amount)

def test_generate_random_sector(amount):
    company_names = generate_text.generate_random_company_name(amount)

    sector_list = generate_text.generate_random_sector(amount, company_names)

    assert len(sector_list) == amount, "Should be %s".format(amount)

def test_generate_random_paragraph(amount):

    paragraph_list = generate_text.generate_random_paragraph(amount = amount, min_sentence = 2, max_sentence = 5)
    
    assert len(paragraph_list) == amount, "Should be %s".format(amount)

def test_generate_random_url(amount):

    url_list = generate_text.generate_random_url(amount)

    assert len(url_list) == amount, "Should be %s".format(amount)

if __name__ == "__main__":
    test_generate_random_name(5)
    test_generate_random_company_name(10)
    test_generate_random_address(5)
    test_generate_random_email(5)
    test_generate_random_website(5)
    test_generate_random_region(5)
    test_generate_random_country(5)
    test_generate_random_phone_number(5)
    test_generate_random_job_title(5)
    test_generate_random_industry(5)
    test_generate_random_sector(10)
    test_generate_random_industry(10)
    test_generate_random_paragraph(3)
    test_generate_random_url(5)
    print("Everything passed")
