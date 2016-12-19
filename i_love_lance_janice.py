# -*- coding: utf-8 -*-
"""
I Love Lance & Janice
=====================

You've caught two of your fellow minions passing coded notes back and forth - while they're on duty, no less! Worse, you're pretty sure it's not job-related - they're both huge fans of the space soap opera "Lance & Janice". You know how much Commander Lambda hates waste, so if you can prove that these minions are wasting her time passing non-job-related notes, it'll put you that much closer to a promotion.

Fortunately for you, the minions aren't exactly advanced cryptographers. In their code, every lowercase letter [a..z] is replaced with the corresponding one in [z..a], while every other character (including uppercase letters and punctuation) is left untouched.  That is, 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.  For instance, the word "vmxibkgrlm", when decoded, would become "encryption".

Write a function called answer(s) which takes in a string and returns the deciphered string so you can show the commander proof that these minions are talking about "Lance & Janice" instead of doing their jobs.


Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) s = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
Output:
    (string) "did you see last night's episode?"

Inputs:
    (string) s = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
Output:
    (string) "Yeah! I can't believe Lance lost his job at the colony!!"
"""

def decrypt(index):

    new_index = (0 - index) - 1

    return new_index


def answer(s):

    split_words_list = list(s)

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    decrypted_words_list = []

    for i, string in enumerate(split_words_list):

        if string in alphabet:

            string = alphabet[decrypt(alphabet.index(string))]
            decrypted_words_list.append(string)

        else:
            decrypted_words_list.append(string)

    result_string = ''

    for i, string in enumerate(decrypted_words_list):

        result_string += string

    return result_string


# s = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
# "did you see last night's episode?"

s = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
# "Yeah! I can't believe Lance lost his job at the colony!!"

print answer(s)
