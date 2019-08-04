
# def smallest_sort_window(arr):
#     sort_arr = sorted(arr)
#     left, right = None, None

#     for i in range(len(arr)):
#         if (arr[i] != sort_arr[i] and left is None):
#             left = i
#         elif(arr[i] != sort_arr[i]):
#             right = i
#     return left, right


# arr = [3, 7, 5, 6, 9]
# print(smallest_sort_window(arr))

def smallest_sort_window(arr):
    left, right = None, None
    max_seen, min_seen = -float("inf"), float("inf")
    n = len(arr)

    for i in range(n):
        max_seen = max(max_seen, arr[i])
        if(arr[i] < max_seen):
            right = i

    for i in range(n - 1, -1, -1):
        min_seen = min(min_seen, arr[i])
        if arr[i] > min_seen:
            left = i
    return left, right


arr = [3, 7, 5, 6, 9]
print(smallest_sort_window(arr))
