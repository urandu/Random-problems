"""
Task: Numeric Palindromes
A palindrome is а word or a phrase or a number, that when reversed, stays the same.

For example, the following sequences are palindromes : "azobi4amma4iboza" or "anna".

But this time, we are not interested in words but numbers. A "number palindrome" is a number, that taken backwards, remains the same.

For example, the numbers 1, 4224, 9999, 1221 are number palindromes.

Implement a function, which given an integer computes if it's a palindrome.

Input
One integer n, where 0 < n <= 10,000,000,000.

Output
Your function must return a boolean true if n is a palindrome and false otherwise.

Test examples
Input	        Output
1	            true
42	            false
100001	        true
999	            true
123	            false



"""

def is_numeric_palindrome(n):
    # Write your code here

    num = abs(n)
    num = str(num)
    length = len(num)
    if length == 1:
        return True

    low_index = 0
    upper_index = length - 1

    while low_index < upper_index:

        if num[low_index] != num[upper_index]:
            return False
        low_index += 1
        upper_index -= 1

    return True

print(is_numeric_palindrome(353))