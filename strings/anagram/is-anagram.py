import unittest

def isAnagram(stringX, stringY):
    if (len(stringX) != len(stringY)):
        return False

    stringX = stringX.lower()
    stringY = stringY.lower()
    stringXCharacterFrequency = {}
    stringYCharacterFrequency = {}
    iterator = 0

    while (iterator < len(stringX)):
        if (stringX[iterator] not in stringXCharacterFrequency):
            stringXCharacterFrequency[stringX[iterator]] = 0

        if (stringY[iterator] not in stringYCharacterFrequency):
            stringYCharacterFrequency[stringY[iterator]] = 0

        stringXCharacterFrequency[stringX[iterator]] += 1
        stringYCharacterFrequency[stringY[iterator]] += 1
        iterator += 1

    return hash(frozenset(stringXCharacterFrequency)) == hash(frozenset(stringYCharacterFrequency))

class IsAnagramTest(unittest.TestCase):
    def testIsAnagram(self):
        self.assertTrue(isAnagram('allergy', 'gallery'))
        self.assertTrue(isAnagram('cautioned', 'education'))
        self.assertTrue(isAnagram('basiparachromatin', 'marsipobranchiata'))
        self.assertFalse(isAnagram('anagram', 'grammar'))
        self.assertFalse(isAnagram('palindrome', 'drones'))
        self.assertFalse(isAnagram('marsupial', 'suppliers'))

if __name__ == '__main__':
    unittest.main()
