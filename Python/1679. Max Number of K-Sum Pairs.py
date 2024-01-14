"""
Title: 1679. Max Number of K-Sum Pairs
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

"""
from collections import Counter


def maxOperations(nums: list[int], k: int) -> int:
    ct = Counter(nums)
    res = 0
    for n in ct:
        tmp = k - n
        if n == tmp:
            res += ct[n] // 2
            continue
        if n < tmp:
            res += min(ct[n], ct[tmp])
    return res
if __name__ == '__main__':
    nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
    # nums = [1,2,3,4]?
    k = 2
    result = maxOperations(nums, k)
    print(result)