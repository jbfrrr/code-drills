import unittest
from math import ceil

def getMiddleIndex(startIndex, endIndex):
    return ceil((endIndex - startIndex) / 2)

def binarySearch(sortedList, target):
    start_index = 0
    end_index = len(sortedList) - 1;

    while (start_index <= end_index):
        middle_index = start_index + getMiddleIndex(start_index, end_index)
        if (sortedList[middle_index] == target):
            return middle_index;
        if (sortedList[middle_index] < target):
            start_index = middle_index + 1
        else:
            end_index = middle_index - 1

    return -1


class BinarySearchTests(unittest.TestCase):
    def setUp(self):
        self.sampleList = [1,3,5,7,11,13,17,19,23,29]
    def testFindExistingElements(self):
        self.assertEqual(binarySearch(self.sampleList, 5), 2)
        self.assertEqual(binarySearch(self.sampleList, 29), 9)
        self.assertEqual(binarySearch(self.sampleList, 1), 0)
        self.assertEqual(binarySearch(self.sampleList, 19), 7)

    def testFindNonExistentElements(self):
        self.assertEqual(binarySearch(self.sampleList, 2), -1)
        self.assertEqual(binarySearch(self.sampleList, 20), -1)

if __name__ == '__main__':
    unittest.main()
