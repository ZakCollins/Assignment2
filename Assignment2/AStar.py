__author__ = 'Zak'

import sys
import math

height = 8
width = 10

class Edge:
    def __init__(self, vert, weight):
        self.vert = vert
        self.weight = weight

class Vert:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.huer = 0
        self.distance = 0
        self.f = 0
        self.parent = None
        self.num = x + y * width


def createEdge(x, y, i, j, height, width, vertList, values):
    currIndex = j + i * width
    if x < 0 and j == 0:
        return
    if y < 0 and i == 0:
        return
    if x > 0 and j == width - 1:
        return
    if y > 0 and i == height - 1:
        return
    if values[i+y][j+x] == 2:
        return

    index = (j + x) + (i + y) * width
    if abs(x) + abs(y) == 2:
        weight = 14
    else:
        weight = 10
    if values[i+y][j+x] == 1:
        weight += 10
    vertList[currIndex].append(Edge(index, weight))

def main():
    fileName = sys.argv[1]
    print('Analyzing World: ', fileName)
    world = open(fileName, 'r')
    data = world.read()
    # for line in world:
    #     print(line)

    hType = int(sys.argv[2])

    values = [[0 for x in range(10)] for x in range(8)]

    i = 0
    j = 0
    for line in data:
        if line == '\n':
            i += 1
            j = 0
        elif line != ' ':
            values[i][j] = int(line)
            j += 1

    vertList = [[] for x in range(height * width)]
    for i in range(0, height):
        for j in range(0, width):
            createEdge(-1, -1, i, j, height, width, vertList, values)
            createEdge(-1, 0, i, j, height, width, vertList, values)
            createEdge(-1, 1, i, j, height, width, vertList, values)
            createEdge(1, -1, i, j, height, width, vertList, values)
            createEdge(1, 0, i, j, height, width, vertList, values)
            createEdge(1, 1, i, j, height, width, vertList, values)
            createEdge(0, -1, i, j, height, width, vertList, values)
            createEdge(0, 1, i, j, height, width, vertList, values)

    nodes = [None for x in range(height * width)]
    for i in range(0, height):
        for j in range(0, width):
            nodes[j + i * width] = Vert(j, i)

    if hType == 1:
        for i in range(0, 8):
            for j in range(0, 10):
                nodes[j + i * width].huer = (9 + i - j) * 10
    elif hType == 2:
        for i in range(0, 8):
            for j in range(0, 10):
                nodes[j + i * width].huer = (math.sqrt(math.pow(i, 2) + math.pow(9 - j, 2))) * 10

    # print("huer:")
    # k = 0
    # for node in nodes:
    #     print(node.huer, end = " ")
    #     k += 1
    #     if k == width:
    #         k = 0
    #         print(" ")

    start = ((height-1) * width)
    end = width - 1

    nodes[start].f = nodes[start].huer

    openList = [nodes[start]]
    closedList = []
    while openList:
        node = openList[0]
        cost = sys.maxsize
        for n in openList:
            if n.f < cost:
                cost = n.f
                node = n

        openList.remove(node)

        if node.num != end:#if not at end
            closedList.append(node)

            for edge in vertList[node.num]:
                newNode = nodes[edge.vert]
                distance = node.distance + edge.weight

                f = distance + newNode.huer
                if newNode in openList:
                    if f < newNode.f:
                        newNode.parent = node
                        newNode.distance = distance
                        newNode.f = f
                elif newNode not in closedList:
                    newNode.parent = node
                    newNode.distance = distance
                    newNode.f = f
                    openList.append(newNode)

        else:
            break

    # print("distance:")
    # k = 0
    # for node in nodes:
    #     print(node.distance, end = " ")
    #     k += 1
    #     if k == width:
    #         k = 0
    #         print(" ")
    #
    # print("f:")
    # k = 0
    # for node in nodes:
    #     print(node.f, end = " ")
    #     k += 1
    #     if k == width:
    #         k = 0
    #         print(" ")

    locations= []
    loc = nodes[end]
    while (loc.parent):
        locations.append((loc.x, loc.y))
        loc = loc.parent
    locations.append((loc.x, loc.y))

    cost = nodes[end].distance
    numExplored = len(closedList)
    locations.reverse()
    print("Cost: ", cost)
    print("Path: ", locations)
    print("Number of explored nodes: ", numExplored)



if __name__ == "__main__":
    main()