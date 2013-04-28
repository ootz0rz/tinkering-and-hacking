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

Basically what we do is, for each combination of cuts we compute, we assign some weight... and we use the solution with the smallest weight.

In more detail...

Note that the maximum number of unique cuts for any string `S`, is `len(s) - 1`. 

	MaxCuts(S)  =  len(S)  -  1  =  {s , s , s , ..., s }
	                                  1   2   3        n 

![MaxCuts(S) = len(S) - 1 = \{s_1, s_2, s_3, \ldots, s_n\}](http://www.sciweavers.org/tex2img.php?eq=MaxCuts%28S%29%20%3D%20len%28S%29%20-%201%20%3D%20%5C%7Bs_1%2C%20s_2%2C%20s_3%2C%20%5Cldots%2C%20s_n%5C%7D&bc=Transparent&fc=Black&im=png&fs=12&ff=arev&edit=0)

We basically go through MaxCuts(S) and remove `1` cut at a time, and check to see if it's a valid solution. If it is, we keep the current solution and then remove `1` cut further along (if possible) and validate. We continue this until we've calculated all valid solution(s).

We then do the same, but removing `2` consecutive cuts at a time. Then `3` and so on until we've removed all cuts. The valid solution with the least number of cuts remaining is our final answer.

This process gives us MinCuts(S)

# Formulations

## MinCuts(S)

Let `i, j` be the starting and ending index of a substring in S.

Let `i = 0`, `j = len(s) - 1`

We then define `MinCuts(S, i, j)` as the minimum number of cuts in the substring `S[i:j]`.



## SubPalindromes(S)

3 main cases:

## ISP(x)

ISP(x) -> True iff x == reverse(x)

```python
def ISP(x):
	return x == x[::-1]
```