"""
Tilte: 345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
"""

def reverseVowels(s: str) -> str:
    vowleList = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    stringVowels = []
    res = []
    k = 0

    for i in s:
        if i in vowleList:
            stringVowels.append(i)

    stringVowels.reverse()

    for i in s:
        if i in vowleList:
            res.append(stringVowels[k])
            k += 1
        else:
            res.append(i)

    return "".join(res)


if __name__ == '__main__':
    s = "hello"
    result = reverseVowels(s)
    print(result)