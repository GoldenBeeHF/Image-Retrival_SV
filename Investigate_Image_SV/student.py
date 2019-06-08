class SinhVien:
    # filed
	STT             = 1
	MaHSSV          = 2001160163 
	HoDem           = "Capit\xe1n\n"
	Ten             = "Capit\xe1n\n"
	GioiTinh        = "Capit\xe1n\n"
	NgaySinh        = "24/01/1997"
	NgayNhapHoc     = "29/08/2016"
	NoiSinh         = "Capit\xe1n\n"
	NguyenQuan      = "Capit\xe1n\n"
	DanToc          = "Capit\xe1n\n"
	TonGiao         = "Capit\xe1n\n"
	HoKhauThuongTru = "Capit\xe1n\n"
	DiaChiLienLac   = "Capit\xe1n\n"
	# KhuVuc          = "KV1"
	# TenPhanHe       = "Capit\xe1n\n"
	# NgayVaoDoan     = "42286"
	# NgayVaoDang     = "30/06/2020"
	# SoCMND          = "12345"
	# NgayCap         = "42591"
	# NoiCap          = "Tp.HCM"
	MaLop           = "07DHTH2"
	KhoaHoc         = 2016
	BacDaoTao       = "Capit\xe1n\n"
	LoaiDaoTao      = "Capit\xe1n\n"
	Nganh           = "Capit\xe1n\n"
	Nghe            = "Capit\xe1n\n"
	NienKhoa        = "2016-2020"
	# NgaySinhCha     = "1965"
	# HoTenCha        = "Capit\xe1n\n"
	# NgheNghiepCha   = "Capit\xe1n\n"
	# NgaySinhMe      = "1967"
	# HoTenMe         = "Capit\xe1n\n"
	# NgheNghiepMe    = "May"
	DienThoai       = "0974112161"
	Email           = "daulaudoan@gmail.com"
	TrangThai       = "Capit\xe1n\n"
	Img             = "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
    
	#method
	def setSTT(self, STT):
		self.STT = int(STT) - 1
	def getSTT(self):
		return self.STT
	def setImg(self, Img):
		self.Img = Img
	def getImg(self):
		return self.Img
	def setMaHSSV(self, MaHSSV):
		self.MaHSSV = MaHSSV
	def getMaHSSV(self):
		return self.MaHSSV
	def setTen(self, Ten):
		self.Ten = Ten
	def getTen(self):
		return self.Ten
	def setHoDem(self, HoDem):
		self.HoDem = HoDem
	def getHoDem(self):
		return self.HoDem
	def setGioiTinh(self, GioiTinh):
		self.GioiTinh = GioiTinh
	def getGioiTinh(self):
		return self.GioiTinh
	def setNgayNhapHoc(self, NgayNhapHoc):
		self.NgayNhapHoc = NgayNhapHoc
	def getNgayNhapHoc(self):
		return self.NgayNhapHoc
	def setNgaySinh(self, NgaySinh):
		self.NgaySinh = NgaySinh
	def getNgaySinh(self):
		return self.NgaySinh
	def setNoiSinh(self, NoiSinh):
		if NoiSinh is None:
			self.NoiSinh = NoiSinh
		else:
			self.NoiSinh = "Not Found"
	def getNoiSinh(self):
		return self.NoiSinh
	def setNguyenQuan(self, NguyenQuan):
		self.NguyenQuan = NguyenQuan
	def getNguyenQuan(self):
		return self.NguyenQuan
	def setDanToc(self, DanToc):
		self.DanToc = DanToc
	def getDanToc(self):
		return self.DanToc
	def setTonGiao(self, TonGiao):
		self.TonGiao = TonGiao
	def getTonGiao(self):
		return self.TonGiao
	def setHoKhauThuongTru(self, HoKhauThuongTru):
		self.HoKhauThuongTru = HoKhauThuongTru
	def getHoKhauThuongTru(self):
		return self.HoKhauThuongTru
	def setDiaChiLienLac(self, DiaChiLienLac):
		self.DiaChiLienLac = DiaChiLienLac
	def getDiaChiLienLac(self):
		return self.DiaChiLienLac
	def setMaLop(self, MaLop):
		self.MaLop = MaLop
	def getMaLop(self):
		return self.MaLop
	def setKhoaHoc(self, KhoaHoc):
		self.KhoaHoc = KhoaHoc
	def getKhoaHoc(self):
		return self.KhoaHoc
	def setBacDaoTao(self, BacDaoTao):
		self.BacDaoTao = BacDaoTao
	def getBacDaoTao(self):
		return self.BacDaoTao
	def setLoaiDaoTao(self, LoaiDaoTao):
		self.LoaiDaoTao = LoaiDaoTao
	def getLoaiDaoTao(self):
		return self.LoaiDaoTao
	def setNganh(self, Nganh):
		self.Nganh = Nganh
	def getNganh(self):
		return self.Nganh
	def setNghe(self, Nghe):
		self.Nghe = Nghe
	def getNghe(self):
		return self.Nghe
	def setNienKhoa(self, NienKhoa):
		self.NienKhoa = NienKhoa
	def getNienKhoa(self):
		return self.NienKhoa
	def setDienThoai(self, DienThoai):
		self.DienThoai = DienThoai
	def getDienThoai(self):
		return self.DienThoai
	def setEmail(self, Email):
		self.Email = Email
	def getEmail(self):
		return self.Email
	def setTrangThai(self, TrangThai):
		self.TrangThai = TrangThai
	def getTrangThai(self):
		return self.TrangThai
	def setKhuVuc(self, KhuVuc):
		self.KhuVuc = KhuVuc
	def getKhuVuc(self):
		return self.KhuVuc
	def setKhuVuc(self, KhuVuc):
		self.KhuVuc = KhuVuc
	def getKhuVuc(self):
		return self.KhuVuc
	def setTenPhanHe(self, TenPhanHe):
		self.TenPhanHe = TenPhanHe
	def getTenPhanHe(self):
		return self.TenPhanHe	