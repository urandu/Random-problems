"""
Task: Longest increasing subsequence
Given a list of N integers find the longest increasing subsequence in this list.

Example
If the list is [16, 3, 5, 19, 10, 14, 12, 0, 15] one possible answer is the subsequence [3, 5, 10, 12, 15], another is [3, 5, 10, 14, 15].

If the list has only one integer, for example: [14], the correct answer is [14].

One more example: [10, 8, 6, 4, 2, 0], a possible correct answer is [8].

Test cases
Your solution will be graded against a number of test cases. All test cases contain at least one integer. Half of them will have no more than 1,000 integers in the input sequence. The other half will contain sequences with up to 10,000 integers.

You can design a solution, which works fast enough for N <= 1,000 but is slow for bigger inputs. Try and see how good of a solution you can create. Of course, aim to get the maximum possible points!


"""


def longest_increasing_subsequence(sequence):
    # Write your solution here

    low_index = 0
    high_index = 0

    temp_low_index = 0
    temp_high_index = 0

    size = len(sequence)
    # print(size)

    if size < 2:
        return sequence

    for i in range(0, size - 1):
        if sequence[i] < sequence[(i + 1)]:
            temp_high_index = i + 1
        else:
            temp_low_index = i + 1
            temp_high_index = i + 1
        if temp_low_index - temp_high_index <= low_index - high_index:
            high_index = temp_high_index
            low_index = temp_low_index
    return sequence[low_index:high_index + 1]


list = [1, 3, 2, 4, 5, 7]
list2 = [1]
list3 = [1, 3, 3]

print(longest_increasing_subsequence(list))
print(longest_increasing_subsequence(list2))
print(longest_increasing_subsequence(list3))

global maximum


def _lis(arr, n):
    global maximum

    # Base Case
    if n == 1:
        return 1

    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1

    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2] 
	IF arr[n-1] is maller than arr[n-1], and max ending with 
	arr[n-1] needs to be updated, then update it"""
    for i in range(1, n):
        res = _lis(arr, i)
        if arr[i - 1] < arr[n - 1] and res + 1 > maxEndingHere:
            maxEndingHere = res + 1

    # Compare maxEndingHere with overall maximum. And
    # update the overall maximum if needed
    maximum = max(maximum, maxEndingHere)

    return maxEndingHere


def lis(arr):
    n = len(arr)

    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    lis = [1] * n

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Initialize maximum to 0 to get the maximum of all
    # LIS
    maximum = 0

    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum


# Driver program to test the above function
arr = [1, 3, 2, 4, 5, 7]
n = len(arr)
print("Length of lis is ", lis(arr))

# This code is contributed by NIKHIL KUMAR SINGH
