"""
Title: 394. Decode String

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

"""
import re

if __name__ == '__main__':
    def decode_string(s):
        stack = []
        current_num = 0
        current_string = ''

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_string, current_num))
                current_string = ''
                current_num = 0
            elif char == ']':
                prev_string, num = stack.pop()
                current_string = prev_string + current_string * num
            else:
                current_string += char

        return current_string


    # Example usage
    s1 = "3[a]2[bc]"
    print("Output 1:", decode_string(s1))

    s2 = "3[a2[c]]"
    print("Output 2:", decode_string(s2))

    s3 = "2[abc]3[cd]ef"
    print("Output 3:", decode_string(s3))
