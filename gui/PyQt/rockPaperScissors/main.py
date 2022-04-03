import random

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

        self.player_score = 0
        self.computer_score = 0
        self.CHOICES = ["rock", "paper", "scissors"]

        self.functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(
            _translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Your choice:"
                                     "</span></p>"
                                     "<p><span style=\" font-size:18pt;\">Computer choice: </span></p></body></html>"))
        self.label_2.setText(
            _translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Your score:"
                                     "</span></p>"
                                     "<p><span style=\" font-size:18pt;\">Computer score: "
                                     "</span></p></body></html>"))
        self.rockB.setText(_translate("MainWindow", "Rock"))
        self.paperB.setText(_translate("MainWindow", "Paper"))
        self.scissorsB.setText(_translate("MainWindow", "Scissors"))

    def functions(self):
        self.rockB.clicked.connect(lambda: self.choose_rock())
        self.paperB.clicked.connect(lambda: self.choose_paper())
        self.scissorsB.clicked.connect(lambda: self.choose_scissors())

    def computer_choice(self):
        return random.choice(self.CHOICES)

    def choose_rock(self):
        choice = self.computer_choice()
        if choice == "rock":
            pass
        elif choice == "paper":
            self.computer_score += 1
        else:
            self.player_score += 1
        # update_labels("rock", choice)

    def choose_paper(self):
        choice = self.computer_choice()
        if choice == "rock":
            self.player_score += 1
        elif choice == "paper":
            pass
        else:
            self.computer_score += 1
        # update_labels("paper", choice)

    def choose_scissors(self):
        choice = self.computer_choice()
        if choice == "rock":
            self.computer_score += 1
        elif choice == "paper":
            self.player_score += 1
        else:
            pass
        # update_labels("scissors", choice)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
