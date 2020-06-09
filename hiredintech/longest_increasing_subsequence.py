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
    array_length = len(sequence)
    if array_length == 1:
        return sequence

    longest_seq = []

    for i in range(0,array_length):
        temp_seq = []
        temp_seq.append(sequence[i])
        for x in range(i,array_length):
            if temp_seq[-1] < sequence[x]:
                temp_seq.append(sequence[x])
        if len(longest_seq) < len(temp_seq):
            longest_seq = temp_seq

    return longest_seq


def longest_increasing_subsequence2(sequence):
    from collections import deque
    array_length = len(sequence)
    if array_length == 1:
        return sequence

    lower_index1 = 0
    upper_index1 = array_length - 1

    longest_inc_seq = deque()
    longest_dec_seq = deque()
    temp_inc_seq = deque()
    temp_dec_seq = deque()
    while lower_index1 < upper_index1:
        temp_inc_seq.clear()
        temp_dec_seq.clear()
        temp_inc_seq.append(sequence[lower_index1])
        temp_dec_seq.appendleft(sequence[upper_index1])

        for i in range(lower_index1,array_length):
            print(temp_inc_seq[-1],sequence[i])
            if temp_inc_seq[-1] < sequence[i]:
                temp_inc_seq.append(sequence[i])

        #     if temp_dec_seq[0] > sequence[array_length -(i+1)]:
        #         temp_dec_seq.appendleft(sequence[array_length -(i+1)])
        # print(temp_inc_seq, temp_dec_seq)


        # if len(longest_inc_seq) < len(temp_dec_seq):
        #     longest_inc_seq = temp_dec_seq.copy()
        if len(longest_inc_seq) < len(temp_inc_seq):
            longest_inc_seq = temp_inc_seq.copy()



        lower_index1 += 1
        upper_index1 -= 1



    return list(longest_inc_seq)



list1 = [0,1,2,43,4,45,6,10]
list2 = [11, 5, 4]
list3 = [1, 3, 3]

print(longest_increasing_subsequence2(list1))
# print(longest_increasing_subsequence2(list2))
# print(longest_increasing_subsequence2(list3))

