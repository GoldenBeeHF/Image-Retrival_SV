from xml.dom import minidom
from student import SinhVien
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
        sinhvien.setHoDem(svs[i].getElementsByTagName(
            "HO")[0].firstChild.data)
        sinhvien.setTen(svs[i].getElementsByTagName("TEN")[0].firstChild.data)
        sinhvien.setGioiTinh(svs[i].getElementsByTagName(
            "GT")[0].firstChild.data)
        try:
            sinhvien.setNgaySinh(svs[i].getElementsByTagName(
            "NS")[0].firstChild.data)
        except:
            sinhvien.setNgaySinh("")
        sinhvien.setKhoaHoc(svs[i].getElementsByTagName(
            "NAM")[0].firstChild.data)
        try:
            sinhvien.setNoiSinh(svs[i].getElementsByTagName(
                "NOISINH")[0].firstChild.data)
        except:
            sinhvien.setNoiSinh("")
        sinhvien.setMaLop(svs[i].getElementsByTagName(
            "LOP")[0].firstChild.data)
        sinhvien.setTrangThai(svs[i].getElementsByTagName(
            "TINHTRANG")[0].firstChild.data)
        sinhvien.setNghe(svs[i].getElementsByTagName(
            "KHOA")[0].firstChild.data)
        sinhvien.setNganh(svs[i].getElementsByTagName(
            "NGANH")[0].firstChild.data)
        # sinhvien.setNgayNhapHoc(svs[i].getElementsByTagName(
        sinhvien.setImg(str(sinhvien.getMaHSSV()) + ".jpg")

        sinhviens.append(sinhvien)

    return sinhviens
