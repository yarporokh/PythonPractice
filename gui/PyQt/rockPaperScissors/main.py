from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 301, 241))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rockB = QtWidgets.QPushButton(self.widget)
        self.rockB.setObjectName("rockB")
        self.horizontalLayout.addWidget(self.rockB)
        self.paperB = QtWidgets.QPushButton(self.widget)
        self.paperB.setObjectName("paperB")
        self.horizontalLayout.addWidget(self.paperB)
        self.scissorsB = QtWidgets.QPushButton(self.widget)
        self.scissorsB.setObjectName("scissorsB")
        self.horizontalLayout.addWidget(self.scissorsB)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.functions()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Your choice:"
                                                    "</span></p>"
                                                    "<p><span style=\" font-size:18pt;\">Computer choice: </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Your score:"
                                                      "</span></p>"
                                                      "<p><span style=\" font-size:18pt;\">Computer score: "
                                                      "</span></p></body></html>"))
        self.rockB.setText(_translate("MainWindow", "Rock"))
        self.paperB.setText(_translate("MainWindow", "Paper"))
        self.scissorsB.setText(_translate("MainWindow", "Scissors"))

    def functions(self):
        self.rockB.clicked.connect()
        self.paperB.clicked.connect()
        self.scissorsB.clicked.connect()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
