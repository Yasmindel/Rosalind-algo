def heapify(heap, i):
   
    if i == 0:
        return
    parent = (i - 1) // 2
    child = i
    if heap[parent] >= heap[child]:  # Maintain max-heap property
        return
    else:
        heap[parent], heap[child] = heap[child], heap[parent]
        heapify(heap, parent)
    
def hs():
    # Directly using the sample dataset
    n = 5
    A = [1, 3, 5, 7, 2]
    
    heap = []
    # Build the heap
    for i in range(len(A)):
        # Add element to the bottom level of the heap
        heap.append(A[i])
        # Heapify
        heapify(heap, i)
    # Print heap
    return ' '.join(map(str, heap))

if __name__ == "__main__":
    a = hs()
    print(a)  # Output to console for direct observation

