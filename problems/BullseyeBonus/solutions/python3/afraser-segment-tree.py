# Computes average by using a segment tree that stores the sum of the array
# Runtime is O(NlogN + MlogN)
# Constructing the tree takes NlogN time. Each query M takes logN time to get the average
# and then perform two updates to the tree.

import math

[n, m] = [int(x) for x in input().split(' ')]
archers = [int(x) for x in input().split(' ')]

class Node:
    left = None
    right = None
    def __init__(self, total, leftBound, rightBound):
        self.total = total
        self.leftBound = leftBound
        self.rightBound = rightBound

def fillTree(archers, leftBound, rightBound):
    currNode = Node(sum(archers[leftBound: rightBound + 1]), leftBound, rightBound)
    if rightBound == leftBound:
        return currNode
    
    middle = leftBound + math.floor((rightBound - leftBound) / 2)

    currNode.left = fillTree(archers, leftBound, middle)
    currNode.right = fillTree(archers, middle + 1, rightBound)
    return currNode

def getTotal(node, leftBound, rightBound):
    if node == None:
        return 0

    if node.leftBound == leftBound and node.rightBound == rightBound:
        return node.total
    
    middle = node.leftBound + math.floor((node.rightBound - node.leftBound) / 2)
    
    if rightBound <= middle:
        return getTotal(node.left, leftBound, rightBound)
    
    if leftBound >= middle + 1:
        return getTotal(node.right, leftBound, rightBound)
    
    return getTotal(node.left, leftBound, middle) + getTotal(node.right, middle + 1, rightBound)

def updateTotal(node, index, modifier):
    if node == None:
        return

    global archers
    node.total = node.total + modifier

    if index == node.leftBound and index == node.rightBound:
        return
    
    middle = node.leftBound + math.floor((node.rightBound - node.leftBound) / 2)

    if index <= middle:
        updateTotal(node.left, index, modifier)
    
    if index >= middle + 1:
        updateTotal(node.right, index, modifier)



root = fillTree(archers, 0, len(archers) - 1)

for i in range(m):
    [x, y, l, r] = [int(x) for x in input().split(' ')]
    average = math.floor(getTotal(root, l - 1, r - 1) / (r + 1 - l))
    archers[x - 1] = archers[x - 1] + average
    archers[y - 1] = archers[y - 1] - average
    updateTotal(root, x - 1, average)
    updateTotal(root, y - 1, average * -1)

print(archers.index(max(archers)) + 1)