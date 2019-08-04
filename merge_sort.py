
def merge_lists(leftArr, rightArr):
    leftLength = len(leftArr)
    rightLength = len(rightArr)
    mergedArray = [None] * (leftLength + rightLength)
    mergedLength = len(mergedArray)

    L, R, C = 0, 0, 0

    while(C < mergedLength):
        while(L < leftLength and R < rightLength):
            leftValue, rightValue = leftArr[L], rightArr[R]
            if (leftValue <= rightValue):
                mergedArray[C] = leftValue
                L += 1
            else:
                mergedArray[C] = rightValue
                R += 1

            C += 1

        if (L < leftLength):
            mergedArray[C:] = leftArr[L:]
        else:
            mergedArray[C:] = rightArr[R:]

        C = mergedLength

    return mergedArray


def merge_multiple_lists(*args):
    merged_array = [None] * sum([len(x) for x in args])
    for ind, arg in enumerate(args):
        if(ind == 0):
            merged_array = arg
        else:
            merged_array = merge_lists(merged_array, arg)

    return merged_array


my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
new_list = [0, 2]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_multiple_lists(my_list, alices_list, new_list))
