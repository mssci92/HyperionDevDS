
def minesweeper(grid): # defines function 
    rows = len(grid) # finds number of rows using len() function
    cols = len(grid[0]) # finds number of columns using len() function
    for i, row in enumerate(grid): # using nested loop to iterate through columns and rows
        for j, cell in enumerate(row):
            if cell == '-': # checks position of dash 
                count = 0 # assigns '-' to value of 0
                for x in range(max(0, i-1), min(rows, i+2)): # using nested loop to iterate through adjacent positions using range to place current range min and max function so current position is starting point as it was assigned at value 0
                    for y in range(max(0, j-1), min(cols, j+2)): # used https://realpython.com/python-min-and-max/ on how to use max and min function
                        if grid[x][y] == '#': # checks if adjacent positions contains a '#'
                            count += 1 # if '#' found then the value of count increases by 1 each time
                grid[i][j] = str(count) # converts count variable to string to replace all '-' with count value
    return grid # returns new grid

grid = [
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]


print(minesweeper(grid)) #prints new grid showing '-' as values of how many adjacent '#' located around

