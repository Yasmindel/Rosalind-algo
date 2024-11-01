def count_swaps_in_insertion_sort(arr):
    swaps = 0
    for i in range(1, len(arr)):
        current = i
        while current > 0 and arr[current] < arr[current - 1]:
            # Swap the elements
            arr[current], arr[current - 1] = arr[current - 1], arr[current]
            swaps += 1
            current -= 1
    return swaps

def main():
    # Input: number of elements
    n = int(input())  # Read the number of elements
    # Input: elements of the array
    arr = list(map(int, input().split()))
    
    # Count swaps and sort the array
    swap_count = count_swaps_in_insertion_sort(arr)
    
    # Output: number of swaps and the sorted array
    print(swap_count)  # Output just the number of swaps

if __name__ == '__main__':
    main()
