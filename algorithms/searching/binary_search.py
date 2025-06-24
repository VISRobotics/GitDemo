"""Binary search implementation."""
from typing import List, Optional

def binary_search(arr: List[int], target: int) -> Optional[int]:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

if __name__ == "__main__":
    sample = [1, 2, 4, 5, 8]
    print(binary_search(sample, 5))
