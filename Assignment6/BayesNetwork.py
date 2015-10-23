__author__ = 'Zak'

import sys
import math
import queue
import getopt

#probs is prob = true or low
P = None
S = None
C = None
X = None
D = None

nodes = []

class Node:
    def __init__(self, name, probs, parents):
        self.name = name
        self.parents = parents
        self.probs = probs
        self.children = []

    def IsChildOf(self, node):
        b = False
        for p in self.parents:
            if node == p:
                return True
            else:
                if p.IsChildOf(node):
                    return True

    def IsParentOf(self, node):
        return node.IsChildOf(self)

def cprob(target, conds, nodes):
    # print("conditional")
    # print(target[0].name[0])
    ans = 0
    if target in conds:
        return target[1]
    elif (target[0], 1 - target[1]) in conds:
        return 1 - target[1]

    for c in conds:
        if c[0].IsChildOf(target[0]):
            newconds = list(conds)
            newconds.append(target)
            ans = jprob(newconds, nodes)/jprob(conds, nodes)
            return ans

    probs = target[0].probs
    if len(probs) == 1:
        #print("source:")
        #print(probs[0][1])
        ans = probs[0][1]
    else:
        sum = 0
        for prob in probs:
            touplist = prob[0]
            chance = prob[1]
            for toup in touplist:
                newconds = conds
                if toup in conds:
                    value = 1
                elif (toup[0], 1-toup[1]) in conds:
                    value = 0
                else:
                    value = cprob(toup, newconds, nodes)
                chance *= value
            sum += chance
            ans = sum
    if target[1] == 0:
        ans = 1 - ans
    return ans

def jprob(jnodes, nodes):
    print("joint")

    for n in jnodes:
        print(n[0].name[0])

    #turn to conditional
    #sort so that first node is lowest
    newNodes = []
    for n in nodes:
        if (n, 0) in jnodes:
            newNodes.append((n, 0))
        elif (n, 1) in jnodes:
            newNodes.append((n, 1))

    jnodes = newNodes
    jnodes.reverse()

    mult = 1
    for i in range(0, len(jnodes)):
        mult *= cprob(jnodes[i], jnodes[i+1:], nodes)
    return mult


def GetNode(nodename, nodes):
    for n in nodes:
        if nodename in n.name:
            return n

def main():
    optlist, args = getopt.getopt(sys.argv[1:],'g:j:m:p:')

    P = Node(['P', 'p'], [0.9], [])
    S = Node(['S', 's'], [0.3], [])
    C = Node(['C','c'], [0.03, 0.001, 0.05, 0.02], [P, S])
    X = Node(['X','x'], [0.9, 0.2], [C])
    D = Node(['D','d'], [0.65, 0.3], [C])

    P.probs = [(None, 0.9)]
    S.probs = [(None, 0.3)]

    values1 = [(P, 1), (S, 1)]
    values2 = [(P, 1), (S, 0)]
    values3 = [(P, 0), (S, 1)]
    values4 = [(P, 0), (S, 0)]
    C.probs = [(values1, 0.03),(values2, 0.001), (values3, 0.05), (values4, 0.02)]

    values1 = [(C, 1)]
    values2 = [(C, 0)]
    X.probs = [(values1, 0.9),(values2, 0.2)]

    values1 = [(C, 1)]
    values2 = [(C, 0)]
    D.probs = [(values1, 0.65),(values2, 0.3)]

    P.children = [C]
    S.children = [C]
    C.children = [X, D]
    X.children = []
    D.children = []

    nodes = [P, S, C, X, D]

    ans = 0

    i = 0
    while(True):
        type = optlist[i][0]
        #g = condition, j = joint, m = marg, p = set
        if type == '-p':
            n = GetNode(optlist[i][1], nodes)
            n.probs[0] = (None, float(args[i]))
            #print(n.probs[0])
            i += 1
            continue
        elif type == '-g':
            target = (GetNode(optlist[i][1][0], nodes), 1)
            string = optlist[i][1][1:]#no | to ignore
            conds = []
            value = 1
            for s in string:
                if s == '~':
                    value = 0
                else:
                    conds.append((GetNode(s, nodes), value))
                    value = 1
            ans = cprob(target, conds, nodes)
            break
        elif type == '-j':
            string = optlist[i][1]
            jnodes = []
            for c in string:
                value = 1
                if c == '~':
                    value = 0
                else:
                    jnodes.append((GetNode(c, nodes), value))
            ans = jprob(jnodes, nodes)
            break
        elif type == '-m':
            ans = cprob((GetNode(optlist[i][1], nodes), 1), [], nodes)
            break

    print("The answer is: ")
    print(ans)



if __name__ == "__main__":
    main()