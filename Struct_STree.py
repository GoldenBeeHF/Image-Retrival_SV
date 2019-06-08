# This Python file uses the following encoding: utf-8
# Task tạo cây STree cải thiện tốc độ tìm kiếm hình ảnh của khóa luận
# Người thực hiện: Trần Lê Văn Đức
# Thời gian thực hiện: đến hết thứ 4, ngày 13 tháng 3 năm 2019
# Yêu cầu làm việc nghiêm túc !!!

# Các bước tạo cây:
# B1: Tạo nút root của cây. Thêm hình (HOG) đầu tiên vào. Cho sức chứa là 20 (quá 20 sẽ tách nút).
# B2: Thêm lần lượt các hình tiếp theo vào. Khi vượt quá 20 sẽ tách nút.
# Cách tách: chọn 2 vector xa nhau nhất tạo thành 2 nút. Đưa các vector còn lại vào 2 nút vừa tạo
# Quy tắc: gần nút nào sẽ gom vào nút đó.
# B3: Sau đó tính vector trung bình của mỗi nút.
# Cách tính: cộng tuyến tính các thành phần của vector sau đó chia trung bình
# Vd: v1 = (x1, x2, ..., xN), v2 = (y1, y2, ..., yN)
# vTB = ((x1 + y1) / 2, (x2 + y2) / 2, ..., (xN + yN) / 2)
# B4: Tạo nút mới với các phần tử là 2 vector trung bình vừa tính. Link 2 vector trung bình với nút con.
# B5: Tiếp tục thêm hình vào cây.
# Cách thêm: mỗi hình đưa vào sẽ so sánh với 2 vector trung bình vừa tạo xem gần vector nào hơn.
# Sau đó sẽ theo đường link và thêm xuống nút lá.
# Khi thêm xuống nút lá phải tiến hành tính lại vector trung bình.
# Cứ tiếp tục thêm đến khi tràn nút lá thì lại tiếp tục tách nút.
# 2 vector trung bình lấy được sẽ được thêm vào root.
# Khi nút root tràn sẽ tách nút root. Tương tự làm tiếp tục.

import struct
import random
import function
import os
import time
start = time.time()
f = open('training.txt', 'a+')
data = f.read()
arr = data.split()
print len(arr)

lst = []
countImage = 0
for i in range(0, 1681):
    vector = []
    for j in range(0, 42):
        vector.append(float(arr[42 * countImage + j]))
    countImage = countImage + 1
    a = struct.HOG(vector, i)
    lst.append(a)

tree = struct.STree()
tree.root = struct.Leaf(tree.countId)
tree.countId = tree.countId + 1

for image in lst:
    tree.addImage(image)
# print "Root"
# for v in tree.root.lstVector:
#     print v.getLink(), v.getVector()
# for node in tree.lstNode:
#     print "Node", node.id
#     for v in node.lstVector:
#         print v.getLink(), v.getVector()

# def makeDirInNode(curDir, node, tree):
#     if node == tree.root:
#         os.makedirs("Root")
#         curDir = "Root"
#     if node.__class__.__name__ == "Node":
#         os.makedirs(curDir + "/" + "Node_id_" + str(node.id))
#         curDir = curDir + "/" + "Node_id_" + str(node.id)
#         for v in node.lstVector:
#             if not os.path.exists(curDir + "/" + "Vector_link_" + str(v.getLink())):
#                 os.makedirs(curDir + "/" + "Vector_link_" + str(v.getLink()))
#             node = function.findNodeById(v.getLink(), tree.lstLeaf, tree.lstNode, tree.root)
#             makeDirInNode(curDir + "/" + "Vector_link_" + str(v.getLink()), node, tree)
#     else:
#         os.makedirs(curDir + "/" + "Leaf_id_" + str(node.id))
#         curDir = curDir + "/" + "Leaf_id_" + str(node.id)
#         for v in node.lstImage:
#             if not os.path.exists(curDir + "/" + "Image_id_" + str(v.getId())):
#                 os.makedirs(curDir + "/" + "Image_id_" + str(v.getId()))

# makeDirInNode("", tree.root, tree)

f = open("root.txt", "wb")
for v in tree.root.lstVector:
    f.write(str(v.getLink()) + " ")
    for value in v.getVector():
        f.write(str(value) + " ")
    f.write('\n')

f.close()
os.makedirs('Node')
for node in tree.lstNode:
    f1 = open('Node/' + str(node.id) + '.txt', 'wb')
    f1.write('Node\n')
    for v in node.lstVector:
        f1.write(str(v.getLink()) + ' ')
        for value in v.getVector():
            f1.write(str(value) + ' ')
        f1.write('\n')
    f1.close()

os.makedirs('Leaf')
for leaf in tree.lstLeaf:
    f2 = open('Leaf/' + str(leaf.id) + '.txt', 'wb')
    f2.write('Leaf\n')
    for v in leaf.lstImage:
        f2.write(str(v.getId()) + ' ')
        for value in v.getVector():
            f2.write(str(value) + ' ')
        f2.write('\n')
    f2.close()
end = time.time()

print end - start

        

