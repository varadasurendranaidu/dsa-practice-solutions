
"""
DSA Practice Solutions
Algorithms: duplicate detection, Two Sum, and binary search.

Assumptions:
- Inputs contain integers.
- Binary search receives a sorted list in ascending order.
"""


def contains_duplicate(nums):
    """
    Return True if any value appears more than once.

    Time: O(n) average
    Space: O(n)
    """
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


def two_sum(nums, target):
    """
    Return indices of two distinct elements whose sum is target.
    Return None if no valid pair exists.

    Time: O(n) average
    Space: O(n)
    """
    seen = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], index]

        seen[num] = index

    return None


def binary_search(nums, target):
    """
    Return the index of target in an ascending sorted list.
    Return -1 if target is absent.

    Time: O(log n)
    Space: O(1)
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    print("Duplicate detection:", contains_duplicate([1, 2, 3, 2]))
    print("Two Sum:", two_sum([2, 7, 11, 15], 9))
    print("Binary search:", binary_search([1, 3, 5, 7, 9], 7))
