f = open("input.txt", "r")
lines = f.readlines()

def get_range_to_mark(a,b):
    result=[]
    result.append(a)
    result.append(b)
    result.sort()
    return result

map={}
for line in lines:
    coordinate=line[:-1].split(" -> ")
    coordinates=[coordinate[0].split(","), coordinate[1].split(",")]
    if coordinates[0][0] == coordinates[1][0]:
        x=int(coordinates[0][0])
        start,end=get_range_to_mark(int(coordinates[0][1]),int(coordinates[1][1]))
        for i in range(start,end+1):
            try:
                map[(x,i)]+=1
            except:
                map[(x,i)]=1

    elif coordinates[0][1] == coordinates[1][1]:
        y=int(coordinates[0][1])
        start,end=get_range_to_mark(int(coordinates[0][0]),int(coordinates[1][0]))
        for i in range(start,end+1):
            try:
                map[(i,y)]+=1
            except:
                map[(i,y)]=1
    else:
        incrementalx=1
        if int(coordinates[0][0])>int(coordinates[1][0]):
            incrementalx=-1
        incrementaly=1
        try:
            if int(coordinates[0][1])>int(coordinates[1][1]):
                incrementaly=-1
        except:
            print(coordinates[0][1])
            print(coordinates[1][1])    
        x=int(coordinates[0][0])
        y=int(coordinates[0][1])
        while x!=int(coordinates[1][0])+incrementalx:
            try:
                map[(x,y)]+=1
            except:
                map[(x,y)]=1
            x+=incrementalx
            y+=incrementaly

counter=0
for value in map.values():    
    if value>1:
        counter+=1

# print(map)
print(f"There are {counter} dangerous points")
