"""
Heap Sort
=========
Builds a max-heap from the array, then repeatedly extracts the
maximum element and places it at the end of the sorted portion.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""


def heap_sort(arr):
    """
    Sort an array using Heap Sort.

    Args:
        arr: list of comparable elements

    Returns:
        The sorted list (sorted in-place)
    """
    n = len(arr)

    # Step 1: Build a max-heap (start from last non-leaf node)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    # Step 2: Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root (max) to end
        arr[0], arr[i] = arr[i], arr[0]

        # Heapify the reduced heap
        _heapify(arr, i, 0)

    return arr


def _heapify(arr, n, i):
    """
    Maintain the max-heap property for the subtree rooted at index i.

    Args:
        arr: the array
        n: size of the heap
        i: index of the root of the subtree
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)


# ── Example ──────────────────────────────────────────────────

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]

    print("=== Heap Sort ===\n")
    print(f"Original array: {arr}")

    heap_sort(arr)

    print(f"Sorted array:   {arr}")
