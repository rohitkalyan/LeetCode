"""
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""
import self as self


def mergeAlternately(self, word1: str, word2: str) -> str:
    i, j = 0, 0

    res = []
    while i < len(word1) and j < len(word2):
        res.append(word1[i])
        res.append(word2[j])
        i += 1
        j += 1
    res.append(word1[i:])
    res.append(word2[j:])

    return "".join(res)

if __name__ == '__main__':

    result = mergeAlternately(self, "abc", "pqr")
    print(result)