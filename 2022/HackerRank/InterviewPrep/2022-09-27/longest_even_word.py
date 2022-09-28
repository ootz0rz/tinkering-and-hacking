from glob import glob
from typing import List, Optional, Dict


def longestEvenWord(sentence):
    # the idea is that we're going to scan through
    # the string array, and keep track of the length
    # of each 'current' word as we go along.
    #
    # when we find a word that's even in length, we
    # check to see if its length is greater than the
    # last max... if so, that's our new longest word
    # and we can return it at the end
    N = len(sentence)

    # vars to track len during iteration
    i = 0
    cur_word_len = 0
    longest_len = 0

    # we want to store the start of the longest word
    # we've found, so we can reconstruct it later
    longest_start = None

    while i < N:

        if sentence[i] == " ":
            if cur_word_len % 2 == 0:
                # the last word was even... is it longer?
                if cur_word_len > longest_len:
                    longest_len = cur_word_len
                    longest_start = i - cur_word_len

            cur_word_len = 0
        else:
            cur_word_len = cur_word_len + 1

        i = i + 1

    # make sure to check the last word/result
    if cur_word_len % 2 == 0:
        # the last word was even... is it longer?
        if cur_word_len > longest_len:
            longest_len = cur_word_len
            longest_start = i - cur_word_len

    if longest_start is None:
        return "00"

    return sentence[longest_start : longest_start + longest_len]


if __name__ == "__main__":
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    sf = longestEvenWord
    check_solution_simple(
        sf,
        args=["It is a pleasant day today"],
        expected="pleasant",
    )

    check_solution_simple(
        sf,
        args=["You can do it the way you like"],
        expected="like",
    )
