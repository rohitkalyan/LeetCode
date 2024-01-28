"""
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""


def maxVowels(s, k):

    vowels = set(["a", "e", "i", "o", "u"])

    b = e = curMax = cur = 0
    while b + k <= len(s):
        if cur == k:
            return k
        if s[e] in vowels:
            cur += 1
            e += 1
            curMax = max(curMax, cur)

        if e - b >= k:
            if s[b] in vowels:
                cur -= 1
                b += 1

    return curMax






if __name__ == '__main__':
    s = "abciiidef"
    k = 3
    result = maxVowels(s, k)
    print(result)
