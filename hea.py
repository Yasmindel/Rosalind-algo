def create_max_heap(elements):
    # Start from the last parent node and move upwards
    for i in range((len(elements) - 2) // 2, -1, -1):
        heapify(elements, i)

def heapify(elements, index):
    largest = index
    left_child = 2 * index + 1  # left child index
    right_child = 2 * index + 2  # right child index

    # Check if left child exists and is greater than the current largest
    if left_child < len(elements) and elements[left_child] > elements[largest]:
        largest = left_child

    # Check if right child exists and is greater than the current largest
    if right_child < len(elements) and elements[right_child] > elements[largest]:
        largest = right_child

    # If largest is not the root, swap and continue heapifying
    if largest != index:
        elements[index], elements[largest] = elements[largest], elements[index]
        heapify(elements, largest)

def main():
    # Given input
    count = 5  # Number of elements
    numbers = [1, 3, 5, 7, 2]  # The elements to be heapified
    
    create_max_heap(numbers)
    
    # Print the max heap structure as required
    print(' '.join(map(str, numbers)))

if name == '__main__':
    main()
