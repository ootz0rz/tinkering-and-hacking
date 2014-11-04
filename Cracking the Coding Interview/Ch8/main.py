def q4_1(n):
    '''
    Fibonacci:

    f(n) = f(n-1) + f(n-2)
    '''

    if n == 0:
        return 0

    if n == 1:
        return 1

    return q4_1(n-1) + q4_1(n-2)


def q4_3(s):
    '''
    All subsets of a set. S is given as a list of elements.

    Note for each element in the set, there are 2 choices (in or not in 
    subset), thus O(2^n) complexity
    '''

    if len(s) == 0:
        return [[]]

    out = []
    cur = s[0]

    for idx, e in enumerate(q4_3(s[1:])):
        out.append(e)
        out.append(e + [cur])

    return out

def q4_4(s):
    '''
    All permutations of a string.
    '''
    if len(s) <= 1:
        return [s]

    first = s[0]

    out = []
    for substr in q4_4(s[1:]):
        for idx, c in enumerate(substr):
            out.append(substr[:idx] + first + substr[idx:])

        out.append(substr + first)

    return out

def q4_5(n):
    '''
    Print all valid n-pairs of parenthesis.
    '''

    if n == 0:
        return ['']

    if n == 1:
        return ['()']

    out = []

    for sub in q4_5(n - 1):

        for i,a in enumerate(sub):

            for j,b in enumerate(sub[i:]):
                left = sub[:i]
                mid = sub[i:i+j]
                right = sub[i+j:]
                new = left + '(' + mid + ')' + right

                out.append(new)

            new = left + '(' + mid + right + ')'
            out.append(new)

    return list(set(out))