def sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: a list of 0 or 1 elements is already sorted

    mid = len(arr) // 2  # Find the middle index
    left = sort(arr[:mid])  # Recursively sort the left half
    right = sort(arr[mid:])  # Recursively sort the right half

    return _merge(left, right)  # Merge the two sorted halves


def _merge(left, right):
    result = []
    i = j = 0

    # Compare elements from left and right
    # and add the smaller one to result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements (if any) from left and right
    result.extend(left[i:])
    result.extend(right[j:])

    return result
