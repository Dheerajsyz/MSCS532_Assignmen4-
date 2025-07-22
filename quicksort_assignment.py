"""
quicksort_assignment.py
Minimalist implementation for deterministic and randomized Quicksort, with empirical analysis and documentation.
"""
import random
import time
import sys
sys.setrecursionlimit(20000)  # Increase recursion limit for empirical testing

def quicksort(arr):
    """Deterministic Quicksort: sorts arr in place using last element as pivot."""
    def _quicksort(a, low, high):
        if low < high:
            p = partition(a, low, high)
            _quicksort(a, low, p - 1)
            _quicksort(a, p + 1, high)
    def partition(a, low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1
    _quicksort(arr, 0, len(arr) - 1)

def randomized_quicksort(arr):
    """Randomized Quicksort: sorts arr in place using a random pivot."""
    def _quicksort(a, low, high):
        if low < high:
            p = randomized_partition(a, low, high)
            _quicksort(a, low, p - 1)
            _quicksort(a, p + 1, high)
    def randomized_partition(a, low, high):
        pivot_index = random.randint(low, high)
        a[pivot_index], a[high] = a[high], a[pivot_index]
        return partition(a, low, high)
    def partition(a, low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1
    _quicksort(arr, 0, len(arr) - 1)

def generate_input(size, distribution):
    if distribution == 'random':
        return [random.randint(0, size) for _ in range(size)]
    elif distribution == 'sorted':
        return list(range(size))
    elif distribution == 'reverse':
        return list(range(size, 0, -1))
    else:
        raise ValueError('Unknown distribution')

def time_sort(sort_fn, arr):
    arr_copy = arr.copy()
    start = time.perf_counter()
    sort_fn(arr_copy)
    end = time.perf_counter()
    return end - start

def empirical_analysis():
    sizes = [1000, 5000, 10000]
    distributions = ['random', 'sorted', 'reverse']
    print(f"{'Size':>6} | {'Dist':>8} | {'Deterministic':>15} | {'Randomized':>12}")
    print('-'*55)
    for size in sizes:
        for dist in distributions:
            arr = generate_input(size, dist)
            t_det = time_sort(quicksort, arr)
            t_rand = time_sort(randomized_quicksort, arr)
            print(f"{size:6} | {dist:>8} | {t_det:15.6f} | {t_rand:12.6f}")

if __name__ == "__main__":
    # Example usage and empirical analysis
    arr = [10, 7, 8, 9, 1, 5]
    print("Original array:", arr)
    quicksort(arr)
    print("Deterministic Quicksort:", arr)
    arr2 = [10, 7, 8, 9, 1, 5]
    randomized_quicksort(arr2)
    print("Randomized Quicksort:", arr2)
    print("\nEmpirical Analysis:")
    empirical_analysis() 