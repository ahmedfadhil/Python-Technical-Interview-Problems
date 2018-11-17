import statistics


# Finding the median metrix
def median_matrix(A):
    # if A is a vector
    if len(A) == 1:
        vec = A[0]
        print(statistics.median(vec))
        return vec[len(vec) // 2]

    else:
        new_list = []
        for row in range(len(A)):
            new_list.extend(A[row])
        new_list = sorted(new_list)
        print(statistics.median(new_list))
    return new_list[len(new_list) // 2]


if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [6, 5, 4]
    l3 = [0, 9, 2]

    A1 = [l1, l2, l3]
    A2 = [l1]
    print(median_matrix(A1))
    print(median_matrix(A2))

#
# # Using a Python function
#
# import statistics
#
# items = [1, 2, 3, 6, 8, 9]
#
# statistics.median(items)
# # >>> 3
