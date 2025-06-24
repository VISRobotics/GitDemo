"""Simple bubble sort implementation."""
from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    a = arr[:]
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

if __name__ == "__main__":
    sample = [5, 1, 4, 2, 8]
    print(bubble_sort(sample))
