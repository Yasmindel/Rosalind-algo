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
    n = int(input("Enter the number of elements: "))
    arr = list(map(int, input("Enter the elements separated by spaces: ").split()))
    print("Number of swaps:", count_swaps_in_insertion_sort(arr))

if name == '__main__':
    main()
