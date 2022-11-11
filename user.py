import phonenumbers
from faker.providers.phone_number.en_US import Provider
class CustomPhoneProvider(Provider):
  def phone_number(self):
    while True:
      phone_number = self.numerify(self.random_element(self.formats))
      parsed_number = phonenumbers.parse(phone_number, 'US')
      if phonenumbers.is_valid_number(parsed_number):
        return phonenumbers.format_number(
          parsed_number,
          phonenumbers.PhoneNumberFormat.E164
        )

# import factory
from faker import Faker
# from . import models
fake = Faker()
fake.add_provider(CustomPhoneProvider)

import utils.gen as rand

class UserFactory():
  # first_name = factory.Faker('first_name')
  # last_name = factory.Faker('last_name')
  # phone_number = factory.LazyAttribute(lambda _: fake.phone_number())

  def __init__(self):
    self.first_name = fake.first_name()
    self.last_name = fake.last_name()
    self.phone_number = fake.phone_number()
    self.email = fake.email()# rand.generateEmailByFullName(name)
    # self.address=fake.address()# rand.generateAddress()

    from gender_guesser import detector as genderGuess
    gd = genderGuess.Detector(case_sensitive=False)
    self.gender = gd.get_gender(self.first_name)
    # name = rand.generateFullName(gender)
    from datetime import date
    self.dob = rand.generateRandomDate(start=date(1976,1,1),end=date(2000,1,1)).strftime("%Y-%m-%d")

  def json(self):
    return self.__dict__#{k:v for k,v in self.__dict__.items() if not k.startswith('__') and not callable(k)}

  def __repr__(self):
    return str(self.json())

  def __str__(self):
    return str(self.json())

def generateCustomerDB():
  size = 100
  users = []
  for i in range(size):
    user = UserFactory().json() 
    user["id"] = f"85{str(i).rjust(3,'0')}"
    import random
    user["status"] = random.choice(["Sold","Estimate"])
    user["address"] = "DK"
    key_order=["id","first_name","last_name","status","phone_number","address","email","gender","dob"]
    print(user)
    users.append({k:user[k] for k in key_order})
  import pandas as pd
  df = pd.DataFrame(users)
  df.to_csv("output/customers.csv",index=False,header=True)

if __name__ == "__main__":
  generateCustomerDB()