# 2D lists and nested loops

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0])  # --> [1, 2, 3]
print(number_grid)  # --> [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]
print(number_grid[1][2])  # ---> 6

for i in number_grid:
    for y in i:
        print(y)  # --> prints out all the numbers inside the list

