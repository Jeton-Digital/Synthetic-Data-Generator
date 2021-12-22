def not_contain_numeric(name_list):
    for name in name_list:
        for ch in name:
            if ch.isnumeric():
                return False
    return True