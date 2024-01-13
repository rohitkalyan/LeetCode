"""
Title: 443. String Compression
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
"""

#   My soultion
"""
def compress(chars: list[str]) -> int:

    setChars = sorted(set(chars))
    charsString = "".join(chars)
    res = []

    for i in setChars:
        countVlaues = charsString.count(i)
        if countVlaues != 1:
            res.append(i)
            res.append(str(countVlaues))
        else:
            res.append(i)

    print(res)
    chars = res
    print("this is Chars ", chars)
    resString = "".join(res)
    return len(resString)
"""
def compress(chars: list[str]) -> int:
    if not chars:
        return 0

    write_index = 0
    read_index = 0

    while read_index < len(chars):
        char = chars[read_index]
        count = 0

        while read_index < len(chars) and chars[read_index] == char:
            read_index += 1
            count += 1

        chars[write_index] = char
        write_index += 1

        if count > 1:
            for digit in str(count):
                chars[write_index] = digit
                write_index += 1

    return write_index

if __name__ == '__main__':
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    result = compress(chars)
    print(result)
