from PyQt6 import QtCore, QtGui, QtWidgets
import subprocess
from getlocation import generate_route
class DetailButtonDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def paint(self, painter, option, index):
        super().paint(painter, option, index)
        rect = option.rect
        icon = QtGui.QIcon('path_to_your_icon')  # Replace 'path_to_your_icon' with the path to your icon
        icon_rect = QtCore.QRect(rect.right() - 20, rect.top(), 20, 20)  # Adjust the position of the icon
        icon.paint(painter, icon_rect)

class CustomListModel(QtCore.QAbstractListModel):
    def __init__(self, data=[], parent=None):
        super().__init__(parent)
        self._data = data

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._data)

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()]

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(543, 505)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 481, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label_5.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label_4.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.label_6 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 70, 481, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.textEdit_3 = QtWidgets.QTextEdit(parent=self.horizontalLayoutWidget_2)
        self.textEdit_3.setObjectName("textEdit_3")
        self.horizontalLayout_8.addWidget(self.textEdit_3)
        self.textEdit_6 = QtWidgets.QTextEdit(parent=self.horizontalLayoutWidget_2)
        self.textEdit_6.setObjectName("textEdit_6")
        self.horizontalLayout_8.addWidget(self.textEdit_6)
        self.textEdit_5 = QtWidgets.QTextEdit(parent=self.horizontalLayoutWidget_2)
        self.textEdit_5.setObjectName("textEdit_5")
        self.horizontalLayout_8.addWidget(self.textEdit_5)
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.horizontalLayoutWidget_2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_8.addWidget(self.textEdit_2)
        self.textEdit = QtWidgets.QTextEdit(parent=self.horizontalLayoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_8.addWidget(self.textEdit)
        self.textEdit_4 = QtWidgets.QTextEdit(parent=self.horizontalLayoutWidget_2)
        self.textEdit_4.setObjectName("textEdit_4")
        self.horizontalLayout_8.addWidget(self.textEdit_4)
        self.listView = QtWidgets.QListView(parent=Dialog)
        self.listView.setGeometry(QtCore.QRect(40, 210, 471, 221))
        self.listView.setObjectName("listView")
        self.model = CustomListModel()
        self.listView.setModel(self.model)
        self.listView.setItemDelegate(DetailButtonDelegate()) 
        
        
        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)
        self.listView.setItemDelegate(DetailButtonDelegate()) 
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(360, 110, 160, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_info_to_listview)
        self.horizontalLayout_9.addWidget(self.pushButton)
        
        # Add the "Route" button
        self.routeButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        self.routeButton.setObjectName("routeButton")
        self.routeButton.setText("Route")
        self.routeButton.clicked.connect(self.abc_info_to_listview)
        self.horizontalLayout_9.addWidget(self.routeButton)
        
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.dete_info)
        self.horizontalLayout_9.addWidget(self.pushButton_2)
        
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def open_route_map(self):
        # Open the route_map.html file
         self.abc_info_to_listview
    def dete_info(self):
        self.textEdit_3.clear()    
        self.textEdit_5.clear()    
        self.textEdit_6.clear()    
        self.textEdit_2.clear()    
        self.textEdit.clear()    
        self.textEdit_4.clear()    
    def add_info_to_listview(self):
        # Get information from input fields
        id_ = self.textEdit_3.toPlainText()
        ten_hang = self.textEdit_6.toPlainText()
        so_luong = self.textEdit_5.toPlainText()
        don_vi = self.textEdit_2.toPlainText()
        diem_nhan_hang = self.textEdit.toPlainText()
        diem_giao_hang = self.textEdit_4.toPlainText()

        # Create a string of information to display in the ListView
        info = f"ID: {id_}, Tên hàng: {ten_hang}, Số lượng: {so_luong}, Đơn vị: {don_vi}, Điểm nhận hàng: {diem_nhan_hang}, Điểm giao hàng: {diem_giao_hang}"
        
        # Create a data item
        item = QtGui.QStandardItem(info)
        
        # Add the data item to the model
        self.model.appendRow(item)
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "ID"))
        self.label_5.setText(_translate("Dialog", "Tên hàng"))
        self.label_4.setText(_translate("Dialog", "Số lượng"))
        self.label_3.setText(_translate("Dialog", "Đơn vị"))
        self.label.setText(_translate("Dialog", "Điển nhận hàng"))
        self.label_6.setText(_translate("Dialog", "Điểm giao hàng"))
        self.pushButton.setText(_translate("Dialog", "Nhập"))
        self.pushButton_2.setText(_translate("Dialog", "Hủy"))
        self.routeButton.setText(_translate("Dialog", "Lộ trình"))
    def abc_info_to_listview(self):
        # Lấy thông tin từ các ô nhập
        id_ = self.textEdit_3.toPlainText().strip()

        # Kiểm tra xem ID có tồn tại trong ListView không
        index = self.get_index_of_id(id_)
        if index.isValid():
            # Tìm thấy dòng có ID tương đương
            # Thực hiện các hành động cần thiết trên dòng đó
            # Ví dụ: Lấy thông tin từ dòng đó và hiển thị nó
            diem_nhan_hang = self.textEdit_4.toPlainText()
            diem_giao_hang = self.textEdit.toPlainText()
            subprocess.run(["python", "getlocation.py", diem_nhan_hang, diem_giao_hang])
            generate_route(diem_nhan_hang,diem_giao_hang)
            item_data = index.data()
            
            print("Đã tìm thấy dòng có ID tương đương:", item_data)
        else:
            print("Không tìm thấy dòng có ID tương đương trong ListView.")

    def get_index_of_id(self, target_id):
        # Lấy số hàng trong model
        row_count = self.model.rowCount()

        # Duyệt qua từng hàng để kiểm tra ID
        for row in range(row_count):
            index = self.model.index(row, 0)
            item_data = index.data()
            # Tách ID từ thông tin của mỗi hàng
            item_id = item_data.split(',')[0].split(':')[1].strip()
            # So sánh ID nhập với ID trong ListView
            if target_id == item_id:
                return index
        return QtCore.QModelIndex()  # Trả về QModelIndex không hợp lệ nếu không tìm thấy

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
