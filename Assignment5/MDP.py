__author__ = 'Zak'

import sys
import math
import queue

height = 8
width = 10

values = [[0 for x in range(width)] for x in range(height)]
util = [[0 for x in range(width)] for x in range(height)]
gamma = 0.9

def getReward(i, j):

    n = values[i][j]
    if n == 0:
        return 0
    elif n == 1:
        return -1
    elif n == 3:
        return -2
    elif n == 4:
        return 1
    elif n == 50:
        return 50

def upValue(i, j):
    if i == 0 or values[i-1][j] == 2:
        i += 1
    return U(i-1, j)

def leftValue(i, j):
    if j == 0 or values[i][j-1] == 2:
        j += 1
    return U(i, j-1)

def downValue(i, j):
    if i == height - 1 or values[i+1][j] == 2:
        i -= 1
    return U(i + 1, j)

def rightValue(i, j):
    if j == width - 1 or values[i][j+1] == 2:
        j -= 1
    return U(i, j+1)

# d is direction: 1 is up, 2 is left, 3 is down, 4 is right
def weightedSum(i, j, d):
    if d == 1:
        return 0.8 * upValue(i, j) + 0.1 * leftValue(i, j) + 0.1 * rightValue(i, j)
    if d == 2:
        return 0.8 * leftValue(i, j) + 0.1 * downValue(i, j) + 0.1 * upValue(i, j)
    if d == 3:
        return 0.8 * downValue(i, j) + 0.1 * rightValue(i, j) + 0.1 * leftValue(i, j)
    if d == 4:
        return 0.8 * rightValue(i, j) + 0.1 * upValue(i, j) + 0.1 * downValue(i, j)


def maxSum(i, j):
    return max(weightedSum(i, j, 1), weightedSum(i, j, 2), weightedSum(i, j, 3), weightedSum(i, j, 4))


def U(i, j):
    return util[i][j]


def calcU(i, j, delta):
    if values[i][j] == 50:
        return 0

    bestValue = maxSum(i, j)
    newUtil = getReward(i, j) + gamma * bestValue

    if newUtil > util[i][j]:
        delta = max(delta, abs(util[i][j] - newUtil))
        util[i][j] = newUtil
    return delta


def printMatrix(u):
    k = 0
    for i in range(0, height):
        print(" ")
        for j in range(0, width):
            print(int(u[i][j]), end = "    ")
    print(" ")
    print(" ")


def iterationLoop(epsilon):
    q = queue.Queue()
    while True:
        #printMatrix(util)
        delta = 0
        q.put((0, width-1))
        while not q.empty():
            x = q.get()
            if (x[0] < height-1 and values[x[0]+1][x[1]] != 2):
                q.put((x[0] + 1, x[1]))
            if (x[1] > 0 and values[x[0]][x[1]-1] != 2):
                q.put((x[0], x[1] - 1))

            delta = max(delta, calcU(x[0], x[1], delta))
        if delta < epsilon * (1 - gamma)/gamma:
            return

def calcPolicy():
    policy = [[0 for x in range(width)] for x in range(height)]
    for i in range(0, height):
        for j in range(0, width):
            if values[i][j] == 2:
                continue
            curPol = 1
            curMax = weightedSum(i, j, 1)
            if weightedSum(i, j, 2) > curMax:
                curMax = weightedSum(i, j, 2)
                curPol = 2
            if weightedSum(i, j, 3) > curMax:
                curMax = weightedSum(i, j, 3)
                curPol = 3
            if weightedSum(i, j, 4) > curMax:
                curPol = 4
            policy[i][j] = curPol
    return policy


def main():
    fileName = sys.argv[1]
    print('Analyzing World: ', fileName)
    world = open(fileName, 'r')
    data = world.read()

    epsilon = float(sys.argv[2])

    i = 0
    j = 0
    alter = 1
    for line in data:
        if line == '\n':
            i += 1
            j = 0
            alter = 1
        elif line != ' ':
            if alter == 1:
                values[i][j] = int(line)
                j += 1
            else:
                j -= 1
                values[i][j] = values[i][j] * 10 + int(line)
                if values[i][j] == 50:
                    util[i][j] = 50
                j += 1
            alter = 0
        else:
            alter = 1

    iterationLoop(epsilon)

    policy = calcPolicy()

    i = height-1
    j = 0
    path = []
    while not (i == 0 and j == width-1):
        path.append((j, i, round(util[i][j], 2)))
        if policy[i][j] == 1:
            i -= 1
        elif policy[i][j] == 2:
            j -= 1
        elif policy[i][j] == 3:
            i += 1
        elif policy[i][j] == 4:
            j += 1
    path.append((width-1, 0, 50))

    pathMatrix = [[0 for x in range(width)] for x in range(height)]
    for v in path:
        pathMatrix[v[1]][v[0]] = v[2]

    #printMatrix(util)
    #printMatrix(policy)
    print(path)
    printMatrix(pathMatrix)



if __name__ == "__main__":
    main()