maze = [
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

tm = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

points = []  # to track junctions

row, col = 0, 1  # Start position

def check():
    global row, col, points, maze, tm

    option = {"up": 0, "down": 0, "right": 0, "left": 0}
    count = 0

    tm[row][col] = 1  # Mark current position as visited

    if col < 9 and maze[row][col + 1] == 1 and tm[row][col + 1] != 1:  # Right
        option["right"] = 1
        count += 1

    if col > 0 and maze[row][col - 1] == 1 and tm[row][col - 1] != 1:  # Left
        option["left"] = 1
        count += 1

    if row > 0 and maze[row - 1][col] == 1 and tm[row - 1][col] != 1:  # Up
        option["up"] = 1
        count += 1

    if row < 9 and maze[row + 1][col] == 1 and tm[row + 1][col] != 1:  # Down
        option["down"] = 1
        count += 1

    if count > 1:  # Junction point
        points.append((row, col, option))

    if count == 0:  # Dead end, backtrack
        if points:
            row, col, option = points.pop()
        else:
            print("No solution found")
            exit()  # Stop execution if no path

while True:
    check()

    if row == 9:  # Reached the last row
        print("Path found!")
        break

    if points:
        _, _, option = points[-1]  # Get last junction's option

        if option["right"]:
            col += 1
            option["right"] = 0
        elif option["left"]:
            col -= 1
            option["left"] = 0
        elif option["up"]:
            row -= 1
            option["up"] = 0
        elif option["down"]:
            row += 1
            option["down"] = 0

    tm[row][col] = 1
    print(row, col)  # Print the path taken