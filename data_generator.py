import datetime
import random
from faker import Faker
from phone_gen import PhoneNumber


def generate_name():
    return Faker('ru-RU').first_name()


def generate_surname():
    return Faker('ru-RU').last_name()


def generate_address():
    address = Faker('ru-RU').street_name()
    address = address + " " + str(random.randint(1, 100))
    return address


def generate_metro_station():
    return random.randint(1, 10)


def generate_phone_number():
    phone_number = PhoneNumber("RU")
    number = phone_number.get_number()
    return number


def generate_date():
    return "0" + str(datetime.datetime.today().day)


def generate_rental_period():
    return random.randint(1, 7)


def generate_comment():
    return Faker('ru-RU').text(max_nb_chars=100)

