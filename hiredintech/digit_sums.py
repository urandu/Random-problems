"""
Implement a program, which given an integer n, computes the sum of its digits.

If a negative number is given, the function should work as if it was positive.

For example, if n is 1325132435356, the digit's sum is 43. If n is -10, the sum is 1 + 0 = 1.

In the test cases for this task we will have that -2^63 < n < 2^63.

Test examples
Input	        Output
10	                1
2	                2
-3456	            18
1325132435356	    43


"""

def digit_sum(number):
    # Write your code here

    num = abs(number)
    num = str(num)
    length = len(num)
    top_total = 0
    bottom_total = 0
    low_index = 0
    upper_index = length - 1

    while low_index < upper_index:
        bottom_total += int(num[low_index])
        low_index += 1
        top_total += int(num[upper_index])
        upper_index -= 1

    if length % 2 == 0:
        return bottom_total + top_total
    return bottom_total + top_total + int(num[low_index])

print(digit_sum(35))