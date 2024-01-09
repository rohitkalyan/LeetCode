"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""



def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    if len(str1) == len(str2):
        return str1
    if len(str1) > len(str2):
        return gcdOfStrings(str1[len(str2):], str2)
    return gcdOfStrings(str1, str2[len(str1):])


if __name__ == '__main__':
    result = gcdOfStrings("ABCABC", "ABC")
    print(result)