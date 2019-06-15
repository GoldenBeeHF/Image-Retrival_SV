# This Python file uses the following encoding: utf-8
# Các hàm xử lý khi thao tác với cây STree.

import math
import random
import types
import struct

# Tính khoảng cách euclide giữa 2 vector
# vectorA: vector 1
# vectorB: vector 2
def computeDistanceEuclide(vectorA, vectorB):
    dis = 0
    for i in range(0, len(vectorA)):
        dis = dis + math.pow(vectorA[i] - vectorB[i], 2)
    return math.sqrt(dis)

# Tìm 2 vector có khoảng cách xa nhau nhất
# lstVector: danh sách các vector
# return 2 vector with max distance
def findMaxDistance(lstVector):
    max = computeDistanceEuclide(lstVector[0].getVector(), lstVector[1].getVector())
    vector1 = lstVector[0]
    vector2 = lstVector[1]
    for i in range(0, len(lstVector) - 1):
        for j in range(i + 1, len(lstVector)):
            if (max < computeDistanceEuclide(lstVector[i].getVector(), lstVector[j].getVector())):
                max = computeDistanceEuclide(lstVector[i].getVector(), lstVector[j].getVector())
                vector1 = lstVector[i]
                vector2 = lstVector[j]
    return [vector1, vector2]

# Tính vector trung bình của danh sách các vector
# lstVector: danh sách các vector
# idVector: id sẽ được đặt cho vector trung bình vừa tạo
def computeAvgVector(lstVector, idVector=None):
    n = 42
    avgVector = []
    for i in range(0, n):
        avgVector.append(0)
    for v in lstVector:
        for i in range(0, n):
            avgVector[i] = avgVector[i] + v.getVector()[i]

    for i in range(0, n):
        avgVector[i] = avgVector[i] / len(lstVector)
    if idVector is None:
        return avgVector
    else:
        return struct.Vector(avgVector, idVector)        

# Tìm node dựa vào id
# idNode: id của node cần tìm
# lstNode: danh sách các node trong cây
# lstLeaf: danh sách các lá trong cây
# return: 3 loại (node, leaf hoặc none)
def findNode(Node, lstNode, lstLeaf):
    for node in lstNode:
        if int(Node.getLink()) == int(node.id):
            return node
    for node in lstLeaf:
        if int(Node.getLink()) == int(node.id):
            return node
    return None

def findNodeById(idNode, lstNode, lstLeaf, root):
    if int(root.id) == int(idNode):
        return root
    for node in lstNode:
        if int(idNode) == int(node.id):
            return node
    for node in lstLeaf:
        if int(idNode) == int(node.id):
            return node
    return None

# Tìm vị trí khoảng cách nhỏ nhất
# vector: vector truyền vào
# lstVector: danh sách các vector so sánh với vector truyền vào
def findMinDistance(vector, lstVector):
    vt = 0
    min = computeDistanceEuclide(vector, lstVector[0].getVector())
    for i in range(1, len(lstVector)):
        if min > computeDistanceEuclide(vector, lstVector[i].getVector()):
            min = computeDistanceEuclide(vector, lstVector[i].getVector())
            vt = i
    return vt

# Tìm vị trí của lá trong danh sách
# idLeaf: id lá cần tìm
# lstLeaf: danh sách lá của cây
def findLeaf(idLeaf, lstLeaf):
    for i in range (0, len(lstLeaf)):
        if int(idLeaf) == int(lstLeaf[i].id):
            return i

def computeDistanceByCount(vectorA, vectorB):
    dem = 0
    for i in range(0, len(vectorA)):
        if abs(float(vectorA[i]) - float(vectorB[i])) < 3:
            dem += 1
    return dem

def findMatchDistance(vector, lstVector):
    vt = 0
    top = computeDistanceByCount(vector, lstVector[0].getVector())
    for i in range(1, len(lstVector)):
        if top < computeDistanceByCount(vector, lstVector[i].getVector()):
            top = computeDistanceByCount(vector, lstVector[i].getVector())
            vt = i
    return vt