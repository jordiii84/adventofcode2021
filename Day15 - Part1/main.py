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
    if x<(len(map)-1):
        adjacents.append((x+1,y))

    if y<(len(map[0])-1):
        adjacents.append((x,y+1))
    return adjacents

def get_cost(path,tag):
    print(f"----- {tag} {path}")

f = open("input.txt", "r")
lines = f.readlines()
map=[]
for line in lines:
    row=[int(number) for number in line[:-1]]
    map.append(row)

# draw_map(map,"Start")
found=False
possible_paths=[]
start_point=(0,0)
starting_path={}
starting_path[start_point]=0
possible_paths.append(starting_path)

optimal_paths={}
optimal_paths[start_point]=start_point

while not found:
    new_paths=[]
    for path in possible_paths:
        keys=list(path.keys())
        values=list(path.values())
        last_point=keys[values.index(max(values))]
        last_value=path[last_point]
        adjacents=get_adjacents(map,last_point)
        for adjacent in adjacents:
            new_path=path.copy()
            if adjacent not in keys:
                x=adjacent[0]
                y=adjacent[1]
                cost=last_value+map[x][y]
                add_adjacent_in_path=True
                new_path[adjacent]=last_value+map[x][y]
                try:
                    optimal_path=optimal_paths[adjacent]
                    if optimal_path[adjacent]>new_path[adjacent]:
                        optimal_paths[adjacent]=new_path
                        new_paths.append(new_path)
                except:
                    optimal_paths[adjacent]=new_path
                    new_paths.append(new_path)
    possible_paths=new_paths.copy()
    if(len(possible_paths)==0):
        found=True
    print(f"Len of possible_paths: {len(possible_paths)}")
    # draw_paths(possible_paths,"End of step")

max_x=len(map)
max_y=len(map[0])
max_point=(max_x-1,max_y-1)
print(max_x)
print(max_y)
print(optimal_paths[max_point])
print(optimal_paths[max_point][max_point])