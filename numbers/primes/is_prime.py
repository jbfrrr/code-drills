import unittest
from math import sqrt

def isPrime(number):
    if (number < 2):
        return False
    limit = sqrt(number)
    factor = 2
    while (factor <= limit):
        if ((number % factor) == 0):
            return False
        factor += 1
    return True

class IsPrimeTests(unittest.TestCase):
    def testIsPrime(self):
        self.assertFalse(isPrime(133))
        self.assertFalse(isPrime(1))
        self.assertFalse(isPrime(0))
        self.assertFalse(isPrime(843))
        self.assertTrue(isPrime(524287))
        self.assertTrue(isPrime(131071))
        self.assertTrue(isPrime(2147483647))

if __name__ == '__main__':
    unittest.main()
