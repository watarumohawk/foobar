# -*- coding: utf-8 -*-
"""
En Route Salute
===============

Commander Lambda loves efficiency and hates anything that wastes time. She's a busy lamb, after all! She generously rewards henchmen who identify sources of inefficiency and come up with ways to remove them. You've spotted one such source, and you think solving it will help you build the reputation you need to get promoted.

Every time the Commander's employees pass each other in the hall, each of them must stop and salute each other - one at a time - before resuming their path. A salute is five seconds long, so each exchange of salutes takes a full ten seconds (Commander Lambda's salute is a bit, er, involved). You think that by removing the salute requirement, you could save several collective hours of employee time per day. But first, you need to show her how bad the problem really is.

Write a program that counts how many salutes are exchanged during a typical walk along a hallway. The hall is represented by a string. For example:
"--->-><-><-->-"

Each hallway string will contain three different types of characters: '>', an employee walking to the right; '<', an employee walking to the left; and '-', an empty space. Every employee walks at the same speed either to right or to the left, according to their direction. Whenever two employees cross, each of them salutes the other. They then continue walking until they reach the end, finally leaving the hallway. In the above example, they salute 10 times.

Write a function answer(s) which takes a string representing employees walking along a hallway and returns the number of times the employees will salute. s will contain at least 1 and at most 100 characters, each one of -, >, or <.

Python
======

Your code will run inside a Python 2.7.6 sandbox.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

Test cases
==========

Inputs:
    (string) s = ">----<"
Output:
    (int) 2

Inputs:
    (string) s = "<<>><"
Output:
    (int) 4
"""

def answer(s):

    right_arrow = '>'
    left_arrow = '<'
    empty_string = '-'

    input_list = list(s)

    arrow_list = [elm for elm in input_list if elm is not empty_string]

    arrow_dict = {'right': [], 'left': []}

    # Store positions of right arrows and left ones
    for i, elm in enumerate(arrow_list):

        if elm == right_arrow:
            arrow_dict['right'].append(i)

        if elm == left_arrow:
            arrow_dict['left'].append(i)

    r_encount = 0
    l_encount = 0

    for i, r_elm in enumerate(arrow_dict['right']):
        for j, l_elm in enumerate(arrow_dict['left']):
            if r_elm < l_elm:
                r_encount += 1

    for i, l_elm in enumerate(arrow_dict['left']):
        for j, r_elm in enumerate(arrow_dict['right']):
            if r_elm < l_elm:
                l_encount += 1

    return r_encount + l_encount


# s = ">----<"
# (int) 2

# s = "<<>><"
# (int) 4

s = "--->-><-><-->-"
# (int) 10
print answer(s)
