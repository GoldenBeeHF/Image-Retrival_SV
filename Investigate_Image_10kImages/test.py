from xml.dom import minidom
from student import SinhVien
import xml.etree.ElementTree as ET

tree = ET.parse('dataSV.xml')  
root = tree.getroot()
# for elem in root.iter('Data'):  
#     elem.set(name,xsi)


for elem in root.iter('sinhvien'):  
    elem.set('name2', 'newitem2')
        # if we know the name of the attribute, access it directly
        # print(subelem)
    # adding an element to the root node
    # attrib = {}  
    # element = root.makeelement(nameEle, attrib)  
    # root.append(element)

    # # adding an element to the seconditem node 
    # subelement = root[0][1].makeelement(nameEle, attrib)  

    # ET.SubElement(root[index], 'MSSV', attrib)  
    # root[index][0].text = sinhvien.getMaHSSV()

    # ET.SubElement(root[index], 'HO', attrib)
    # root[index][1].text = sinhvien.getHoDem()

    # ET.SubElement(root[index], 'TEN', attrib)  
    # root[index][2].text = sinhvien.getTen()

    # ET.SubElement(root[index], 'GT', attrib)
    # root[index][3].text = sinhvien.getGioiTinh()

    # ET.SubElement(root[index], 'NS', attrib)
    # root[index][4].text = sinhvien.getNgaySinh()

    # ET.SubElement(root[index], 'NOISINH', attrib)
    # root[index][5].text = sinhvien.getNoiSinh()

    # ET.SubElement(root[index], 'LOP', attrib)  
    # root[index][6].text = sinhvien.getMaLop()

    # ET.SubElement(root[index], 'NAM', attrib)
    # root[index][7].text = sinhvien.getKhoaHoc()

    # ET.SubElement(root[index], 'HE', attrib)  
    # root[index][8].text = sinhvien.getHe()

    # ET.SubElement(root[index], 'LOAIHINHDAOTAO', attrib)
    # root[index][9].text = sinhvien.getLoaiHinhDaoTao()

    # ET.SubElement(root[index], 'KHOA', attrib)
    # root[index][10].text = sinhvien.getNghe()

    # ET.SubElement(root[index], 'NGANH', attrib)
    # root[index][11].text = sinhvien.getNganh()

    # ET.SubElement(root[index], 'TINHTRANG', attrib)
    # root[index][12].text = sinhvien.getTrangThai()

    # # create a new XML file with the new element
    # tree.write('dataSV.xml',encoding="UTF-8",xml_declaration=True)