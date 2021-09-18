import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI import WelcomeScreen, MakeDiagnosisController


# this is the controller for 'WelcomeScreen'.
# initialize new window and the parameters for the screen.
class Welcome(QMainWindow, WelcomeScreen.Ui_WelcomeWindow):

    def __init__(self, parent=None):
        super(Welcome, self).__init__(parent)
        self.setupUi(self)
        self.exit_btn.clicked.connect(exit)  # define the exit button
        self.start_btn.clicked.connect(self.enter_to_system)  # define the continue button

    # this function will open the 'make diagnosis' window and let the user to enter to the system.
    def enter_to_system(self):
        Make_diagnosis_page = MakeDiagnosisController.MakeDiagnosis(self)
        Make_diagnosis_page.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    WelcomeWindow = Welcome()
    WelcomeWindow.show()
    sys.exit(app.exec_())
