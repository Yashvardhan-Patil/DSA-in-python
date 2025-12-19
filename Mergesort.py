def merge(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)

    # Merge both halves
    while i < n and j < m:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    while i < n:
        result.append(left[i])
        i += 1

    while j < m:
        result.append(right[j])
        j += 1

    return result


def merge_s(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_s(arr[:mid])
    right_half = merge_s(arr[mid:])
    return merge(left_half, right_half)


# Example
n = [4, 2, 1, 6, 3]
print(merge_s(n))
