import os

from uuid import uuid4

from flask import Flask, request, render_template, send_from_directory

from readXML import *

from student import SinhVien

from get_face_top_100 import findTop100, findImageInTree

import time

import requests

import json

sinhviens = []

sinhviens = readXML()

app = Flask(__name__)
# app = Flask(__name__, static_folder="images")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def checkMssvExist(listSV, mssv):
    for i in range(len(listSV)):
        if mssv == listSV[i].getMaHSSV():
            return [True, i]
    return [False, None]

@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    # target = os.path.join(APP_ROOT, 'static/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)
        # path = 'E:/Quang/Github/Image-Retrival/Investigate_Image_10kImages/data'

        # # fCountLinear = open('countLinear.txt', 'a+')
        # fCountTree = open('countTree.txt', 'a+')
        # # fTimeLinear = open('timeLinear.txt', 'a+')
        # fTimeTree = open('timeTree.txt', 'a+')
        # for i in range(0, 1686):
        #     # countLinear = 0
        #     # start = time.time()
        #     # lstImg, countLinear = findTop100(path + '/' + str(i) + '.jpg')
        #     # end = time.time()
        #     # timeLinearSearch = end - start
        #     countTree = 0
        #     start = time.time()
        #     lstImg, countTree = findImageInTree(path + '/' + str(i) + '.jpg')
        #     end = time.time()
        #     timeTreeSearch = end - start
        #     # fCountLinear.write(str(countLinear))
        #     # fCountLinear.write('\n')
        #     fCountTree.write(str(countTree))
        #     fCountTree.write('\n')
        #     # fTimeLinear.write(str(timeLinearSearch))
        #     # fTimeLinear.write('\n')
        #     fTimeTree.write(str(timeTreeSearch))
        #     fTimeTree.write('\n')
        #     print i

        # countLinear = 0
        # countTree = 0
        # lstImg, countLinear = findTop100(destination)
        lstImg, countTree = findImageInTree(destination)
        image_names = []
        # lstMSSV = []
        # for i in range(0, len(lstImg)):
        #     lstMSSV.append(sinhviens[int(lstImg[i])].getMaHSSV())
        # print lstMSSV
        for image in lstImg:
            image_names.append(str(image) + ".jpg")
        # print countLinear, countTree

        amount = len(lstImg)

    # return send_from_directory("images", filename, as_attachment=True)
    # return render_template("complete.html", image_name=filename)
    # image_names = os.listdir('./images')
    return render_template("gallery.html", filename=filename, image_names=image_names, amount=amount, lstMSSV=lstImg)


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("data", filename)


@app.route('/research/<filename>')
def result_image(filename):
    return send_from_directory("images", filename)


@app.route('/infostudent/<index>', methods=['GET', 'POST'])
def result(index):
    ms = index.split('.')[0]
    if request.method == 'POST':
        isExist, direct = checkMssvExist(sinhviens, ms)
        if isExist == True:
            # Edit SV
            sinhviens[direct].setHoDem(request.form['ho'])
            sinhviens[direct].setTen(request.form['ten'])
            sinhviens[direct].setGioiTinh(request.form['gt'])
            sinhviens[direct].setNgaySinh(request.form['ns'])
            sinhviens[direct].setNoiSinh(request.form['quequan'])
            sinhviens[direct].setMaLop(request.form['lop'])
            sinhviens[direct].setKhoaHoc(request.form['namvaohoc'])
            sinhviens[direct].setHe(request.form['he'])
            sinhviens[direct].setLoaiHinhDaoTao(request.form['loaidaotao'])
            sinhviens[direct].setNghe(request.form['khoa'])
            sinhviens[direct].setNganh(request.form['nganh'])
            sinhviens[direct].setTrangThai(request.form['trangthai'])
            editXML(sinhviens[direct])
            return render_template("info.html", sv=sinhviens[direct])
        else:
            # Add SV
            student = SinhVien()
            student.setMaHSSV(ms)
            student.setHoDem(request.form['ho'])
            student.setTen(request.form['ten'])
            student.setGioiTinh(request.form['gt'])
            student.setNgaySinh(request.form['ns'])
            student.setNoiSinh(request.form['quequan'])
            student.setMaLop(request.form['lop'])
            student.setKhoaHoc(request.form['namvaohoc'])
            student.setHe(request.form['he'])
            student.setLoaiHinhDaoTao(request.form['loaidaotao'])
            student.setNghe(request.form['khoa'])
            student.setNganh(request.form['nganh'])
            student.setTrangThai(request.form['trangthai'])
            student.setImg(index + ".jpg")
            sinhviens.append(student)
            writeXML(student)
            return render_template("info.html", sv=student)
    for i in range(len(sinhviens)):
        if ms == sinhviens[i].getMaHSSV():
            return render_template("info.html", sv=sinhviens[i])
    return render_template("not-found.html", mssv=ms)
    
@app.route('/addstudent/<index>', methods=['GET', 'POST'])
def add(index):
    image = index + ".jpg"
    return render_template("add-sv.html", img=image, mssv=index)

@app.route('/editstudent/<index>', methods=['GET', 'POST'])
def edit(index):
    for i in range(len(sinhviens)):
        if index == sinhviens[i].getMaHSSV():
            return render_template("edit-sv.html", sv=sinhviens[i])
    

if __name__ == "__main__":
    app.run(debug=True)
