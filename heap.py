

import heapq

def max_heapify(arr, n, i):
    largest = i  # Assume root is largest
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and heapify the subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        max_heapify(arr, n, largest)  # Heapify the affected subtree

def min_heapify(arr, n, i):
    smallest = i  # Assume root is smallest
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child is smaller than root
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # Check if right child is smaller than smallest so far
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # If the smallest element is not the root, swap and heapify
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # Swap
        min_heapify(arr, n, smallest)  # Recursively heapify the affected subtree



def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap max element with last element
        max_heapify(arr, i, 0)  # Heapify the reduced heap

def char_counter(arr):
    count = 0
    for i in range(len(arr)):
        count += 1
    return count


# Example usage