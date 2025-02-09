maze = [
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
]

direction = [(0,1),(0,-1),(-1,0),(1,0)]  # Right, Left, Up, Down

start = (0,0) 

row = len(maze)

col = len(maze[0])

end = (row-1, col-2)

path = [(0,0)]     # Stack

while path:              # While stack is not empty


    temp = list(path)

    (x,y) = path.pop()

    if (x,y) == end:

        print("The Path: ",path)
        break

    maze[x][y] = 0   # Mark as visited

    for dx, dy in direction:    # This loop is to add all the possible directoin in the stack.

        nx = x + dx      # for checking the nearby cells using the direction
        ny = y + dy

        if 0 <= nx < row and 0 <= ny < col and maze[nx][ny] == 1:

            path = temp + [(nx,ny)]
    
else:

    print("No path found")



# when reaching a dead end the if condition wont satisfy, hencing back tracking until a path or the junction is found