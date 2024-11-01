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

def merge_and_sort(arr1, arr2):
    # Combine the two arrays
    combined = arr1 + arr2
    # Sort the combined array using insertion sort
    count_swaps_in_insertion_sort(combined)
    return combined

def main():
    # Sample dataset
    arr1 = [2, 4, 10, 18]  # First dataset
    arr2 = [-5, 11, 12]    # Second dataset

    # Merge and sort both arrays
    sorted_array = merge_and_sort(arr1, arr2)
    print(' '.join(map(str, sorted_array)))

if __name__ == '__main__':
    main()
