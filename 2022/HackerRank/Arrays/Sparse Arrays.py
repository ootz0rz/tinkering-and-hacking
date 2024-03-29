# https://www.hackerrank.com/challenges/sparse-arrays/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#


def matchingStrings(stringList, queries):
    q = {}
    outarr = [0] * len(queries)

    for idx, query in enumerate(queries):
        if query not in q:
            q[query] = [idx]
        else:
            q[query].append(idx)

    for s in stringList:
        if s in q:
            for idx in q[s]:
                outarr[idx] = outarr[idx] + 1

    return outarr


if __name__ == "__main__":

    def process(s, q):
        strings = s.strip().split("\n")
        qs = q.strip().split("\n")

        print(s.strip().replace("\n", ", "), "|", q.strip().replace("\n", ","))
        print(matchingStrings(strings, qs))

    process(
        """
        def
        de
        fgh
        """,
        """
        de
        lmn
        fgh
        """,
    )

    process(
        """
lekgdisnsbfdzpqlkg
eagemhdygyv
jwvwwnrhuai
urcadmrwlqe
mpgqsvxrijpombyv
mpgqsvxrijpombyv
urcadmrwlqe
mpgqsvxrijpombyv
eagemhdygyv
eagemhdygyv
jwvwwnrhuai
urcadmrwlqe
jwvwwnrhuai
kvugevicpsdf
kvugevicpsdf
mpgqsvxrijpombyv
urcadmrwlqe
mpgqsvxrijpombyv
exdafbnobg
qhootohpnfvbl
suffrbmqgnln
exdafbnobg
exdafbnobg
eagemhdygyv
mpgqsvxrijpombyv
urcadmrwlqe
jwvwwnrhuai
lekgdisnsbfdzpqlkg
mpgqsvxrijpombyv
lekgdisnsbfdzpqlkg
jwvwwnrhuai
exdafbnobg
mpgqsvxrijpombyv
kvugevicpsdf
qhootohpnfvbl
urcadmrwlqe
kvugevicpsdf
mpgqsvxrijpombyv
lekgdisnsbfdzpqlkg
mpgqsvxrijpombyv
kvugevicpsdf
qhootohpnfvbl
lxyqetmgdbmh
urcadmrwlqe
urcadmrwlqe
kvugevicpsdf
lxyqetmgdbmh
urcadmrwlqe
lxyqetmgdbmh
jwvwwnrhuai
qhootohpnfvbl
qhootohpnfvbl
jwvwwnrhuai
lekgdisnsbfdzpqlkg
kvugevicpsdf
mpgqsvxrijpombyv
exdafbnobg
kvugevicpsdf
lekgdisnsbfdzpqlkg
qhootohpnfvbl
exdafbnobg
qhootohpnfvbl
exdafbnobg
mpgqsvxrijpombyv
suffrbmqgnln
mpgqsvxrijpombyv
qhootohpnfvbl
jwvwwnrhuai
mpgqsvxrijpombyv
qhootohpnfvbl
lekgdisnsbfdzpqlkg
eagemhdygyv
jwvwwnrhuai
kvugevicpsdf
eagemhdygyv
eagemhdygyv
lxyqetmgdbmh
qhootohpnfvbl
lxyqetmgdbmh
exdafbnobg
qhootohpnfvbl
qhootohpnfvbl
exdafbnobg
suffrbmqgnln
mpgqsvxrijpombyv
urcadmrwlqe
eagemhdygyv
lxyqetmgdbmh
urcadmrwlqe
suffrbmqgnln
qhootohpnfvbl
kvugevicpsdf
lekgdisnsbfdzpqlkg
lxyqetmgdbmh
mpgqsvxrijpombyv
jwvwwnrhuai
lxyqetmgdbmh
lxyqetmgdbmh
lekgdisnsbfdzpqlkg
qhootohpnfvbl
        """,
        """
exdafbnobg
eagemhdygyv
mpgqsvxrijpombyv
kvugevicpsdf
lekgdisnsbfdzpqlkg
kvugevicpsdf
exdafbnobg
qhootohpnfvbl
eagemhdygyv
kvugevicpsdf
suffrbmqgnln
jwvwwnrhuai
lekgdisnsbfdzpqlkg
lekgdisnsbfdzpqlkg
mpgqsvxrijpombyv
jwvwwnrhuai
kvugevicpsdf
lekgdisnsbfdzpqlkg
exdafbnobg
suffrbmqgnln
qhootohpnfvbl
eagemhdygyv
exdafbnobg
suffrbmqgnln
jwvwwnrhuai
qhootohpnfvbl
eagemhdygyv
exdafbnobg
exdafbnobg
jwvwwnrhuai
qhootohpnfvbl
lxyqetmgdbmh
qhootohpnfvbl
suffrbmqgnln
lxyqetmgdbmh
qhootohpnfvbl
eagemhdygyv
jwvwwnrhuai
eagemhdygyv
qhootohpnfvbl
mpgqsvxrijpombyv
qhootohpnfvbl
jwvwwnrhuai
exdafbnobg
eagemhdygyv
eagemhdygyv
kvugevicpsdf
kvugevicpsdf
jwvwwnrhuai
urcadmrwlqe
lxyqetmgdbmh
qhootohpnfvbl
exdafbnobg
exdafbnobg
eagemhdygyv
qhootohpnfvbl
exdafbnobg
exdafbnobg
lekgdisnsbfdzpqlkg
jwvwwnrhuai
eagemhdygyv
urcadmrwlqe
kvugevicpsdf
lekgdisnsbfdzpqlkg
jwvwwnrhuai
eagemhdygyv
lekgdisnsbfdzpqlkg
exdafbnobg
kvugevicpsdf
jwvwwnrhuai
exdafbnobg
lxyqetmgdbmh
exdafbnobg
lxyqetmgdbmh
jwvwwnrhuai
mpgqsvxrijpombyv
eagemhdygyv
urcadmrwlqe
kvugevicpsdf
qhootohpnfvbl
jwvwwnrhuai
eagemhdygyv
urcadmrwlqe
urcadmrwlqe
exdafbnobg
qhootohpnfvbl
exdafbnobg
eagemhdygyv
exdafbnobg
jwvwwnrhuai
eagemhdygyv
jwvwwnrhuai
mpgqsvxrijpombyv
urcadmrwlqe
urcadmrwlqe
eagemhdygyv
eagemhdygyv
jwvwwnrhuai
suffrbmqgnln
eagemhdygyv
        """,
    )
