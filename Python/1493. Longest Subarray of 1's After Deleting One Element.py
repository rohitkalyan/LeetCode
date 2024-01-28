"""
1493. Longest Subarray of 1's After Deleting One Element
Medium
Topics
Companies
Hint
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
"""


def longestSubarray(nums: list[int]) -> int:
    res = 0
    k = 1  # max zeroes we can delete
    l = 0

    for r in range(len(nums)):
        # if we encounter a zero, decrement
        # the num zeroes we can now delete
        if nums[r] == 0:
            k -= 1

        # if we've seen more than one zero
        # move the left pointer until we
        # have discarded the first zero
        # we have encountered hence making the
        # sliding window (l..r) valid again
        while k < 0 and l <= r:
            if nums[l] == 0:
                k += 1
            l += 1

        # make sure you're not adding +1
        # to the sliding window because we
        # want to also account for the deleted
        # zero, so don't index correct here
        res = max(res, r - l)

    return res

if __name__ == '__main__':
    nums = [0,1,1,1,0,1,1,0,1]
    res = longestSubarray(nums)
    print(res)