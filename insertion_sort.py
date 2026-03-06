"""
Insertion Sort
==============
Builds the sorted array one element at a time by inserting each
element into its correct position among the previously sorted elements.

Time Complexity: O(n²) worst/average, O(n) best (already sorted)
Space Complexity: O(1)
"""


def insertion_sort(arr):
    """
    Sort an array using Insertion Sort.

    Args:
        arr: list of comparable elements

    Returns:
        The sorted list (sorted in-place)
    """
    for i in range(1, len(arr)):
        key = arr[i]

        # Step 1: Compare key with each element to its left
        j = i - 1
        while j >= 0 and arr[j] > key:
            # Step 2: Shift larger elements one position to the right
            arr[j + 1] = arr[j]
            j -= 1

        # Step 3: Insert the key at its correct position
        arr[j + 1] = key

    return arr


# ── Example ──────────────────────────────────────────────────

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]

    print("=== Insertion Sort ===\n")
    print(f"Original array: {arr}")

    insertion_sort(arr)

    print(f"Sorted array:   {arr}")
