import string
import random

import names
def generateFullName(gender="male"):
  first_name, last_name= names.get_full_name(gender).split()
  return {"first_name":first_name, "last_name": last_name, "gender":gender}

from random_address import real_random_address
def generateAddress():
  # real_random_address_by_state('CA')
  # real_random_address_by_postal_code('32409')
  return real_random_address()

from datetime import date, timedelta
def generateRandomDate(start:date,end:date):
  delta = end-start
  total_days = delta.days
  return start+timedelta(days=random.randrange(total_days))

def generateDOB(start=date(1976,1,1),end=date(2000,1,1)):
  return { "dob": generateRandomDate(start,end).strftime("%Y-%m-%d")}

def generateEmailByFullName(fullname):
  from operator import itemgetter
  _first_name, _last_name = itemgetter("first_name","last_name")(fullname)
  return {"email":f"{_first_name.lower()}{_last_name.lower()}@gmail.com"}

def generateRandomEmail():
  size = random.randint(4,12)
  result = ''.join([random.choice(string.ascii_lowercase) for i in range(size)])
  return f"{result}@gmail.com"

def generateUserInfo():
  gender = random.choice(["female","male"])
  name = generateFullName(gender)
  dob = generateDOB()
  email = generateEmailByFullName(name)
  address = generateAddress()
  return {**name,**dob,**email,**address}

if __name__ == "__main__":
  print(generateUserInfo())
