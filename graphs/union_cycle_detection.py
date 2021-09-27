'''
can only detect cycle in undirected graphs

'''
def find(vertix):
    if mapping[vertix]==-1:
        return vertix
    return find(mapping[vertix])

def union(fr,to):
    frParent = find(fr)
    toParent = find(to)
    mapping[frParent]=toParent

def isCyclic(edge_list):
    for edge in edge_list:
        frParent=find(edge[0])
        toParent=find(edge[1])
        if frParent==toParent:
            return True
        union(edge[0],edge[1])
    return False

edge_list = [] #nested list of vertices pairs
mapping = {} #node : parent pairs
node=set()
E,V=map(int,input().split(' '))
for i in range(E+1):
    fr,to=map(int,input().split(' '))
    edge_list.append([fr,to])
    node.add(fr)
    node.add(to)

for i in node:
    mapping[i]=-1
print(edge_list)
print(mapping)
if isCyclic(edge_list):
    print('cycle exist')
else:
    print('cycle doesnt exist')
