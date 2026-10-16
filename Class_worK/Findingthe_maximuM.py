def find_max(my_list):
    max_value = my_list[0][0]
    for row in my_list:
        for element in row:
            if element > max_value:
                max_value = element
    return max_value

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
max_value = find_max(my_list)
print("The maximum value is:", max_value) 