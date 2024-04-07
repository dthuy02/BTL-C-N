
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QApplication
import sys  
import sqlite3
from trangchu import Ui_MainWindow

#cửa sổ đăng nhập
class Dangnhap(QDialog):
    def __init__(self):
        super(Dangnhap,self).__init__()
        uic.loadUi("login.ui",self)
        self.dangnhapbtn.clicked.connect(self.ttdangnhap)
        self.dangkybtn1.clicked.connect(self.Dendangky)
    
    def ttdangnhap(self):
        dangnhap = self.dangnhap.text()
        matkhau = self.matkhau.text()

        if len(dangnhap)==0 or len(matkhau)==0:
            self.loi.setText("Hãy điền đầy đủ thông tin!")
        else:
            conn = sqlite3.connect("login-info.db")
            cur = conn.cursor()
            query = 'SELECT password FROM Dangnhap WHERE username =\''+ dangnhap+"\'"
            cur.execute(query)
            result_pass = cur.fetchone()[0]
            if result_pass == matkhau:
                QMessageBox.information(self, "Thông báo", "Đăng nhập thành công!")
                dntc = Trangchu()
                widget.addWidget(dntc)
                widget.setCurrentIndex(widget.currentIndex()+2)
            else:
                self.loi.setText("Tên đăng nhập hoặc mật khẩu không đúng!")


    # xử lý nút đăng ký tài khoản từ trang đăng nhập
    def Dendangky(self):
        dangkybtn1 = Dangky()
        widget.addWidget(dangkybtn1)
        widget.setCurrentIndex(1)

# cửa sổ đăng ký
class Dangky(QDialog):
    def __init__(self):
        super(Dangky,self).__init__()
        uic.loadUi("createacc.ui",self)
        self.dangkybtn.clicked.connect(self.ttdangky)

    def ttdangky(self):
        dangky = self.dangky.text()
        mkdk = self.mkdk.text()
        mkdk1 = self.mkdk1.text()
        if len(dangky) == 0 or len(mkdk) == 0 or len(mkdk1) == 0:
            self.loi1.setText("Hãy điền đầy đủ thông tin!")
        elif mkdk != mkdk1:
            self.loi1.setText("Mật khẩu không trùng khớp!")
        else:
            conn = sqlite3.connect("login-info.db")
            cur = conn.cursor()

            user_info = [dangky, mkdk]
            cur.execute('INSERT INTO Dangnhap (username, password) VALUES (?,?)', user_info)

            conn.commit()
            conn.close()
            QMessageBox.information(self, "Thông báo", "Đăng ký thành công!")

            #đăng ký thành công thì chuyển sang trang đăng nhập
            login = Dangnhap()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()-1)
# # #cửa sổ trang chủ
class Trangchu(QMainWindow):
    def __init__(self):
        super(Trangchu,self).__init__()
        # self.main_win = QMainWindow()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        # self.setWindowTitle("Trang chủ")
        uic.loadUi("main.ui",self)
        # self.setWindowTitle("Trang chủ")
    #     self.ui.stackedWidget_2.setCurrentWidget(self.ui.donhang)
    #     self.ui.donhangbtn.clicked.connect(self.chuyen_trang_don_hang)
    #     self.ui.lotrinhbtn.clicked.connect(self.chuyen_trang_lo_trinh)

    # def chuyen_trang_don_hang(self):
    #     self.ui.stackedWidget_2.setCurrentWidget(self.ui.donhang)
    # def chuyen_trang_lo_trinh(self):
    #     self.ui.stackedWidget_2.setCurrentWidget(self.ui.lotrinh)
        
        # def add_icon(self):
        #     user = QPixmap("user.png")
        #     self.user_lb.setPixmap(user)

        #     menu = QPixmap("menu.png")
        #     self.menubtn.setPixmap(menu)

        #     find = QPixmap("search-interface-symbol.png")
        #     self.findbtn.setPixmap(find)
            

        # # self.ui.icon_only_widget.hide()
        #     self.donhangbtn.clicked.connect(self.chuyen_trang_don_hang)
        # # self.donhangbtn_1.clicked.connect(self.chuyen_trang_don_hang)

        #     self.lotrinhbtn.clicked.connect(self.chuyen_trang_lo_trinh)
        # # self.lotrinhbtn1.clicked.connect(self.chuyen_trang_lo_trinh)

        #     self.thongbaobtn.clicked.connect(self.chuyen_trang_thong_bao)
        # # self.thongbaobtn1.clicked.connect(self.chuyen_trang_thong_bao)

        #     self.caidatbtn.clicked.connect(self.chuyen_trang_cai_dat)
        # # self.caidatbtn1.clicked.connect(self.chuyen_trang_cai_dat)

        #     def chuyen_trang_don_hang(self):
        #         self.stackedWidget.setCurrentIndex(0)

        #     def chuyen_trang_lo_trinh(self):
        #         self.stackedWidget.setCurrentIndex(1)
        #     def chuyen_trang_thong_bao(self):
        #         self.stackedWidget.setCurrentIndex(2)
        #     def chuyen_trang_cai_dat(self):
        #         self.stackedWidget.setCurrentIndex(3)
        
#xử lý
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
Login_f = Dangnhap()
ReLog_f = Dangky()
Main_f = Trangchu()

widget.addWidget(Login_f)
widget.addWidget(ReLog_f)
widget.addWidget(Main_f)

widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
app.exec()
