def partition(arr):
    pivot = arr[0]
    left, right = 0, len(arr) - 1
    while left < right:
        while left < right and arr[right] > pivot:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]
    arr[left] = pivot
    return left

def find_kth_smallest(arr, k):
    pos = partition(arr)
    if pos == k - 1:
        return arr[pos]
    elif pos < k - 1:
        return find_kth_smallest(arr[pos + 1:], k - pos - 1)
    else:
        return find_kth_smallest(arr[:pos], k)

def main():
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").split()))
    k = int(input("Enter k (1-based index): "))
    print("The", k, "th smallest element is:", find_kth_smallest(arr, k))

if name == '__main__':
    main()
