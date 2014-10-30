import unittest
import calc

class TestCalc(unittest.TestCase):
	def test_create_account(self):
		calc.create_account('saving', 700)
		self.assertTrue(1)

	def test_deposit(self):
		calc.deposit(333, 'saving')
		self.assertTrue(1)

	def test_output(self):
		calc.output()

if __name__ == '__main__':
	unittest.main()