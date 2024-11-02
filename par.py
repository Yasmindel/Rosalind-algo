def par():
    # Predefined dataset
    A = [7, 2, 5, 6, 1, 3, 9, 4, 8]  # Elements of the array
    
    # Initialize lists to hold the results
    B = []
    
    # Separate elements based on a custom condition
    for num in A:
        if num < 7:  # Since 7 is the first number and we want numbers less than it first
            B.append(num)
    
    # Add the first number (7)
    B.append(7)
    
    # Add the remaining numbers greater than 7 in sorted order
    for num in A:
        if num > 7:
            B.append(num)

    return ' '.join(map(str, B))

if __name__ == "__main__":
    a = par()
    with open('output_par.txt', 'w') as g:
        g.write(a)

