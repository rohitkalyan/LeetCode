"""
Titel: 643. Maximum Average Subarray I
Easy
Topics
Companies
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
"""

from decimal import Decimal

def findMaxAverage(nums, k):
    i, j = 0, k
    maxAverage = 0

    while j < len(nums) + 1:
        sumList = sum(nums[i:j])
        averageList = Decimal(sumList / k)
        maxAverage = max(averageList, maxAverage)
        i += 1
        j += 1

    return round(maxAverage, 5)


if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    result = findMaxAverage(nums, k)
    print(result)
