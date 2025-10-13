def sort(arr):
    a = arr[:]             # Make a copy of the list to avoid modifying the original
    n = len(a)             # Get the number of elements

    # Outer loop for each pass through the array
    for i in range(n - 1):
        # Inner loop for comparing adjacent elements
        for j in range(n - i - 1):
            # Swap if the current element is greater than the next one
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a               # Return the sorted list
