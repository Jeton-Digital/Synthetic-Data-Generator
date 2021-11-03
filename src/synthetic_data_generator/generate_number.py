import random


def generate_random_int(amount, min, max):

    list_random_int = []

    for i in range(amount):
        list_random_int.append(random.randint(min, max))

    return list_random_int