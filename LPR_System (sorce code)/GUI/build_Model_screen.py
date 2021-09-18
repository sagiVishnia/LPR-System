
# this is the set up code to build_Model_screen
# here the buttons and visual features of the screen will be set.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_befor_results(object):
    def setupUi(self, befor_results):
        befor_results.setObjectName("befor_results")
        befor_results.resize(577, 616)
        befor_results.setStyleSheet("background-color:rgb(237, 249, 255)")
        self.centralwidget = QtWidgets.QWidget(befor_results)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 20, 471, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setLineWidth(1)
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(60, 330, 471, 91))
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 160, 341, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./GUI_Images/proccesing_img.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 520, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("Background-color:rgb(255, 46, 46)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 450, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("Background-color:rgb(85, 255, 127)")
        self.pushButton_2.setObjectName("pushButton_2")
        befor_results.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(befor_results)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 577, 21))
        self.menubar.setObjectName("menubar")
        befor_results.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(befor_results)
        self.statusbar.setObjectName("statusbar")
        befor_results.setStatusBar(self.statusbar)

        self.retranslateUi(befor_results)
        QtCore.QMetaObject.connectSlotsByName(befor_results)

    def retranslateUi(self, befor_results):
        _translate = QtCore.QCoreApplication.translate
        befor_results.setWindowTitle(_translate("befor_results", "build_model"))
        self.textBrowser.setHtml(_translate("befor_results",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:8.25pt; font-weight:600; font-style:italic;\">\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:24pt; font-style:normal; vertical-align:super;\">The detection process has begun,</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:24pt; font-style:normal; vertical-align:super;\">it can take a few seconds.</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("befor_results",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"tw-target-text\"></a><span style=\" font-family:\'Courier New\'; font-size:14pt;\">W</span><span style=\" font-family:\'Courier New\'; font-size:14pt;\">hen the process will be complete, </span></p>\n"
                                              "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:14pt;\">the &quot;View Result&quot; button will appear</span></p></body></html>"))
        self.pushButton.setText(_translate("befor_results", "Abort"))
        self.pushButton_2.setText(_translate("befor_results", "View Result"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    befor_results = QtWidgets.QMainWindow()
    ui = Ui_befor_results()
    ui.setupUi(befor_results)
    befor_results.show()
    sys.exit(app.exec_())
