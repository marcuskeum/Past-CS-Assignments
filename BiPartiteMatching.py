import sys


simpleYes = False

startNums = sys.stdin.readline().rstrip().split(" ")
numReq = int(startNums[0])
numClasses = int(startNums[1])
numClassesPerStudent = int(startNums[2])

if (numReq == 0) or (numClassesPerStudent ==0):
    print("Yes")
    simpleYes = True

studentSet = set()
studentsPerCourseL = []

studentDict = {}
courseDict = {}

#set student dict
for i in range(numReq):
    line = sys.stdin.readline().rstrip("\n")
    line = line.split(" ")
    studentSet.add(line[0])
    studentDict.setdefault(line[0], []).append(line[1])
    i +=1

#set class dict
for i in range(numClasses):
    line = sys.stdin.readline().rstrip("\n")
    line = line.split(" ")
    studentsPerCourseL.append(int(line[1]))
    courseDict[line[0]] = i
    i += 1


numStudents = len(studentSet)
matrixSize = numStudents + numClasses + 2

#make empty adj_mat
adjMatrix = [ [ 0 for i in range(matrixSize) ] for j in range(matrixSize) ]

#fill out source to graph
for i in range(1, numStudents + 1):
    adjMatrix[0][i] = numClassesPerStudent

#fill out graph to sink
for i in range(numClasses):
    adjMatrix[i + (numStudents+1)][matrixSize-1] = studentsPerCourseL[i]

#fill out 1s between students and classes


indexForFillingRow = 1
for student in studentDict:
    indClasses = studentDict.get(student)

    for i in indClasses:
        courseIndex = courseDict.get(i) + (numStudents+1)
        adjMatrix[indexForFillingRow][courseIndex] = 1
    indexForFillingRow += 1

####FORD FULKERSON ALGO

class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)



    def BFS(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)

        # Create a queue for BFS
        queue = []

        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:

                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True


        return False

    def FordFulkerson(self, source, sink):

        parent = [-1] * (self.ROW)
        # print(parent, self.ROW)
        max_flow = 0
        # print(source, sink, parent)
        while self.BFS(source, sink, parent):
            # print(source, sink, parent)
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow
            # print(max_flow,path_flow)

            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

    # The ford fulkerson algorithm is contributed by Neelam Yadav

# simpleYes = False
# numReq = 4
# numStudents = 2
# numClassesPerStudent = 2
# adjMatrix = [[0,2,2,0,0,0],
#  [0,0,0,1,1,0],
#  [0,0,0,1,1,0],
#  [0,0,0,0,0,3],
#  [0,0,0,0,0,3],
#  [0,0,0,0,0,0]]


# print(adjMatrix)
g = Graph(adjMatrix)

source = 0
sink = numStudents + numClasses +1 #numReq -1

maxFlow = g.FordFulkerson(source, sink)
# print(maxFlow)

if simpleYes == False:
    if maxFlow == (numStudents * numClassesPerStudent):
        print("Yes")
    else:
        print("No")

