# This Python file uses the following encoding: utf-8
# Cấu trúc của cây STree
# Các class cần thiết trong đề tài
import math
import random
import types
import function

# Cấu trúc của 1 hình: gồm vector và id
class HOG:
    def __init__(self, vector, idImage):
        self.__vector = vector # private attribute
        self.__id = idImage # private attribute
    def getId(self):
        return self.__id
    def getVector(self):
        return self.__vector

class Vector:
    def __init__(self, vector, link):
        self.__vector = vector # private attribute
        self.__link = link # private attribute
    def getVector(self):
        return self.__vector
    def getLink(self):
        return self.__link
    def setVector(self, vector):
        self.__vector = vector

# Cấu trúc của 1 nút lá gồm:
# + n: số lượng phần tử
# + lstVector: danh sách các hình (class HOG)
class Leaf:
    def __init__(self, idLeaf):
        self.id = idLeaf
        self.n = 0
        self.lstImage = []
    
    def add(self, image):
        self.lstImage.append(image)
        self.n = self.n + 1

# Cấu trúc của 1 nút không phải lá trong cây:
# + n: số lượng phần tử
# + link: link tới nút con
# + lstVector: danh sách các vector (mỗi vector là 1 mảng 42 phần tử)
class Node:
    def __init__(self, idNode):
        self.id = idNode
        self.n = 0
        self.lstVector = []

    def add(self, vector):
        self.lstVector.append(vector)
        self.n = self.n + 1

# Cấu trúc cây STree:
# + root: nút gốc
# + lstLeaf: danh sách các nút lá
# + lstNode: danh sách các nút không phải lá và root trong cây
class STree:
    def __init__(self):
        self.m = 50
        self.countId = 0
        self.root = None
        self.lstLeaf = []
        self.lstNode = []

    def addRoot(self, root):
        self.root = root

    # thêm hình ảnh vào cây
    def addImage(self, image):
        # cut root if n >= m
        if (self.root.n >= self.m):
            self.cutRoot()
        if (self.root.__class__.__name__ == "Leaf"):
                self.root.add(image)
        else:
            t = self.root
            tempVector = image.getVector()
            lstLink = []
            lstVtLink = []
            lstLink.append(t.id)
            while True:
                # tìm vị trí khoảng cách nhỏ nhất
                direct = function.findMinDistance(tempVector, t.lstVector)
                # thêm vị trí vào danh sách tạm để quay lui sau khi thêm hình
                lstVtLink.append(direct)
                # tìm node link tới dựa vào vị trí vector có khoảng cách gần với vector ảnh truyền vào nhất
                t = function.findNode(t.lstVector[direct], self.lstNode, self.lstLeaf)
                if t.__class__.__name__ == "Leaf":
                    break
                lstLink.append(t.id)

            # thêm ảnh vào lá link tới
            vt = function.findLeaf(t.id, self.lstLeaf)
            self.lstLeaf[int(vt)].add(image)
            count = 1
            tNode = self.lstLeaf[int(vt)]
            # tính toán lại vector trung bình
            node = function.findNodeById(lstLink[len(lstLink) - count], self.lstNode, self.lstLeaf, self.root)
            node.lstVector[int(lstVtLink[len(lstVtLink) - count])].setVector(function.computeAvgVector(tNode.lstImage))
            if (node != self.root):
                count = count + 1
                tNode = node
                while True:
                    node = function.findNodeById(lstLink[len(lstLink) - count], self.lstNode, self.lstLeaf, self.root)
                    node.lstVector[int(lstVtLink[len(lstVtLink) - count])].setVector(function.computeAvgVector(tNode.lstVector))
                    count = count + 1
                    if node == self.root:
                        break
                    tNode = node

            # while True:
            #     node = function.findNodeById(lstLink[len(lstLink) - count], self.lstNode, self.lstLeaf, self.root)
            #     node.lstVector[int(lstVtLink[len(lstVtLink) - count])].setVector(function.computeAvgVector(tNode.lstImage))
            #     count = count + 1
            #     if node == self.root:
            #         break
            #     node = tNode

            # kiểm tra số lượng phần tử sau khi thêm hình để tách lá
            if self.lstLeaf[int(vt)].n == self.m:
                self.cutLeaf(self.lstLeaf[int(vt)], lstLink, lstVtLink)
                lstLink.reverse()
                lstVtLink.reverse()
                for i in range(0, len(lstLink)):
                    node = function.findNodeById(lstLink[i], self.lstNode, self.lstLeaf, self.root)
                    if node.n < self.m:
                        break
                    else:
                        if (node == self.root):
                            self.cutRoot()
                            return
                        else:
                            temp = self.cutNode(node, lstLink[i + 1], lstVtLink[i + 1])
                            if temp == self.root:
                                return
                            c = 2

                            while True:
                                tempNode = function.findNodeById(lstLink[i + c], self.lstNode, self.lstLeaf, self.root)
                                tempNode.lstVector[int(lstVtLink[i + c])].setVector(function.computeAvgVector(temp.lstVector))
                                c = c + 1
                                if tempNode == self.root:
                                    break
                                temp = tempNode

    # cắt nút root
    def cutRoot(self):
        if self.root.__class__.__name__ == "Leaf":
            # Tìm 2 vector có khoảng cách lớn nhất tạo thành 2 cụm
            cluster = function.findMaxDistance(self.root.lstImage)
            clusterA = Leaf(self.countId)
            self.countId = self.countId + 1
            clusterA.add(cluster[0])
            clusterB = Leaf(self.countId)
            self.countId = self.countId + 1
            clusterB.add(cluster[1])
            self.lstLeaf.append(clusterA)
            self.lstLeaf.append(clusterB)

            # Đưa các vector vào 2 cụm vừa tạo
            for hog in self.root.lstImage:
                if (int(hog.getId()) == int(cluster[0].getId())):
                    continue
                if (int(hog.getId()) == int(cluster[1].getId())):
                    continue

                if (function.computeDistanceEuclide(hog.getVector(), cluster[0].getVector())
                    > function.computeDistanceEuclide(hog.getVector(), cluster[1].getVector())):
                    clusterA.add(hog)
                else:
                    clusterB.add(hog)

            # thay thế nút root mới
            t = Node(self.root.id)
            self.root = t
            self.root.add(function.computeAvgVector(clusterA.lstImage, clusterA.id))
            self.countId = self.countId + 1
            self.root.add(function.computeAvgVector(clusterB.lstImage, clusterB.id))
            self.countId = self.countId + 1
        else:
            # Tìm 2 vector có khoảng cách lớn nhất tạo thành 2 cụm
            cluster = function.findMaxDistance(self.root.lstVector)
            clusterA = Node(self.countId)
            self.countId = self.countId + 1
            clusterA.add(cluster[0])
            clusterB = Node(self.countId)
            self.countId = self.countId + 1
            clusterB.add(cluster[1])
            self.lstNode.append(clusterA)
            self.lstNode.append(clusterB)
            
            # Đưa các vector vào 2 cụm vừa tạo
            for v in self.root.lstVector:
                if (int(v.getLink()) == int(cluster[0].getLink())):
                    continue
                if (int(v.getLink()) == int(cluster[1].getLink())):
                    continue

                if (function.computeDistanceEuclide(v.getVector(), cluster[0].getVector())
                    > function.computeDistanceEuclide(v.getVector(), cluster[1].getVector())):
                    clusterA.add(v)
                else:
                    clusterB.add(v)
            
            
            # thay thế nút root mới
            t = Node(self.root.id)
            self.root = t
            self.root.add(function.computeAvgVector(clusterA.lstVector, clusterA.id))
            self.countId = self.countId + 1
            self.root.add(function.computeAvgVector(clusterB.lstVector, clusterB.id))
            self.countId = self.countId + 1

    # Cắt nút Node
    def cutNode(self, node, nodeLink, vtNodeLink):
        # Tìm 2 vector có khoảng cách lớn nhất tạo thành 2 cụm
        cluster = function.findMaxDistance(node.lstVector)
        clusterA = Node(self.countId)
        # self.countId = self.countId + 1
        clusterA.add(cluster[0])
        clusterB = Node(self.countId)
        self.countId = self.countId + 1
        clusterB.add(cluster[1])
        # self.lstNode.append(clusterA)
        # self.lstNode.append(clusterB)
        # self.lstNode.remove(node)

        # Đưa các vector vào 2 cụm vừa tạo
        for v in node.lstVector:
            if (int(v.getLink()) == int(cluster[0].getLink())):
                continue
            if (int(v.getLink()) == int(cluster[1].getLink())):
                continue

            if (function.computeDistanceEuclide(v.getVector(), cluster[0].getVector())
                > function.computeDistanceEuclide(v.getVector(), cluster[1].getVector())):
                clusterA.add(v)
            else:
                clusterB.add(v)
        
        node.lstVector = []
        node.lstVector = clusterA.lstVector
        node.n = clusterA.n

        self.lstNode.append(clusterB)
        
        # thay thế vector ở nút link tới bằng 2 vector khác dựa vào 2 cụm vừa tạo
        node = function.findNodeById(nodeLink, self.lstNode, self.lstLeaf, self.root)
        node.lstVector[vtNodeLink].setVector(function.computeAvgVector(clusterA.lstVector))
        # node.lstVector.remove(node.lstVector[vtNodeLink])
        # node.add(function.computeAvgVector(clusterA.lstVector, clusterA.id))
        node.add(function.computeAvgVector(clusterB.lstVector, clusterB.id))
        # node.n = node.n - 1
        return node

    # Cắt nút Leaf
    def cutLeaf(self, leaf, lstLink, lstVtLink):
        # Tìm 2 vector có khoảng cách lớn nhất tạo thành 2 cụm
        cluster = function.findMaxDistance(leaf.lstImage)
        clusterA = Leaf(self.countId)
        # self.countId = self.countId + 1
        clusterA.add(cluster[0])
        clusterB = Leaf(self.countId)
        self.countId = self.countId + 1
        clusterB.add(cluster[1])
        # self.lstLeaf.append(clusterA)
        # self.lstLeaf.append(clusterB)

        # Đưa các vector vào 2 cụm vừa tạo
        for hog in leaf.lstImage:
            if (int(hog.getId()) == int(cluster[0].getId())):
                continue
            if (int(hog.getId()) == int(cluster[1].getId())):
                continue

            if (function.computeDistanceEuclide(hog.getVector(), cluster[0].getVector())
                > function.computeDistanceEuclide(hog.getVector(), cluster[1].getVector())):
                clusterA.add(hog)
            else:
                clusterB.add(hog)
        
        leaf.lstImage = []
        leaf.lstImage = clusterA.lstImage
        leaf.n = clusterA.n

        self.lstLeaf.append(clusterB)

        # thay thế vector ở nút link tới bằng 2 vector khác dựa vào 2 cụm vừa tạo
        count = 1
        node = function.findNodeById(lstLink[len(lstLink) - count], self.lstNode, self.lstLeaf, self.root)
        node.lstVector[int(lstVtLink[len(lstVtLink) - count])].setVector(function.computeAvgVector(clusterA.lstImage))
        # node.lstVector.remove(node.lstVector[int(lstVtLink[len(lstVtLink) - count])])
        # node.add(function.computeAvgVector(clusterA.lstImage, clusterA.id))
        node.add(function.computeAvgVector(clusterB.lstImage, clusterB.id))
        
        # node.n = node.n - 1
        # self.lstLeaf.remove(leaf) # Xóa nút lá cũ
        if node == self.root:
            return
        count = count + 1
        # tính toán lại vector trung bình
        while True:
            tempNode = function.findNodeById(lstLink[len(lstLink) - count], self.lstNode, self.lstLeaf, self.root)
            tempNode.lstVector[int(lstVtLink[len(lstVtLink) - count])].setVector(function.computeAvgVector(node.lstVector))
            if tempNode == self.root:
                break
            count = count + 1            
            node = tempNode