def sort(arr):
    a = arr[:]  # Make a copy of the list

    # Start from the second element (index 1)
    for i in range(1, len(a)):
        key = a[i]   # The element to be inserted into the sorted part
        j = i - 1    # Index of the last element in the sorted part

        # Move elements of the sorted part
        # that are greater than key one position ahead
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        # Insert the key at its correct position
        a[j + 1] = key

    return a  # Return the sorted list
