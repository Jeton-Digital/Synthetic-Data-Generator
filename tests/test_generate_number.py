import importlib.util

spec = importlib.util.spec_from_file_location("module.name", "../src/synthetic_data_generator/generate_number.py")
generate_number = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generate_number)


def test_generate_random_int(amount, min, max):
    len_list = len(generate_number.generate_random_int(amount, min, max))
    assert len_list == amount, "Should be %s".format(amount)


if __name__ == "__main__":
    test_generate_random_int(2, 1, 10)
    print("Everything passed")