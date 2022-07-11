import random
from faker import Faker
from data.data import Person, Color

faker_en = Faker('en_US')
Faker.seed()


def generate_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        firstname=faker_en.first_name(),
        lastname=faker_en.last_name(),
        age=random.randint(18, 100),
        department=faker_en.job(),
        salary=random.randint(2000, 20000),
        email=faker_en.email(),
        cur_addr=faker_en.address(),
        permanent_addr=faker_en.address(),
        mobile=faker_en.msisdn()[:10],
    )


def generate_color():
    yield Color(
        color_name=['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Black', 'White', 'Violet', 'Indigo', 'Magenta', 'Aqua']
    )
