# is palindrome

def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
            continue

        if s[i] != s[j]:
            return False
    
    return True

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    check_solution_simple(is_palindrome, args=[""], expected=True)
    check_solution_simple(is_palindrome, args=["a"], expected=True)
    check_solution_simple(is_palindrome, args=["aa"], expected=True)
    check_solution_simple(is_palindrome, args=["aba"], expected=True)
    check_solution_simple(is_palindrome, args=["abc"], expected=False)
    check_solution_simple(is_palindrome, args=["acaa"], expected=False)
    check_solution_simple(is_palindrome, args=["aaca"], expected=False)
    check_solution_simple(is_palindrome, args=["daac"], expected=False)