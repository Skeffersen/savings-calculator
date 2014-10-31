import unittest
import calc

class TestCalc(unittest.TestCase):
	def test_create_account(self):
		calc.create_account('savings')
		calc.create_account('debt')
		self.assertTrue(1)

	def test_deposit(self):
		calc.deposit(3900, 'debt')
		self.assertTrue(1)

	def test_output(self):
		calc.output()
		self.assertTrue(1)

	def test_transaction_receipt(self):
		calc.transaction_receipt()
		self.assertTrue(1)

if __name__ == '__main__':
	unittest.main()