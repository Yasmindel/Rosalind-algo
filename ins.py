# Embedded input
n = 6
lst = [6, 10, 4, 5, 1, 2]

count = 0
for i in range(1, len(lst)):
    k = i
    while k > 0 and lst[k] < lst[k - 1]:
        # Swap the elements
        lst[k - 1], lst[k] = lst[k], lst[k - 1]
        count += 1
        k -= 1

# Output the number of swaps
print(count)
