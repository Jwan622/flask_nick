import unittest
from app.services.nicks_code import ComplicatedThing

class TestNicksCode(unittest.TestCase):
	def test_perform_calc(self):
		expected = ComplicatedThing().perform_calc()

		self.assertEqual(expected, "something ccompli9cated")

if __name__ == '__main__':
	unittest.main()