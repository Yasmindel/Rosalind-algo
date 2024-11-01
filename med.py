def partition(a):
    pivot = a[0]
    left, right = 0, len(a) - 1
    while left != right:
        while right != left and a[right] > pivot:
            right -= 1
        a[left], a[right] = a[right], a[left]
        while left != right and a[left] <= pivot:
            left += 1
        a[left], a[right] = a[right], a[left]
    return left

def find_kth_smallest_element(a, k):
    pos = partition(a)
    if pos == k - 1:
        return a[pos]
    elif pos < k - 1:
        return find_kth_smallest_element(a[pos + 1:], k - pos - 1)
    else:
        return find_kth_smallest_element(a[:pos], k)

def main():
    # Dataset directly included
    n = 11
    a = [2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1]
    k = 8
    print(find_kth_smallest_element(a, k))

if __name__ == '__main__':
    main()
