def main():
    # Read the number of elements
    n = int(input("Enter the number of elements: "))
    # Read the elements into a list
    a = list(map(int, input("Enter the elements: ").split()))
    # Read the number of smallest elements to return
    k = int(input("Enter the number of smallest elements to display: "))
    
    # Sort the list and get the first k elements
    smallest_elements = sorted(a)[:k]
    
    # Print the result
    print(' '.join(map(str, smallest_elements)))

if name == '__main__':
    main()
