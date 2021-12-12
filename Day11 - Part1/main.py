def draw_grid(grid):
    print("-------------------------")
    for row in grid:
        print(row)
    print("-------------------------")

def increase(grid):
    new_grid=[]
    for row in grid:
        new_row=[value+1 for value in row]
        new_grid.append(new_row)
    return new_grid

def set_flashed_to_zero(grid):
    new_grid=[]
    for row in grid:
        new_row=[0 if value>9 else value for value in row]
        new_grid.append(new_row)
    return new_grid

def flash_octopus(grid,already_flased):
    new_flashed=[]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            value=grid[i][j]
            if value>9 and [i,j] not in already_flased:
                # print(f"Found flashing {i},{j}")
                new_flashed.append([i,j])
                adjacents = get_adjacents([i,j])
                # print(f"found adjacents {adjacents}")
                for adjacent in adjacents:
                    grid[adjacent[0]][adjacent[1]]+=1
    return grid,new_flashed

def get_adjacents(position):
    adjacents=[]
    for i in range(position[0]-1,position[0]+1+1):
        for j in range(position[1]-1,position[1]+1+1):
            # print(f"{i},{j}")
            if i>=0 and j>=0 and i<=9 and j<=9:
                adjacents.append([i,j])
    return adjacents

f = open("input.txt", "r")
lines = f.readlines()

steps=100

grid=[]
for line in lines:
    row=[int(value) for value in line[:-1]]
    grid.append(row)

draw_grid(grid)
count_flashed=0
for i in range(steps):
    flashed=[]
    # First step
    grid=increase(grid)
    # print("After increase")
    # draw_grid(grid)
    # print("End of increase")
 
    # Second step
    end_flashing=False
    flashed=[]
    while not end_flashing:
        grid,new_flashed=flash_octopus(grid,flashed)
        # print("Step of flashing")
        # draw_grid(grid)
        # print("End of step of flashing")
        if len(new_flashed)==0:
            end_flashing=True
        else:
            for position in new_flashed:
                flashed.append(position)
    count_flashed+=len(flashed)

    # Third step
    grid=set_flashed_to_zero(grid)
    # print("After set to zero")
    # draw_grid(grid)
    # print("After set to zero")

    print(f"Grid after {i+1} steps")
    draw_grid(grid)

print(f"There have been {count_flashed} flashed octopus")