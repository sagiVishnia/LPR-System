import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from GUI import build_Model_screen, result_controller
from System.Image_Utilities import align_image
from symptom_detection import get_detections

rfs = None  # the 'rfs' is the RFS table. it save the detection results.


# this is the controller for build_Model_screen.
# initialize new window and the parameters for the screen.
class BeforeResControl(QMainWindow, build_Model_screen.Ui_befor_results):
    def __init__(self, parent=None, RFS_table=None):
        super(BeforeResControl, self).__init__(parent)
        self.setupUi(self)
        global rfs
        rfs = RFS_table
        self.start_detection = ThreadClass()
        self.start_detection.start()
        self.start_detection.finished.connect(self.ShowButton)
        self.pushButton.clicked.connect(exit)  # abort btn
        self.pushButton_2.hide()
        self.pushButton_2.clicked.connect(self.view_res)  # view result btn

    # when the detection is done, this function will display the 'show results' button.
    def ShowButton(self):
        self.pushButton_2.show()

    # when the 'show results' button will be pressed by the user, this function will open the result window.
    def view_res(self):
        nextPage = result_controller.ResultControl(self, rfs)
        nextPage.show()
        self.close()


# this class is a thread that runs the detection in the background when this screen is open.
class ThreadClass(QtCore.QThread):

    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)

    def run(self):
        rfs.find_triangle(rfs.mask)  # load the mask to the RFS table.
        rfs.aligned_image, rfs.tri_vertices = align_image(rfs.image, rfs.tri_vertices)  # align the image
        rfs.find_all_symptoms(rfs.aligned_image,
                              rfs.tri_vertices)  # find and cut all symptoms. save the output inside data/images folder.
        get_detections(rfs.symptoms)  # start the detection.
        rfs.make_diagnosis()  # sum the detection  results.

    # this function close the window.
    def closeEvent(self, event):
        sys.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    passing_window = BeforeResControl()
    passing_window.show()
    sys.exit(app.exec_())
