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

![LCS(X, Y) = LCS(X_{i-1}, Y_{j-1}) + X[i]](http://www.sciweavers.org/tex2img.php?eq=LCS%28X%2C%20Y%29%20%3D%20LCS%28X_%7Bi-1%7D%2C%20Y_%7Bj-1%7D%29%20%2B%20X%5Bi%5D&bc=Transparent&fc=Black&im=png&fs=12&ff=arev&edit=0)

## Case 2:
`X_i, Y_j` may have different endings in the sequence. We then wish to try and compute the LCS with each of `X` and `Y`'s last character removed, and then use the maximum length LCS of the two. That is:

	MAX(LCS(X     , Y ), LCS(X , Y     ))
	         i - 1   j        i   j - 1  

![MAX(LCS(X_{i-1}, Y_j), LCS(X_i, Y_{j-1}))](http://www.sciweavers.org/tex2img.php?eq=MAX%28LCS%28X_%7Bi-1%7D%2C%20Y_j%29%2C%20LCS%28X_i%2C%20Y_%7Bj-1%7D%29%29&bc=Transparent&fc=Black&im=png&fs=12&ff=arev&edit=0)

# Final Formulation

	LCS(X_i, Y_j) =
	\begin{cases}
		\phi							& \mbox{if } i = 0 \mbox{, or } j = 0 \\
		LCS(X_{i-1}, Y_{j-1}) + X[i]	& \mbox{if } X[i] = Y[j] \\
		MAX(LCS(X_{i-1}, Y_j), LCS(X_i, Y_{j-1})) & \mbox{if } X[i] \neq Y[j]
	\end{cases} 

![Final](http://www.sciweavers.org/tex2img.php?eq=%09LCS%28X_i%2C%20Y_j%29%20%3D%0A%09%5Cbegin%7Bcases%7D%0A%09%09%5Cphi%09%09%09%09%09%09%09%26%20%5Cmbox%7Bif%20%7D%20i%20%3D%200%20%5Cmbox%7B%2C%20or%20%7D%20j%20%3D%200%20%5C%5C%0A%09%09LCS%28X_%7Bi-1%7D%2C%20Y_%7Bj-1%7D%29%20%2B%20X%5Bi%5D%09%26%20%5Cmbox%7Bif%20%7D%20X%5Bi%5D%20%3D%20Y%5Bj%5D%20%5C%5C%0A%09%09MAX%28LCS%28X_%7Bi-1%7D%2C%20Y_j%29%2C%20LCS%28X_i%2C%20Y_%7Bj-1%7D%29%29%20%26%20%5Cmbox%7Bif%20%7D%20X%5Bi%5D%20%5Cneq%20Y%5Bj%5D%0A%09%5Cend%7Bcases%7D%20&bc=Transparent&fc=Black&im=png&fs=12&ff=arev&edit=0)