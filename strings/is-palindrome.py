import unittest

def isPalindrome(userInput):
    primedUserInput = userInput.lower().replace(' ', '')
    front = 0
    tail = len(primedUserInput) - 1
    while front <= tail:
        if (primedUserInput[front] != primedUserInput[tail]):
            return False
        front += 1
        tail -= 1
    return True

class IsPalindromeTest(unittest.TestCase):
    def testIsPalindrome(self):
        self.assertTrue(isPalindrome('A but Tuba'))
        self.assertTrue(isPalindrome('Flee to me Remote Elf'))
        self.assertFalse(isPalindrome('anatawa'))
        self.assertFalse(isPalindrome('not a palindrome'))

if __name__ == '__main__':
    unittest.main()
