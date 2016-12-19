"""
The cake is not a lie!
======================

Commander Lambda has had an incredibly successful week: she completed the first test run of her LAMBCHOP doomsday device, she captured six key members of the Bunny Rebellion, and she beat her personal high score in Tetris. To celebrate, she's ordered cake for everyone - even the lowliest of minions! But competition among minions is fierce, and if you don't cut exactly equal slices of cake for everyone, you'll get in big trouble.

The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms are not: there are multiple colors, and every minion must get exactly the same sequence of M&Ms. Commander Lambda hates waste and will not tolerate any leftovers, so you also want to make sure you can serve the entire cake.

To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: each possible letter (between a and z) corresponds to a unique color, and the sequence of M&Ms is given clockwise (the decorations form a circle around the outer edge of the cake).

Write a function called answer(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) s = "abccbaabccba"
Output:
    (int) 2

Inputs:
    (string) s = "abcabcabcabc"
Output:
    (int) 4
"""

def sliceString(s):
    str_list = []

    for i in range(len(s)):
        sliced_str = s[0:i+1]
        str_list.append(sliced_str)

    return str_list


def answer(s):

    str_list = sliceString(s)
    str_length_list = []

    for i, elm in enumerate(str_list):

        counted_elm = s.count(elm)
        quotient = len(s)/len(elm)

        if (elm * quotient) == s:

            str_length_list.append(counted_elm)

    str_length_list.sort()
    max_str_length = str_length_list[-1]

    return max_str_length

# s = "abccbaabccba"
# 2

s = "abcabcabcabc"
# 4


print answer(s)