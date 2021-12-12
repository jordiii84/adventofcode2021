def get_is_minimum(map, position):
    x=position[0]
    y=position[1]

    traveled_positions=[]
    is_minimum=True

    adjacents=[]
    if x>0:
        adjacents.append([x-1,y])
    if x<(len(map)-1):
        adjacents.append([x+1,y])
    if y>0:
        adjacents.append([x,y-1])
    if y<(len(map[0])-1):
        adjacents.append([x,y+1])

    for adjacent in adjacents:
        adjx=adjacent[0]
        adjy=adjacent[1]
        if map[adjx][adjy]<=map[x][y]:
            is_minimum=False
        else:
            traveled_positions.append([adjx,adjy])


    return is_minimum,traveled_positions

f = open("input.txt", "r")
lines = f.readlines()

map=[]
for line in lines:
    map.append([int(position) for position in line[:-1]])

traveled_points=[]
minimum_positions=[]
minimums=[]
for i in range(len(map)):
    for j in range(len(map[0])):
        try:
            map.index([i,j])
        except:
            is_minimum, traveled, = get_is_minimum(map,[i,j])
            for position_traveled in traveled:
                traveled_points.append(position_traveled)
            
            if is_minimum:
                minimums.append(map[i][j])
                minimum_positions.append([i,j])

result=0

for num in minimums:
    result+=num+1
print(f"Minimums are {minimums} and the result is {result}")
