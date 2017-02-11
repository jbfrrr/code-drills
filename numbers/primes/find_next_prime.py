import unittest
from is_prime import isPrime

def findNextPrime(number):
    if (isPrime(number+1)):
        return number+1
    else:
        return findNextPrime(number+1)


class FindNextPrimeTest(unittest.TestCase):
    def testFindNextPrime(self):
        self.assertEqual(findNextPrime(100003573), 100003601)
        self.assertEqual(findNextPrime(100000081), 100000123)
        self.assertEqual(findNextPrime(100003063), 100003091)

if __name__ == '__main__':
    unittest.main()
