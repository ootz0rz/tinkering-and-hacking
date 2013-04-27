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

![LCS(X, Y) = \max_{len} { LCSPrefix(X, Y) }](http://www.sciweavers.org/tex2img.php?eq=LCS%28X%2C%20Y%29%20%3D%20%5Cmax_%7Blen%7D%20%7B%20LCSPrefix%28X%2C%20Y%29%20%7D&bc=Transparent&fc=Black&im=png&fs=12&ff=arev&edit=0)

----

## LCSPrefix(X, Y)

We have two basic cases:

### Case 1:
	
`X[i] = Y[j]`, that is each string ends in the same character, and so we compute:

	LCSPrefix(X     , Y     )  +  X[i]
	           i - 1   j - 1          

![LCSPrefix(X_{i-1}, Y_{j-1}) + X[i]](http://www.sciweavers.org/tex2img.php?eq=LCSPrefix%28X_%7Bi-1%7D%2C%20Y_%7Bj-1%7D%29%20%2B%20X%5Bi%5D&bc=Transparent&fc=Black&im=png&fs=12&ff=arev&edit=0)

### Case 2:

Simply ![the empty set](http://www.sciweavers.org/tex2img.php?eq=%5Cphi&bc=Transparent&fc=Black&im=png&fs=12&ff=arev&edit=0) otherwise.

### Final Formulation

So we compute the table:

	LCSPrefix(X, Y) = 
		\begin{cases}
			LCSPrefix(X_{i-1}, Y_{j-1}) + X[i]	& \mbox{if } X[i] = Y[j] \\
			\phi								& otherwise
		\end{cases}

![LCSPrefix Final Formulation](http://www.sciweavers.org/tex2img.php?eq=%09LCSPrefix%28X%2C%20Y%29%20%3D%20%0A%09%09%5Cbegin%7Bcases%7D%0A%09%09%09LCSPrefix%28X_%7Bi-1%7D%2C%20Y_%7Bj-1%7D%29%20%2B%20X%5Bi%5D%09%26%20%5Cmbox%7Bif%20%7D%20X%5Bi%5D%20%3D%20Y%5Bj%5D%20%5C%5C%0A%09%09%09%5Cphi%09%09%09%09%09%09%09%09%26%20otherwise%0A%09%09%5Cend%7Bcases%7D&bc=Transparent&fc=Black&im=png&fs=12&ff=arev&edit=0)

----