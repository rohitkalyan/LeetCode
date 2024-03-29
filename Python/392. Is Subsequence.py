"""
392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""

def listToStringJoin(wordList: list) -> str:
    return "".join(wordList)

def isSubsequence(s: str, t: str) -> bool:

    i = 0
    j = 0
    while j <len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1

    if i == len(s):
        return True
    else:
        return False

if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    result = isSubsequence(s,t)
    print(result)
