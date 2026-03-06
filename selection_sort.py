"""
Selection Sort
==============
Repeatedly finds the minimum element from the unsorted portion
and places it at the beginning.

Time Complexity: O(n²)
Space Complexity: O(1)
"""


def selection_sort(arr):
    """
    Sort an array using Selection Sort.

    Args:
        arr: list of comparable elements

    Returns:
        The sorted list (sorted in-place)
    """
    n = len(arr)

    for i in range(n):
        # Step 1: Find the index of the minimum element in unsorted portion
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Step 2: Swap the minimum element with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# ── Example ──────────────────────────────────────────────────

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]

    print("=== Selection Sort ===\n")
    print(f"Original array: {arr}")

    selection_sort(arr)

    print(f"Sorted array:   {arr}")
