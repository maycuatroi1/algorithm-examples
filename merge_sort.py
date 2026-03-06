"""
Merge Sort
==========
Divides the array into two halves, recursively sorts each half,
then merges the two sorted halves back together.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""


def merge_sort(arr):
    """
    Sort an array using Merge Sort.

    Args:
        arr: list of comparable elements

    Returns:
        The sorted list (sorted in-place)
    """
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Step 2: Recursively sort each half
    merge_sort(left)
    merge_sort(right)

    # Step 3: Merge the two sorted halves back into arr
    _merge(arr, left, right)

    return arr


def _merge(arr, left, right):
    """Merge two sorted arrays into arr."""
    i = j = k = 0

    # Compare elements from both halves and place the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


# ── Example ──────────────────────────────────────────────────

if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]

    print("=== Merge Sort ===\n")
    print(f"Original array: {arr}")

    merge_sort(arr)

    print(f"Sorted array:   {arr}")
