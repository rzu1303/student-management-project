from gui import Ui_MainWindow
import db
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys, os

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from pprint import pprint
import datetime 

class Main(Ui_MainWindow):
    students = {}
    def __init__(self, MainWindow):
        """MainWindow constructor"""
        super().setupUi(MainWindow) 

        self.populate_list()
        # submit and record new student
        self.pushButton_submit.clicked.connect(self.save_student)
        # populating student form when student is selected
        self.listWidget_studentlist.itemSelectionChanged.connect(self.populate_form)
        # delete student
        self.pushButton_delete.clicked.connect(self.delete_student)
        # update student
        self.pushButton_update.clicked.connect(self.update_student)



    def save_student(self):
        student = {
            'name': self.lineEdit_name.text(),
            'mobile': self.lineEdit_mobile.text(),
            'email': self.lineEdit_email.text(),
            'gender': self.comboBox_gender.currentText(),
            'dob': self.dateEdit_bdate.date()
        }

        if db.student_create(name=student['name'],
                          mobile=student['mobile'],
                          email=student['email'],
                          gender=student['gender'],
                          dob = student['dob'].toString('dd.MM.yyyy')):
            self.students = self.student_read()

        self.populate_list()

    def populate_list(self):
        self.listWidget_studentlist.setCurrentRow(-1)
        self.listWidget_studentlist.clear()
        self.clear_form()
        self.students = db.student_read()
        # loop for student_list
        for student in self.students:
            id = int(student[0])    
            self.listWidget_studentlist.addItem(f"{id}: {student[1], student[3]}")
 

    def populate_form(self):
        self.clear_form()
        student_number = self.listWidget_studentlist.currentRow()
        if student_number == -1:
            return
        
        students = db.student_read()
        student_data = students[student_number]
        
        self.lineEdit_name.setText(student_data[1])
        self.lineEdit_mobile.setText(student_data[2])
        self.lineEdit_email.setText(student_data[3])
        self.comboBox_gender.setCurrentText(student_data[4])
        self.dateEdit_bdate.setDate(student_data[5])

    def clear_form(self):
        self.lineEdit_name.clear()
        self.lineEdit_mobile.clear()
        self.lineEdit_email.clear()
        self.comboBox_gender.setCurrentIndex(0)
        self.dateEdit_bdate.setDate(QtCore.QDate(2000, 1, 1))

    def initiate(self):
        self.students = self.student_read()
        self.populate_list()


    def student_read(self):
        results = db.student_read()
        all_students = {} 

        for row in results:
            id = row[0]
            if id not in all_students:
                all_students[id] = []
            all_students[id].append(
                {
                  'name':row[1],
                  'mobile':row[2],
                  'email' :row[3],
                  'gender':row[4],
                  'dob': QtCore.QTime.fromString(str(row[5]), 'dd.MM.yyyy')
                }
            )

        return all_students


    def delete_student(self):
        row = self.listWidget_studentlist.currentRow() - 1
        del(self.students[row])

        if db.student_delete(self.students[row][0]):
            self.student = self.student_read()
        self.listWidget_studentlist.setCurrentRow(-1)
        self.clear_form()
        self.populate_list()

    def update_student(self):
        row = self.listWidget_studentlist.currentRow()
        n_student = {
            'name': self.lineEdit_name.text(),
            'mobile': self.lineEdit_mobile.text(),
            'email': self.lineEdit_email.text(),
            'gender': self.comboBox_gender.currentText(),
            'dob': self.dateEdit_bdate.date()
        }
        if db.student_update(row_id = self.students[row][0],
                          name=n_student['name'],
                          mobile=n_student['mobile'],
                          email=n_student['email'],
                          gender=n_student['gender'],
                          dob = n_student['dob'].toString('dd.MM.yyyy')):
            self.students = self.student_read()
        
        self.populate_list()



if __name__ == "__main__":
    db.db_init()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()

    ui = Main(MainWindow)

    MainWindow.show()

    sys.exit(app.exec())    