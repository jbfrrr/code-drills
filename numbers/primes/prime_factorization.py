import unittest
from is_prime import isPrime
from find_next_prime import findNextPrime

def getPrimeFactorization(number, primeFactors, primeNumber = 2):
    if (isPrime(number)):
        primeFactors.append(number)
        return primeFactors
    if ((number % primeNumber) == 0):
        primeFactors.append(primeNumber)
        return getPrimeFactorization(
                int(number/primeNumber),
                primeFactors,
                primeNumber)
    return getPrimeFactorization(
            number,
            primeFactors,
            findNextPrime(primeNumber))


class PrimeFactorizationTest(unittest.TestCase):
    def testGetPrimeFactorization(self):
        self.assertEqual(
                getPrimeFactorization(300, []),
                [2, 2, 3, 5, 5])
        self.assertEqual(
                getPrimeFactorization(10034233, []),
                [11, 17, 23, 2333])
        self.assertEqual(
                getPrimeFactorization(7899, []),
                [3, 2633])

if __name__ == '__main__':
    unittest.main()
