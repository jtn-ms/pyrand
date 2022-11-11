import unittest

from gen import generateFullName

class TestGen(unittest.TestCase):
	def test_generateFullName(self):
		times = 10
		for i in range(times):
			import random
			gender = random.choice(["female","male"])
			rand_name = generateFullName(gender)

			self.assertEqual(len(rand_name.values()),3)

			from operator import itemgetter
			_first_name, _last_name, _gender = itemgetter("first_name","last_name","gender")(rand_name)
			from gender_guesser import detector as genderGuess
			gd = genderGuess.Detector(case_sensitive=False)
			self.assertEqual(_gender,gender)
			self.assertEqual(_gender,gd.get_gender(_first_name))

if __name__ == "__main__":
	unittest.main()