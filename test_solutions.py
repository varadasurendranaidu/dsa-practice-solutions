
import unittest

from solutions import contains_duplicate, two_sum, binary_search


class TestContainsDuplicate(unittest.TestCase):

    def test_duplicate_exists(self):
        self.assertTrue(contains_duplicate([1, 2, 3, 2]))

    def test_no_duplicates(self):
        self.assertFalse(contains_duplicate([1, 2, 3, 4]))

    def test_empty_list(self):
        self.assertFalse(contains_duplicate([]))

    def test_single_element(self):
        self.assertFalse(contains_duplicate([5]))

    def test_repeated_values(self):
        self.assertTrue(contains_duplicate([7, 7]))


class TestTwoSum(unittest.TestCase):

    def test_valid_pair(self):
        result = two_sum([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])

    def test_pair_not_at_start(self):
        result = two_sum([3, 2, 4], 6)
        self.assertEqual(result, [1, 2])

    def test_negative_numbers(self):
        result = two_sum([-3, 4, 3, 90], 0)
        self.assertEqual(result, [0, 2])

    def test_same_value_at_different_indices(self):
        result = two_sum([3, 3], 6)
        self.assertEqual(result, [0, 1])

    def test_no_valid_pair(self):
        self.assertIsNone(two_sum([1, 2, 3], 10))

    def test_empty_list(self):
        self.assertIsNone(two_sum([], 5))

    def test_single_element(self):
        self.assertIsNone(two_sum([5], 10))


class TestBinarySearch(unittest.TestCase):

    def test_target_in_middle(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 5), 2)

    def test_target_at_start(self):
        self.assertEqual(binary_search([1, 3, 5, 7], 1), 0)

    def test_target_at_end(self):
        self.assertEqual(binary_search([1, 3, 5, 7], 7), 3)

    def test_target_missing(self):
        self.assertEqual(binary_search([1, 3, 5, 7], 4), -1)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 5), -1)

    def test_single_element_found(self):
        self.assertEqual(binary_search([8], 8), 0)

    def test_single_element_missing(self):
        self.assertEqual(binary_search([8], 3), -1)


if __name__ == "__main__":
    unittest.main()
