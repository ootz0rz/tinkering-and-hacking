# Problem Definition

Basically, you're given a string, and you want to split it into as few strings as possible such that each string is a palindrome.

## Example 1

`S = "ABCBD"`
This can be split into: `[A, BCB, D]`

Note that single letter strings are considered palindromes.

## Example 2

`S = ABCBADEDFG`
This can be split into: `[ABCBA, DED, F, G]`

# Idea

First, we'll preprocess our string `S` to find all palindromes.

Let `ISP(x) -> True` iff string `x` is a palindrome.

We construct a table `M[i][j]` such that `M[i][j] = True` iff `ISP(S[i:j]) = True`

That is...

	SubPalindromes(S) = M[i][j] = ISP(S[i:j])

This table can be constructed in `O(n^2)` time, and can then be used for `O(1)` look ups later.

We then construct a second table, `C[m][n]` such that:

	C[m][n] = MinCuts(S[m:n])

Where `MinCuts(S[m:n])` is the mininum cuts for the substring of `S`, between index `m` to `n`.

Our final answer would be `C[0][n]`, `n = len(S) - 1`

# Formulations

## MinCuts(S)

## SubPalindromes(S)

3 main cases:

## ISP(x)

ISP(x) -> True iff x == reverse(x)