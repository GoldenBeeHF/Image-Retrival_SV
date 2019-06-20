from xml.dom import minidom
from student import SinhVien
import xml.etree.ElementTree as ET
# parse an xml file by name


def readXML():
    sinhviens = []

    mydoc = minidom.parse('dataSV.xml')

    dataSV = mydoc.getElementsByTagName('Data')
    # all item attributes

    svs = mydoc.getElementsByTagName("sinhvien")
    flag = 0
    # i = 0
    for i in range(len(svs)):
        sinhvien = SinhVien()
        sinhvien.setMaHSSV(svs[i].getElementsByTagName(
            "MSSV")[0].firstChild.data)
        try:
            sinhvien.setHoDem(svs[i].getElementsByTagName(
            "HO")[0].firstChild.data)
        except:
            sinhvien.setHoDem("")
        try:
            sinhvien.setTen(svs[i].getElementsByTagName("TEN")[0].firstChild.data)
        except:
            sinhvien.setTen("")
        try:
            sinhvien.setGioiTinh(svs[i].getElementsByTagName(
            "GT")[0].firstChild.data)
        except:
            sinhvien.setGioiTinh("")
        try:
            sinhvien.setNgaySinh(svs[i].getElementsByTagName(
            "NS")[0].firstChild.data)
        except:
            sinhvien.setNgaySinh("")
        try:
            sinhvien.setKhoaHoc(svs[i].getElementsByTagName(
            "NAM")[0].firstChild.data)
        except:
            sinhvien.setKhoaHoc("")
        try:
            sinhvien.setNoiSinh(svs[i].getElementsByTagName(
                "NOISINH")[0].firstChild.data)
        except:
            sinhvien.setNoiSinh("")
        try:
            sinhvien.setMaLop(svs[i].getElementsByTagName(
            "LOP")[0].firstChild.data)
        except:
            sinhvien.setMaLop("")
        try:
            sinhvien.setTrangThai(svs[i].getElementsByTagName(
            "TINHTRANG")[0].firstChild.data)
        except:
            sinhvien.setTrangThai("")
        try:
            sinhvien.setNghe(svs[i].getElementsByTagName(
            "KHOA")[0].firstChild.data)
        except:
            sinhvien.setNghe("")
        try:
            sinhvien.setNganh(svs[i].getElementsByTagName(
            "NGANH")[0].firstChild.data)
        except:
            sinhvien.setNganh("")
        try:
            sinhvien.setHe(svs[i].getElementsByTagName(
            "HE")[0].firstChild.data)
        except:
            sinhvien.setHe("")
        try:
            sinhvien.setLoaiHinhDaoTao(svs[i].getElementsByTagName(
            "LOAIHINHDAOTAO")[0].firstChild.data)
        except:
            sinhvien.setLoaiHinhDaoTao("")
        # sinhvien.setNgayNhapHoc(svs[i].getElementsByTagName(
        sinhvien.setImg(str(sinhvien.getMaHSSV()) + ".jpg")

        sinhviens.append(sinhvien)

    return sinhviens

def writeXML(sinhvien):
    
    xsi =  "http://www.w3.org/2001/XMLSchema-instance"
    name = "xmlns:xsi"
    tree = ET.parse('dataSV.xml')  
    root = tree.getroot()
    for elem in root.iter('Data'):  
        elem.set(name,xsi)

    nameEle = 'sinhvien'
    index = len(root.findall(nameEle))
    # adding an element to the root node
    attrib = {}  
    element = root.makeelement(nameEle, attrib)  
    root.append(element)

    # adding an element to the seconditem node 
    subelement = root[0][1].makeelement(nameEle, attrib)  

    ET.SubElement(root[index], 'MSSV', attrib)  
    root[index][0].text = sinhvien.getMaHSSV()

    ET.SubElement(root[index], 'HO', attrib)
    root[index][1].text = sinhvien.getHoDem()

    ET.SubElement(root[index], 'TEN', attrib)  
    root[index][2].text = sinhvien.getTen()

    ET.SubElement(root[index], 'GT', attrib)
    root[index][3].text = sinhvien.getGioiTinh()

    ET.SubElement(root[index], 'NS', attrib)
    root[index][4].text = sinhvien.getNgaySinh()

    ET.SubElement(root[index], 'NOISINH', attrib)
    root[index][5].text = sinhvien.getNoiSinh()

    ET.SubElement(root[index], 'LOP', attrib)  
    root[index][6].text = sinhvien.getMaLop()

    ET.SubElement(root[index], 'NAM', attrib)
    root[index][7].text = sinhvien.getKhoaHoc()

    ET.SubElement(root[index], 'HE', attrib)  
    root[index][8].text = sinhvien.getHe()

    ET.SubElement(root[index], 'LOAIHINHDAOTAO', attrib)
    root[index][9].text = sinhvien.getLoaiHinhDaoTao()

    ET.SubElement(root[index], 'KHOA', attrib)
    root[index][10].text = sinhvien.getNghe()

    ET.SubElement(root[index], 'NGANH', attrib)
    root[index][11].text = sinhvien.getNganh()

    ET.SubElement(root[index], 'TINHTRANG', attrib)
    root[index][12].text = sinhvien.getTrangThai()

    # create a new XML file with the new element
    tree.write('dataSV.xml',encoding="UTF-8",xml_declaration=True)

def editXML(sinhviens):
    
    xsi =  "http://www.w3.org/2001/XMLSchema-instance"
    name = "xmlns:xsi"
    tree = ET.parse('dataSV.xml')  
    root = tree.getroot()
    for elem in root:  
        for subelem in elem.findall('sinhvien'):
            print(subelem.get('MSSV'))
   