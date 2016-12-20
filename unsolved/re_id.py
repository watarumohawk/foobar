# -*- coding: utf-8 -*-
"""
There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning everyone new, random IDs based on her Completely Foolproof Scheme.

She's concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number from a hat. That number is the starting index in that string of primes, and the minion's new ID number will be the next five digits in the string. So if a minion draws "3", their ID number will be "71113".

Help the Commander assign these IDs by writing a function answer(n) which takes in the starting index n of Lambda's string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.

Languages
=========

Inputs:
    (int) n = 0
Output:
    (string) "23571"

Inputs:
    (int) n = 3
Output:
    (string) "71113"

"""
import re

def generate_prime(max_range):
    seed = list(range(2, max_range))
    while not len(seed) == 0:
        top = seed.pop(0)
        yield top
        seed = [i for i in seed if not i % top == 0]


def answer(n):

    prime_list = list(generate_prime(2000))
    primal_num = ''

    for prime in prime_list:
        primal_num += str(prime)

    new_id = ''

    print '~~~~~~ %d ~~~~~~' % n

    if n == 0:
        primal_num = primal_num.replace('23571', '')
        return '23571'
    else:
        prefix_num = 5 - len(str(n))

        pattern = re.compile(r'\d{%d}%d' % (prefix_num, n))
        match = pattern.findall(primal_num)

        if match:
            print 'match: ', match

            locals()
            primal_num = primal_num.replace(match[0], '')

            if match[0] == '23571':
                new_id = match[1]
            else:
                new_id = match[0]

                # 切り取った数字は list に格納
                # その list 内に match[0] があるか判定
                # あれば、match[1] を取得。while か何かで increment する


        else:
            print 'Did not find'

    return new_id


# n = 0
# '23571

n = 3
# '71113'

for n in range(72):
    print answer(n)


