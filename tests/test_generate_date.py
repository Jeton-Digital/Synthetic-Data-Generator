import importlib.util
from test_generate_date_utils import *

spec = importlib.util.spec_from_file_location("module.name", "../src/synthetic_data_generator/generate_date.py")
generate_date = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generate_date)

def test_generate_random_date(amount, min_year=1930, max_year=2022):
    date_list = generate_date.generate_random_date(amount, min_year, max_year)

    assert len(date_list) == amount, "Should be %s".format(amount)
    assert date_format(date_list), "Date format should be in dd/mm/yyyy format."
    assert year_interval(date_list,min_year,max_year), "Year should be between %s and %s".format(min_year, max_year)

if __name__ == "__main__":
    test_generate_random_date(5)
    print("Everything passed")