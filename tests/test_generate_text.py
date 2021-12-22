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


if __name__ == "__main__":
    test_generate_random_name(5)
    test_generate_random_company_name(10)
    test_generate_random_address(5)
    print("Everything passed")
