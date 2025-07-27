from faker import Faker

fake = Faker()

def generate_user():
    return {
        "first": fake.first_name(),
        "last": fake.last_name(),
        "zip": fake.zipcode()
    }
