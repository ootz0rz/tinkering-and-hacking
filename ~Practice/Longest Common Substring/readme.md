# Example
Let `X, Y` be two strings. For example:

	X = ABCD
	Y = DABC

Then the `LCS` is `ABC`

i.e. the largest substring

# Problem

Let `LCS(X, Y)` be the longest substring common to both `X, Y`

Let `X_i, Y_i` be the prefix of `X, Y` respectively such that `i, j` denotes the # of characters contained from the original string starting from the first element.

Ex: `X_2 = AB, Y_3 = DAB`

We begin by finding all the longest common suffix of every pair of substring prefixes `X_{1...n}` and `Y_{1...m}`, where `n, m` is the total length of each `X, Y` respectively. We'll call this operation LCSPrefix(X, Y). See formulation below.

We then wish to find the set of LCSPrefix elements with the maximum length.

That is, within the generated table, we wish to find:

	LCS(X, Y)  =  max    { LCSPrefix(X, Y) }
	                 len                    

![LCS(X, Y) = \max_{len} { LCSPrefix(X, Y) }](http://www.sciweavers.org/upload/Tex2Img_1367103862/eqn.png)

----

## LCSPrefix(X, Y)

We have two basic cases:

### Case 1:
	
`X[i] = Y[j]`, that is each string ends in the same character, and so we compute:

	LCSPrefix(X     , Y     )  +  X[i]
	           i - 1   j - 1          

![LCSPrefix(X_{i-1}, Y_{j-1}) + X[i]](http://www.sciweavers.org/upload/Tex2Img_1367102858/eqn.png)

### Case 2:

Simply ![the empty set](http://www.sciweavers.org/upload/Tex2Img_1367103021/eqn.png) otherwise.

### Final Formulation

So we compute the table:

	LCSPrefix(X, Y) = 
		\begin{cases}
			LCSPrefix(X_{i-1}, Y_{j-1}) + X[i]	& \mbox{if } X[i] = Y[j] \\
			\phi								& otherwise
		\end{cases}

![LCSPrefix Final Formulation](http://www.sciweavers.org/upload/Tex2Img_1367103516/eqn.png)

----