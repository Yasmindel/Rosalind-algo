def sift_down(heap, heap_size, index):
    while True:
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        if left_child < heap_size and heap[left_child] > heap[largest]:
            largest = left_child
        if right_child < heap_size and heap[right_child] > heap[largest]:
            largest = right_child
        if largest == index:
            break
        
        # Swap values
        heap[index], heap[largest] = heap[largest], heap[index]
        index = largest

def build_max_heap(heap):
    for i in range(len(heap) // 2 - 1, -1, -1):
        sift_down(heap, len(heap), i)

def heap_sort(arr):
    build_max_heap(arr)
    
    for heap_size in range(len(arr), 1, -1):
        arr[0], arr[heap_size - 1] = arr[heap_size - 1], arr[0]
        sift_down(arr, heap_size - 1, 0)

def main():
    num_elements = int(input("Enter the number of elements: "))
    elements = list(map(int, input("Enter the elements: ").split()))
    heap_sort(elements)
    print('Sorted elements:', ' '.join(map(str, elements)))

if name == '__main__':
    main()
