"""
Bubble Sort
===========
Repeatedly steps through the list, compares adjacent elements,
and swaps them if they are in the wrong order.

Time Complexity: O(n²) worst/average, O(n) best (already sorted, with optimization)
Space Complexity: O(1)
"""


def bubble_sort(arr):
    """
    Sort an array using Bubble Sort.

    Args:
        arr: list of comparable elements

    Returns:
        The sorted list (sorted in-place)
    """
    n = len(arr)

    for i in range(n):
        swapped = False

        # Step 1: Compare adjacent elements and swap if needed
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Step 2: If no swaps occurred, array is already sorted
        if not swapped:
            break

    return arr


# ── Example ──────────────────────────────────────────────────

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    print("=== Bubble Sort ===\n")
    print(f"Original array: {arr}")

    bubble_sort(arr)

    print(f"Sorted array:   {arr}")
