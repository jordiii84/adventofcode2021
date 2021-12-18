def draw_map(map, tag):
    print(f"--------------drawing {tag} ")
    for row in map:
        print(row)
    print(f"--------------End of drawing {tag} ")

def draw_paths(paths,tag):
    print(f"---------- {tag}")
    for path in paths:
        print(path)

def get_adjacents(map,position):
    adjacents=[]
    x=position[0]
    y=position[1]

    adjacents=[]
    if x>0:
        adjacents.append((x-1,y))
    if x<(len(map)-1):
        adjacents.append((x+1,y))
    if y>0:
        adjacents.append((x,y-1))
    if y<(len(map[0])-1):
        adjacents.append((x,y+1))
    return adjacents

def get_cost(path,tag):
    print(f"----- {tag} {path}")

def increase_row(row):
    return [value+1 if value<9 else 1 for value in row]

f = open("input.txt", "r")
lines = f.readlines()
map=[]
for line in lines:
    expanded_row=[]
    row=[int(number) for number in line[:-1]]
    expanded_row+=row
    prev_row=row.copy()
    for i in range(4):
        new_row=increase_row(prev_row)
        expanded_row+=new_row
        prev_row=new_row.copy()
    map.append(expanded_row)


original_rows=map.copy()
for i in range(4):
    new_original_rows=[]
    for row in original_rows:
        increased_row=increase_row(row)
        new_original_rows.append(increased_row)
        map.append(increased_row)
    original_rows=new_original_rows.copy()

def draw_cost_map(map):
    for i in range(500):
        row=""
        for j in range(500):
            row+=str(map[(i,j)])+","
        print(row)

found=False
possible_paths=[]
cost_map={}
starting_path={}

def get_diagonal(position):
    x=position[0]
    y=position[1]

    new_x=x
    new_y=y
    diagonal=[]
    while new_y>=0 and new_x<=y:
        diagonal.append((new_x,new_y))
        new_x+=1
        new_y-=1
    return diagonal
    
end=False
current_position=(0,0)
cost_map[current_position]=0
positions_to_calculate=[]
positions_to_calculate.append(current_position)
while not end:
    new_positions_to_calculate=[]
    for position in positions_to_calculate:
        adjacents=get_adjacents(map,position)
        # print(adjacents)
        for adjacent in adjacents:
            new_cost=cost_map[position]+map[adjacent[0]][adjacent[1]]
            try:
                current_cost=cost_map[adjacent]
                if new_cost<current_cost:
                    cost_map[adjacent]=new_cost
                    new_positions_to_calculate.append(adjacent)
            except:
                cost_map[adjacent]=new_cost
                new_positions_to_calculate.append(adjacent)
    positions_to_calculate=new_positions_to_calculate.copy()
    if len(positions_to_calculate)==0:
        end=True
# print(map[len(map)-1][len(map[0])-1])
draw_cost_map(cost_map)
                # print("No cost")
        # if position[0]==0:
        #     cost_map[position]=cost_map[position[0],position[1]-1]+map[position[0]][position[1]]

        # elif position[1]==0:
        #     cost_map[position]=cost_map[position[0]-1,position[1]]+map[position[0]][position[1]]
        # else:
        #     x_position=(position[0],position[1]-1)
        #     y_position=(position[0]-1,position[1])
        #     cost_x=cost_map[x_position[0],x_position[1]]
        #     cost_y=cost_map[y_position[0],y_position[1]]
        #     cost_position=map[position[0]][position[1]]
        #     cost_map[position] = cost_x+cost_position if cost_x<cost_y else cost_y+cost_position
    # print(cost_map)        
