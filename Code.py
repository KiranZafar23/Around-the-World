def dijkstra(graph, root):
    bucket = [root]
    city_distance = {}
    city_distance[root] = 0
    for v in bucket:
        for id in range(len(graph[v])):
            if graph[v][id][0] not in bucket:
                temp = city_distance[v]+ graph[v][id][1]
                vertice = graph[v][id]
        for ver in graph[v]:
            if city_distance[v]+ ver[1] <= temp and ver[0] not in bucket:
                temp = city_distance[v]+ ver[1]
                vertice = ver
        if vertice[0] not in bucket:
            bucket.append(vertice[0])
            city_distance[vertice[0]] = city_distance[v]+ vertice[1]
    return bucket, city_distance
with open("ha30_dist.txt") as distance:
    distances = distance.read().split()
with open("ha30_name.txt") as name:
    names = name.read().split('\n')
with open("ha30_code.txt") as code:
    codes = code.read().split()
graph = {}
for i in range(len(codes)):
    city = []
    val = i*(len(codes))
    dist =distances[val:val+len(codes)]
    for j in range(len(codes)):
        city.append((codes[j],int(dist[j])))
    graph[codes[i]] = city
AllPaths = {}
for i in codes:
    root = i
    bucket, paths = dijkstra(graph,root)
    AllPaths[i] = [bucket,paths]
print(AllPaths)
while(True):
    print("""Select from the following option.
    1. Shortest Path.
    2. Longest Shortest Path.
    3. Route and distance between two cities with minimum cost.""")
    choice = int(input("Enter choice:"))
    if choice == 1:
        print(AllPaths['AZ'])
    elif choice == 2:
        print(AllPaths['NS'])  
    elif choice == 3:
        a = input("Root city:")
        b = input("End city:")
        required = AllPaths[a] 
        path = required[0][:required[0].index(b)+1]
        distance= list(required[1].items())[:len(path)]
        print(path,distance)