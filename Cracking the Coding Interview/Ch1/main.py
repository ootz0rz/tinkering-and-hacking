def q1_1(s):
    '''
    True iff there are no repeated characters in the given string s
    '''
    d = {}

    for c in s:
        if c in d:
            return False
        else:
            d[c] = 0

    return True

def q1_2(s, TERM='\0'):
    '''
    Reverse a c-style string.

    i.e. one that has a NULL terminator at the end (we'll use TERM to represent
    this)

    Assumes s is a list of characters.
    '''
    if len(s) < 2 or s[0] == TERM:
        return s

    import math

    # find end of string
    for idx, c in enumerate(s):
        if c == TERM:
            break
    s_end = idx - 1
    s_mid = math.floor(s_end / 2.)

    # swap characters in place
    i = 0
    j = s_end

    while j > s_mid:
        s[i], s[j] = s[j], s[i]
        j -= 1
        i += 1

    return s