num_pad = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ["*", 0, "#"]]

# Outer loop: runs after a complete run of the inner (row)
for row in num_pad:

    # Inner loop: runs though every character in the current row
    for x in row:
        # 'end=" "' keeps the keys onthe same line seperated by a space
        print(x, end=" ")
    # Runs after every row ti move to the next line    
    print()