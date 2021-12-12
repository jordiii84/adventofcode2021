def get_connected_nodes(node,connections):
    connected_nodes=[]
    for connection in connections:
        try: 
            index=connection.index(node)
            connected_node=connection[1-index]
            if connected_node!="start":
                connected_nodes.append(connected_node)
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

connections_node={}
for node in set(nodes):
    connections_node[node]=get_connected_nodes(node,connections)

end=False
paths=[["start"]]
while not end:
    new_paths=[]
    for path in paths:
        last_node=path[-1]
        if last_node!="end":
            connected_nodes=connections_node[last_node]
            can_revisit_lower=True
            for node in path:
                if node.islower() and path.count(node)>1:
                    can_revisit_lower=False
            for connected_node in connected_nodes:
                if (connected_node.islower() and connected_node not in path) or connected_node.isupper() or can_revisit_lower:
                    new_path=path.copy()
                    new_path.append(connected_node)
                    new_paths.append(new_path)
        else:
            new_paths.append(path)
    if new_paths==paths:
        end=True
    else:
        paths=new_paths.copy()
    # print("-----Finished_paths-------")
    # for path in paths:
    #     print(path)
print(f"There are {len(paths)} different paths")
