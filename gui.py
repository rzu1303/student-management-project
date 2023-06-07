# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 600)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(260, 10, 281, 31))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(MainWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 50, 781, 531))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_left = QtWidgets.QVBoxLayout()
        self.verticalLayout_left.setSpacing(15)
        self.verticalLayout_left.setObjectName("verticalLayout_left")
        self.formLayout_ = QtWidgets.QFormLayout()
        self.formLayout_.setContentsMargins(5, 5, 5, 5)
        self.formLayout_.setSpacing(5)
        self.formLayout_.setObjectName("formLayout_")
        self.label_name = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.formLayout_.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_name)
        self.lineEdit_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.formLayout_.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name)
        self.label_mobile = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_mobile.setFont(font)
        self.label_mobile.setObjectName("label_mobile")
        self.formLayout_.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_mobile)
        self.lineEdit_mobile = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_mobile.setObjectName("lineEdit_mobile")
        self.formLayout_.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_mobile)
        self.label_email = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")
        self.formLayout_.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_email)
        self.lineEdit_email = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.formLayout_.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_email)
        self.label_gender = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_gender.setFont(font)
        self.label_gender.setObjectName("label_gender")
        self.formLayout_.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_gender)
        self.label_bdate = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_bdate.setFont(font)
        self.label_bdate.setObjectName("label_bdate")
        self.formLayout_.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_bdate)
        self.dateEdit_bdate = QtWidgets.QDateEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_bdate.setFont(font)
        self.dateEdit_bdate.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_bdate.setDate(QtCore.QDate(2000, 1, 1))
        self.dateEdit_bdate.setObjectName("dateEdit_bdate")
        self.formLayout_.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateEdit_bdate)
        self.pushButton_update = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_update.setFont(font)
        self.pushButton_update.setObjectName("pushButton_update")
        self.formLayout_.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.pushButton_update)
        self.pushButton_submit = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_submit.setFont(font)
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.formLayout_.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pushButton_submit)
        self.comboBox_gender = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_gender.setObjectName("comboBox_gender")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.addItem("")
        self.formLayout_.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_gender)
        self.verticalLayout_left.addLayout(self.formLayout_)
        self.horizontalLayout.addLayout(self.verticalLayout_left)
        self.verticalLayout_right = QtWidgets.QVBoxLayout()
        self.verticalLayout_right.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_right.setSpacing(5)
        self.verticalLayout_right.setObjectName("verticalLayout_right")
        self.label_student_list = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_student_list.setFont(font)
        self.label_student_list.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_student_list.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_student_list.setAlignment(QtCore.Qt.AlignCenter)
        self.label_student_list.setObjectName("label_student_list")
        self.verticalLayout_right.addWidget(self.label_student_list)
        self.listWidget_studentlist = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget_studentlist.setObjectName("listWidget_studentlist")
        self.verticalLayout_right.addWidget(self.listWidget_studentlist)
        self.pushButton_delete = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.verticalLayout_right.addWidget(self.pushButton_delete)
        self.horizontalLayout.addLayout(self.verticalLayout_right)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Student Management Project</span></p></body></html>"))
        self.label_name.setText(_translate("MainWindow", "Name:"))
        self.label_mobile.setText(_translate("MainWindow", "Mobile:"))
        self.label_email.setText(_translate("MainWindow", "Email:"))
        self.label_gender.setText(_translate("MainWindow", "Gender:"))
        self.label_bdate.setText(_translate("MainWindow", "Date of Birth:"))
        self.dateEdit_bdate.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.pushButton_update.setText(_translate("MainWindow", "Update"))
        self.pushButton_submit.setText(_translate("MainWindow", "Submit and Add Record"))
        self.comboBox_gender.setItemText(0, _translate("MainWindow", "Select Gender"))
        self.comboBox_gender.setItemText(1, _translate("MainWindow", "Male"))
        self.comboBox_gender.setItemText(2, _translate("MainWindow", "Female"))
        self.comboBox_gender.setItemText(3, _translate("MainWindow", "Others"))
        self.label_student_list.setText(_translate("MainWindow", "Students List"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
