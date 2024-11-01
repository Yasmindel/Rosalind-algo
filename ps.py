def main():
    # Number of elements in the list
    n = 10
    # Elements in the list
    a = [4, -6, 7, 8, -9, 100, 12, 13, 56, 17]
    # Number of smallest elements to return
    k = 3
    
    # Sort the list and get the first k smallest elements
    smallest_elements = sorted(a)[:k]
    
    # Print the result
    print(' '.join(map(str, smallest_elements)))

if __name__ == '__main__':
    main()
