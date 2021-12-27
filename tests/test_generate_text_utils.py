def not_contain_numeric(name_list):
    for name in name_list:
        for ch in name:
            if ch.isnumeric():
                return False
    return True

def email_contains_at(email_list):
    for email in email_list:
        if "@" not in email:
            return False
    return True