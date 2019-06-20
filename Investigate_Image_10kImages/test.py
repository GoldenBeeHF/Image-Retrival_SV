from xml.dom import minidom
from student import SinhVien
import xml.etree.ElementTree as ET
    
tree = ET.parse('dataSV.xml')  
root = tree.getroot()
 
print len(root.findall('sinhvien'))
