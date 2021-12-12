# class Node():
#     name=""
#     connections=[]
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         print(f" Node name {self.name} . Connections {self.connections}")
#     def add_connection(self,connection):
#         self.connections.append(connection)

# f = open("input_test.txt", "r")
# lines = f.readlines()
# nodes={}
# for line in lines:
#     nodes_connected=line[:-1].split("-")
#     for n in nodes_connected:
#         node=nodes.get(n)
#         node.add_connection()
#         if not node:
#             node = Node(n)
#             nodes[n]=node

# print(nodes)
# for node in nodes:
#     print(node)

def get_connected_nodes(node,connections):
    connected_nodes=[]
    for connection in connections:
        try: 
            index=connection.index(node)
            connected_nodes.append(connection[1-index])
        except:
            pass
    return connected_nodes

f = open("input.txt","r")
lines = f.readlines()
connections=[]
nodes=[]
for line in lines:
    nodes_conn=line[:-1].split("-")
    connections.append((nodes_conn[0],nodes_conn[1]))
    nodes.append(nodes_conn[0])
    nodes.append(nodes_conn[1])

end=False
paths=[["start"]]
while not end:
    new_paths=[]
    for path in paths:
        # print(f"Trying path {path}")
        last_node=path[-1]
        if last_node!="end":
            connected_nodes=get_connected_nodes(last_node,connections)
            for connected_node in connected_nodes:
                if (connected_node.islower() and connected_node not in path) or connected_node.isupper():
                    new_path=path.copy()
                    new_path.append(connected_node)
                    new_paths.append(new_path)
        else:
            new_paths.append(path)
    if new_paths==paths:
        end=True
    else:
        paths=new_paths.copy()

for path in paths:
    print(path)
print(f"There are {len(paths)} different paths")
