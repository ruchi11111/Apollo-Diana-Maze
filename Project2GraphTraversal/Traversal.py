import sys
import re
import linecache as lc


GRAPH_FILE_NAME = sys.argv[1]    #get inputfile from argument 1
OUTPUT_FILE_NAME = sys.argv[2]
queueelement = []                #list for printing the path by inserting connected nodes
adjajencymatrix = []
dict = {"color": "e1", "visited": "e2", "connectededge": "e3", "direction": "e4"}       #dictonary to store color, visited nodes, parent nodes and directions

# To get number of rows and columns
rc = lc.getline(GRAPH_FILE_NAME, 1)
y = rc.split()
r = int(y[0])
c = int(y[1])

# To create graph from text file
with open(GRAPH_FILE_NAME) as file:
    next(file)
    graph = [line for line in file]
open(OUTPUT_FILE_NAME, 'w').close()



#print path in the output file
def Path():
    i = r - 1
    j = c - 1
    pathlist = []

    while True:
        parentRow = adjajencymatrix[i][j]["connectededge"][0]
        parentColumn = adjajencymatrix[i][j]["connectededge"][1]
        print(parentRow, parentColumn)
        tempRow = i - adjajencymatrix[i][j]["connectededge"][0]
        tempColumn = j - adjajencymatrix[i][j]["connectededge"][1]

        if (adjajencymatrix[parentRow][parentColumn]["direction"][0] == 'S'):
            pathlist.append(tuple([adjajencymatrix[parentRow][parentColumn]["direction"], tempRow]))
        elif (adjajencymatrix[parentRow][parentColumn]["direction"][0] == 'N'):
            pathlist.append(tuple([adjajencymatrix[parentRow][parentColumn]["direction"], (tempRow * -1)]))
        elif (adjajencymatrix[parentRow][parentColumn]["direction"][0] == 'E'):
            pathlist.append(tuple([adjajencymatrix[parentRow][parentColumn]["direction"], tempColumn]))
        elif (adjajencymatrix[parentRow][parentColumn]["direction"][0] == 'W'):
            pathlist.append(tuple([adjajencymatrix[parentRow][parentColumn]["direction"], (tempColumn * -1)]))

        i = parentRow
        j = parentColumn

        if (i != 0 or j != 0):
            continue
        else:
            break
    print("Graph takes ", len(pathlist), " steps to reach the destination")
    x = len(pathlist) - 1
    while x >= 0:
        with open(OUTPUT_FILE_NAME, "a") as f:
            print(f"{pathlist[x][1]}{pathlist[x][0]}", end=" ", file=f)
        x = x - 1




def MakeGraph():
    for elements in range(len(graph)):           # To create a mulidimensional list of dictionaries to create adjacency matrix
        listforgraph = graph[elements]
        i = 0
        empytlist = []
        while (i < len(listforgraph)):
            if (listforgraph[i] == 'R' or listforgraph[i] == 'B'):
                dict["color"] = listforgraph[i]
                dict["visited"] = 0
                dict["connectededge"] = (0, 0)
                if (listforgraph[i + 3] != ' '):
                    dict["direction"] = listforgraph[i + 2:i + 4]                #when directions are: SE, SW, NE, NW
                    i = i + 3
                else:
                    dict["direction"] = listforgraph[i + 2:i + 3]
                    i = i + 2
                empytlist.append(dict.copy())                                   #when directions are: S, N, E, W
            elif (listforgraph[i] == 'O'):
                dict["color"] = listforgraph[i]
                dict["visited"] = 0
                dict["connectededge"] = (0, 0)
                dict["direction"] = listforgraph[i]
                empytlist.append(dict.copy())
            i += 1
        adjajencymatrix.append(empytlist)



def BFSTraversal():
    queueelement.append((0, 0))                             # Using BFS to solve the maze
    while True:
        adjajencymatrix[queueelement[0][0]][queueelement[0][1]]["visited"] = 1
        addnodestomatrix()
        queueelement.pop(0)
        if (queueelement == []):
            break

def addnodestomatrix():
    nodeclr = adjajencymatrix[queueelement[0][0]][queueelement[0][1]]["color"]        #get element from list of list for obtaining color
    nodecol = queueelement[0][1]
    noderow = queueelement[0][0]
    nodedir = adjajencymatrix[queueelement[0][0]][queueelement[0][1]]["direction"]    ##get element from list of list for obtaining direction
    i = 0
    j = 0

    if (nodedir == "N"):
        i = noderow
        while (i >= 0):
            if (adjajencymatrix[i][nodecol]["color"] != nodeclr and adjajencymatrix[i][nodecol]["visited"] == 0):
                queueelement.append((i, nodecol))
                adjajencymatrix[i][nodecol]["visited"] = 1
                adjajencymatrix[i][nodecol]["connectededge"] = (noderow, nodecol)
            i = i - 1

    elif (nodedir == "NE"):
        i = noderow
        j = nodecol
        while (i >= 0 and j < c):
            if (adjajencymatrix[i][j]["color"] != nodeclr and adjajencymatrix[i][j]["visited"] == 0):
                queueelement.append((i, j))
                adjajencymatrix[i][j]["visited"] = 1
                adjajencymatrix[i][j]["connectededge"] = (noderow, nodecol)
            i = i - 1
            j = j + 1

    elif (nodedir == "E"):
        i = nodecol
        while (i < c):
            if (adjajencymatrix[noderow][i]["color"] != nodeclr and adjajencymatrix[noderow][i]["visited"] == 0):
                queueelement.append((noderow, i))
                adjajencymatrix[noderow][i]["visited"] = 1
                adjajencymatrix[noderow][i]["connectededge"] = (noderow, nodecol)
            i = i + 1

    elif (nodedir == "SE"):
        i = noderow
        j = nodecol
        while (i < r and j < c):
            if (adjajencymatrix[i][j]["color"] != nodeclr and adjajencymatrix[i][j]["visited"] == 0):
                queueelement.append((i, j))
                adjajencymatrix[i][j]["visited"] = 1
                adjajencymatrix[i][j]["connectededge"] = (noderow, nodecol)
            i = i + 1
            j = j + 1

    elif (nodedir == "S"):
        i = noderow
        while (i < r):
            if (adjajencymatrix[i][nodecol]["color"] != nodeclr and adjajencymatrix[i][nodecol]["visited"] == 0):
                queueelement.append((i, nodecol))
                adjajencymatrix[i][nodecol]["visited"] = 1
                adjajencymatrix[i][nodecol]["connectededge"] = (noderow, nodecol)
            i = i + 1

    elif (nodedir == "SW"):
        i = noderow
        j = nodecol
        while (i < r and j >= 0):
            if (adjajencymatrix[i][j]["color"] != nodeclr and adjajencymatrix[i][j]["visited"] == 0):
                queueelement.append((i, j))
                adjajencymatrix[i][j]["visited"] = 1
                adjajencymatrix[i][j]["connectededge"] = (noderow, nodecol)
            i = i + 1
            j = j - 1

    elif (nodedir == "W"):
        i = nodecol
        while (i >= 0):
            if (adjajencymatrix[noderow][i]["color"] != nodeclr and adjajencymatrix[noderow][i]["visited"] == 0):
                queueelement.append((noderow, i))
                adjajencymatrix[noderow][i]["visited"] = 1
                adjajencymatrix[noderow][i]["connectededge"] = (noderow, nodecol)
            i = i - 1

    elif (nodedir == "NW"):
        i = noderow
        j = nodecol
        while (i >= 0 and j >= 0):
            if (adjajencymatrix[i][j]["color"] != nodeclr and adjajencymatrix[i][j]["visited"] == 0):
                queueelement.append((i, j))
                adjajencymatrix[i][j]["visited"] = 1
                adjajencymatrix[i][j]["connectededge"] = (noderow, nodecol)
            i = i - 1
            j = j - 1


MakeGraph()
BFSTraversal()
Path()