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
    i = 0
    for dem in range(3000):
        sinhvien = SinhVien()
        stt = svs[i].getElementsByTagName("STT")[0].firstChild.data
        sinhvien.setSTT(int(stt) + int(flag*310))
        sinhvien.setMaHSSV(svs[i].getElementsByTagName(
            "MaHSSV")[0].firstChild.data)
        sinhvien.setHoDem(svs[i].getElementsByTagName(
            "HoDem")[0].firstChild.data)
        sinhvien.setTen(svs[i].getElementsByTagName("Ten")[0].firstChild.data)
        sinhvien.setGioiTinh(svs[i].getElementsByTagName(
            "GioiTinh")[0].firstChild.data)
        sinhvien.setNgaySinh(svs[i].getElementsByTagName(
            "NgaySinh")[0].firstChild.data)
        sinhvien.setKhoaHoc(svs[i].getElementsByTagName(
            "KhoaHoc")[0].firstChild.data)
        try:
            sinhvien.setHoKhauThuongTru(svs[i].getElementsByTagName(
                "HoKhauThuongTru")[0].firstChild.data)
        except:
            sinhvien.setHoKhauThuongTru("")
        sinhvien.setDiaChiLienLac(svs[i].getElementsByTagName(
            "DiaChiLienLac")[0].firstChild.data)
        sinhvien.setTrangThai(svs[i].getElementsByTagName(
            "TrangThai")[0].firstChild.data)
        sinhvien.setNgayNhapHoc(svs[i].getElementsByTagName(
            "NgayNhapHoc")[0].firstChild.data)
        sinhvien.setBacDaoTao(svs[i].getElementsByTagName(
            "BacDaoTao")[0].firstChild.data)
        sinhvien.setNganh(svs[i].getElementsByTagName(
            "Nganh")[0].firstChild.data)
        sinhvien.setNoiSinh(svs[i].getElementsByTagName(
            "NguyenQuan")[0].firstChild.data)
        sinhvien.setTonGiao(svs[i].getElementsByTagName(
            "TonGiao")[0].firstChild.data)
        sinhvien.setDienThoai(svs[i].getElementsByTagName(
            "DienThoai")[0].firstChild.data)
        try:
            sinhvien.setEmail(svs[i].getElementsByTagName(
                "Email")[0].firstChild.data)
        except:
            sinhvien.setEmail("")
        sinhvien.setImg(str(sinhvien.getSTT()) + ".jpg")
        sinhviens.append(sinhvien)
        i = i + 1
        if(i > 309):
            flag = flag + 1
            i = 0

    return sinhviens
