import sys


# The input file will begin with one line containing integers J and C, the number of junction points and
# the number of possible connections respectively.
n = sys.stdin.readline().rstrip("\n")

n = n.split()

# print(n[0],n[1])
points = []
edges = []
numPoints = int(n[0])
#print(n[1].replace(" ", ""), "meme",45,"meme")
numEdges = int(n[1])

# go through the first number of times to get the points
for i in range(numPoints):
    points.append(sys.stdin.readline().rstrip("\n"))

# go through the second number of times to get the edges
for i in range(numEdges):
    edges.append(sys.stdin.readline().rstrip("\n"))


#print(edges)
#print(points)

edge_dict2 = {}
for i in points:
    point = i.split()
    edge_dict2[point[0]] = point[1]

edge_dict = {}
for i in points:
    point = i.split()
    if edge_dict2[point[0]] == "switch":
        switch = point[0]
    if edge_dict2[point[0]] == "light":
        edge_dict2[point[0]] = switch

    edge_dict[point[0]] = point[0]






# sort input array based on weights
def edgeValue(elem):
    weight = elem.split()
    return int(weight[2])

num = 0
for i in edges:
    num +=1

edges = set(edges)
edges = list(edges)


edges.sort(key=edgeValue)

numEdges = 0
for i in edges:
    numEdges +=1


def find(point):
    if edge_dict[point] != point:
        # print(point)
        return find(edge_dict[point])
    # print(point)
    return edge_dict[point]

def reverse(point):
    if point != edge_dict[point]:

        # edge_dict[point] = point
        returnedPoint = reverse(edge_dict[point])

        edge_dict[returnedPoint] = point
        #print("REVERESSSSSSESEES",edge_dict[returnedPoint], "->", point)
        return point
    else:

        return point


def union(uRootKey, vRootKey,u, v, uKey, vKey):
    #print("UNION", u, edge_dict[u], "\n", v, edge_dict[v])
    # print(uRootKey, uKey, vKey)
    if uKey == "switch":
        if vKey != "light":
            edge_dict[u] = v
        else:
            bottom = reverse(v)
            edge_dict[v] = u


    elif vKey == "switch":
        if uKey != "light":
            edge_dict[v] = u
        else:
            bottom = reverse(u)
            edge_dict[u] = v

    elif (uRootKey not in edge_dict2.keys()) and uKey == "light" and vKey == "light":
        bottom = reverse(v)
        edge_dict[v] = u

    elif vRootKey not in edge_dict2.keys() and vKey == "light" and uKey == "light":
        bottom = reverse(u)
        edge_dict[u] = v

    elif uRootKey  == "breaker":
        bottom = reverse(v)
        edge_dict[v] = u


    elif vRootKey == "breaker":
        bottom = reverse(u)
        edge_dict[u] = v



    else:
        bottom = reverse(u)
        edge_dict[u] = v

    #print("UNION", u,"points to->", edge_dict[u], "\n", v, "points to->",edge_dict[v])

# print(edges[0], numEdges)

listOfAccepted = []


def kruskal():
    edgesAccepted = 0
    totalCost = 0
    hasBreaker = False

    while(edgesAccepted < (numEdges)):
        e = edges[edgesAccepted]
        #print("testing:", e, "edges accepted:", edgesAccepted, numEdges)
        e = e.split()
        u = e[0]
        v = e[1]

        cost = int(e[2])
        uRoot = find(u)
        vRoot = find(v)
        #get if its a box or outlet or light ect..
        uRootKey = edge_dict2[uRoot]
        vRootKey = edge_dict2[vRoot]

        uKey = edge_dict2[u]
        vKey = edge_dict2[v]



        # light1 -> light2
        # (if both lights are connected to same switch
        if (uKey in edge_dict2.keys()) and(vKey in edge_dict2.keys()) and (uRoot != vRoot):
            if uKey == vKey:
                union(uRootKey, vRootKey, u, v, "light", "light")
                listOfAccepted.append(str(e[0] + " " + e[1] + " " + e[2]))
                totalCost += cost




        elif uKey in edge_dict2.keys():

            if v == uKey and (uRoot != vRoot):
                union(uRootKey, vRootKey, u, v, "light", vKey)
                listOfAccepted.append(str(e[0] + " " + e[1] + " " + e[2]))
                totalCost += cost


        elif vKey in edge_dict2.keys():

            if u == vKey and (uRoot != vRoot):
                union(uRootKey, vRootKey, u, v, uKey, "light")
                listOfAccepted.append(str(e[0] + " " + e[1] + " " + e[2]))
                totalCost += cost


        #
        #  switch -> light
        #  light -> switch


        ##### light to LIGHT

        # no switch on something else once its attached to no light
        elif (uKey == "switch" and uRootKey != "switch") or (vKey == "switch" and vRootKey != "switch"):
            pass
        # #no light and junction
        # elif (uKey == "light" and vKey == "box") or (vKey == "light" and uKey == "box"):
        #     pass
        # #no outlet and light
        # elif (uKey == "light" and vKey == "outlet") or (vKey == "light" and uKey == "outlet"):
        #     pass
        # # no breaker and light
        # elif (uKey == "light" and vKey == "breaker") or (vKey == "light" and uKey == "breaker"):
        #     pass
        #no switch on switch
        elif (uKey == "switch" and vKey == "switch"):
            pass




        elif(uRoot != vRoot):
            union(uRootKey, vRootKey, u, v, uKey, vKey)
            listOfAccepted.append(str(e[0] + " " + e[1] + " " + e[2]))
            totalCost += cost


            if (uKey == "breaker") or (vKey == "breaker"):
                hasBreaker = True

        edgesAccepted += 1
    if hasBreaker:
        return totalCost
    else:
        return 0

print(kruskal())



# for i in listOfAccepted:
#     print(i)
    #i = str(i[0] + " " + i[1] + " " + i[2])



#print("Here",find("s3"),find("l3"),find("l4"),find("l5"))

# correctEdges = ["s2 o3 1",
# "s3 j1 1",
# "s1 l7 1",
# "j1 s4 1",
# "o3 j2 1",
# "o1 j1 2",
# "s3 l3 2",
# "s1 o4 2",
# "o2 j1 2",
# "l3 l4 3",
# "s4 l8 3",
# "b1 o3 4",
# "b1 o4 4",
# "l1 l2 4",
# "s3 l5 5",
# "j1 o3 5",
# "s2 l2 6",
# "s1 l6 8"]
#
# correctEdges = set(correctEdges)
# print(listOfAccepted)
# listOfAccepted = set(listOfAccepted)
#
# c = listOfAccepted.difference(correctEdges)
# d = correctEdges.difference(listOfAccepted)
# print("COMPARISIONNnnn")
# print(c)
# print("COMPARISIONNnnn")
# print(d)