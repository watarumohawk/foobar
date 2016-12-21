# -*- coding: utf-8 -*-
"""
Don't Get Volunteered!
======================

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and capturing bunnies at the same time, after all! In order to make sure that everyone working for her is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called answer(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) src = 19
    (int) dest = 36
Output:
    (int) 1

Inputs:
    (int) src = 0
    (int) dest = 1
Output:
    (int) 3


constraints.txt: Python
======

Your code will run inside a Python 2.7.6 sandbox.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.
"""
board_size = 8

def find_my_coordinate(num):
    # 座標は自然数

    coordinate = {}

    x = (num % board_size) + 1
    y = board_size - (num / board_size)

    coordinate['x'] = int(x)
    coordinate['y'] = int(y)

    return coordinate

def find_my_node_id(x, y):

    return (board_size - y) * board_size + x - 1

def generate_legal_moves(x, y):

    new_moves = []
    move_offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    for i in move_offsets:
        new_x = x + i[0]
        new_y = y + i[1]

        if legal_coord(new_x, board_size) and legal_coord(new_y, board_size):
            new_moves.append((new_x, new_y))

    return new_moves

def legal_coord(x, board_size):

    if x >= 1 and x <= board_size:
        return True
    else:
        return False

def answer(src, dest):

    src_coordinate = find_my_coordinate(src)
    dest_coordinate = find_my_coordinate(dest)

    print 'Source: ', src_coordinate
    print 'Destination: ', dest_coordinate

    print generate_legal_moves(src_coordinate['x'], src_coordinate['y'])




    # if dest_coordinate in genarate_legal_moves(src_coordinate['x'], src_coordinate['y']):
    #
    # # if dest_coordinate in make_possible_coordinate(src_coordinate):
    #     print 'Found it!'
    #     return 1
    #     # 1回目で発見
    # else:
    #     print "Couldn't find it!"
    #     # 見つからなかったらもう一回探す

# Inputs:
src = 19
dest = 36
# Output: 1

# Inputs:
# src = 0
# dest = 1
# Output: 3

print answer(src, dest)