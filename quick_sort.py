"""
Quick Sort
==========
Divides the array using a pivot element, partitions elements
into two halves (less than and greater than pivot), and recursively
sorts each half.

Time Complexity: O(n log n) average, O(n²) worst case
Space Complexity: O(log n) average (recursion stack)
"""


def quick_sort(arr):
    """
    Sort an array using Quick Sort.

    Args:
        arr: list of comparable elements

    Returns:
        The sorted list (sorted in-place)
    """
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def _quick_sort(arr, low, high):
    """Recursively sort the subarray arr[low..high]."""
    if low < high:
        # Step 1: Partition the array and get pivot index
        pivot_idx = _partition(arr, low, high)

        # Step 2: Recursively sort elements before and after partition
        _quick_sort(arr, low, pivot_idx - 1)
        _quick_sort(arr, pivot_idx + 1, high)


def _partition(arr, low, high):
    """
    Lomuto partition scheme: choose last element as pivot,
    place pivot at its correct position, and place all smaller
    elements to the left, all greater to the right.
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ── Example ──────────────────────────────────────────────────

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]

    print("=== Quick Sort ===\n")
    print(f"Original array: {arr}")

    quick_sort(arr)

    print(f"Sorted array:   {arr}")
