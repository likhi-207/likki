n=5
edges=((1,2),(2,3),(3,4),(4,5),(5,1))

adj={}
for i in range(1,n+1):
    adj[i]=[]
print(adj)


for i in edges:
    u,v=i
    adj[u].append(v)
    adj[v].append(u)


print(adj)