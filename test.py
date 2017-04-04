import unittest
from prime import generatePrimeNumbers

class primeTestcase(unittest.TestCase):
	def test_isprime(self):
		self.assertEqual(generatePrimeNumbers(5),(3,5))
	def test_negative(self):
		self.assertEqual(generatePrimeNumbers(-1),'Return negative numbers')
	def test_lessthantwo(self):
		self.assertEqual(generatePrimeNumbers(1),'Not a prime number')
	def test_string(self):
		self.assertEqual(generatePrimeNumbers('hhhdh'),'Not a prime number')
if __name__=='__main__':
        unittest.main()
