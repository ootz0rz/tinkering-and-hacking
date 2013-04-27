# Example
Let `X, Y` be two sequences of characters. For example:

	X = {A, C, B, D, E, G, C, E, D, B, G}
	Y = {B, E, G, C, F, E, U, B, K}

Then the `LCS` is `{B, E, G, C, E, B}`

i.e. the largest consecutive 

# Problem

Let `LCS(X, Y)` be the longest subsequence common to both `X, Y`

Let `X_i, Y_i` be the prefix of `X, Y` respectively such that `i, j` denotes the # of characters contained from the original sequence starting from the first element.

Ex: `X_2 = {A, C}, Y_3 = {B, E, G}`

We have two basic cases...

## Case 1:
`X_i, Y_j` end in the same character. Therefore, the last character (i.e. `X[i]` and `Y[j]`) is a part of the LCS. Thus we can compute the LCS as:

	LCS(X, Y)  =  LCS(X     , Y     )  +  X[i]
	                   i - 1   j - 1          

![LCS(X, Y) = LCS(X_{i-1}, Y_{j-1}) + X[i]](http://www.sciweavers.org/upload/Tex2Img_1367099812/eqn.png)

## Case 2:
`X_i, Y_j` may have different endings in the sequence. We then wish to try and compute the LCS with each of `X` and `Y`'s last character removed, and then use the maximum length LCS of the two. That is:

	MAX(LCS(X     , Y ), LCS(X , Y     ))
	         i - 1   j        i   j - 1  

![MAX(LCS(X_{i-1}, Y_j), LCS(X_i, Y_{j-1}))](http://www.sciweavers.org/upload/Tex2Img_1367099737/eqn.png)

# Final Formulation

	LCS(X_i, Y_j) =
	\begin{cases}
		\phi							& \mbox{if } i = 0 \mbox{, or } j = 0 \\
		LCS(X_{i-1}, Y_{j-1}) + X[i]	& \mbox{if } X[i] = Y[j] \\
		MAX(LCS(X_{i-1}, Y_j), LCS(X_i, Y_{j-1})) & \mbox{if } X[i] \neq Y[j]
	\end{cases} 

![Final](http://www.sciweavers.org/upload/Tex2Img_1367099598/eqn.png)