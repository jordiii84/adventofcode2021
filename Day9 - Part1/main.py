def print_basins(points,width,height):
    # print(points)
    rows=[]
    for i in range(width):
        row=[0]*height
        rows.append(row)
    for point in points:
        # print(points[point[0],point[1]])
        rows[point[0]][point[1]]=points[point[0],point[1]]

    for row in rows:
        print(row)

def get_adjacent_basin(map, basin):
    # print(f"------------{basin}-------------")
    traveled_positions=[]
    for point in basin:
        x=point[0]
        y=point[1]

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
            if map[adjx][adjy]!=9 and (adjx,adjy) not in basin:
                if (adjx,adjy) in points.keys():
                    basin=points[(adjx,adjy)]

                traveled_positions.append([adjx,adjy])

    # print(f"traveled_positions -> {traveled_positions}")
    return traveled_positions

def get_first_unused_zero(map, marked):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j]!=9 and (i,j) not in marked:
                return (i,j)
    return -1

f = open("input.txt", "r")
lines = f.readlines()

map=[]
for line in lines:
    map.append([int(position) for position in line[:-1]])

traveled_points=[]
minimum_positions=[]
points={}
end=False
basin_end=False
basin_index=1
basins=[]
marked=[]

basin=[]
while not end:
    first_position = get_first_unused_zero(map, set(marked))
    if first_position!=-1:
        basin.append(first_position)
        marked.append(first_position)
        basin_end=False
        adjacents = []
        while not basin_end:
            found_adjacents = get_adjacent_basin(map,set(basin))
            if len(found_adjacents)>0:
                for found_adjacent in found_adjacents:
                    basin.append((found_adjacent[0],found_adjacent[1]))
                    marked.append((found_adjacent[0],found_adjacent[1]))
            else:
                basin_end=True
                basins.append(basin)
                basin=[]

    else:
        end=True
    # end=True
result=0

lengths=[len(set(basin)) for basin in basins]
sizes=sorted(lengths)

result=sizes[len(sizes)-1]*sizes[len(sizes)-2]*sizes[len(sizes)-3]
print(f"The final result is: {sizes[len(sizes)-1]} * {sizes[len(sizes)-2]} * {sizes[len(sizes)-3]} = {result}")
