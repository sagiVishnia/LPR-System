import sys
from RFS_Detector import RFSDetector
from System.Image_Utilities import read_and_convert, image_name_from_path
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QFileDialog
from GUI import MakeDiagnosisWindow, BuildModelController, WelcomeController


# this is the controller for MakeDiagnosisWindow.
# initialize new window and the parameters for the screen.
class MakeDiagnosis(QMainWindow, MakeDiagnosisWindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MakeDiagnosis, self).__init__(parent)
        self.setupUi(self)
        self.back_btn.clicked.connect(self.back)
        self.Help_btn.clicked.connect(self.help_info)
        self.exit_btn.clicked.connect(exit)
        self.uploadLarynx_btn.clicked.connect(self.upload_img)
        self.uploadMask_btn.clicked.connect(self.upload_Mask)
        self.Continue_btn.clicked.connect(self.make_diagnosis)
        self.ImagePath = ""  # save the path to the image.
        self.MaskPath = ""  # save the path to the mask.

    # this function is for the back button. its open the welcome screen.
    def back(self):
        previousPage = WelcomeController.Welcome(self)
        previousPage.show()
        self.close()

    # this function loads the image that was selected by the user.
    def upload_img(self):
        # Save the location of a selected image
        self.ImagePath, _filter = QFileDialog.getOpenFileName(self, 'Open file', 'C:/',
                                                              "Image files (*.jpg *png *.jpeg)")
        # Check if no image was selected
        if self.ImagePath == "":
            self.display_error_message("No image was selected, Please select an image!")
        # Set path location of the selected image and enable further page buttons
        else:
            self.imageName_label.setText(self.ImagePath)

    # this function loads the mask that was selected by the user.
    def upload_Mask(self):
        # Save the location of a selected image
        self.MaskPath, _filter = QFileDialog.getOpenFileName(self, 'Open file', 'C:/',
                                                             "Image files (*.jpg *png *.jpeg)")
        # Check if no image was selected
        if self.MaskPath == "":
            self.display_error_message("No mask image was selected, Please select an image!")
        # Set path location of the selected image and enable further page buttons
        else:
            self.maskName_label.setText(self.MaskPath)

    # this function define whats happen when the 'make diagnosis' button is pressed.
    # it will initialize new RFS table, lode the images, and start the detection process.
    def make_diagnosis(self):
        # here we check that image and mask was selected. if not, we will display error massage.
        if self.ImagePath == "":
            self.display_error_message("No image was selected, to continue you MUST select an image!")
        elif self.MaskPath == "":
            self.display_error_message("No mask image was selected, to continue you MUST select mask!")
        else:  # image and mask was selected, start the detection process.
            image_name = image_name_from_path(self.ImagePath)
            image = read_and_convert(self.ImagePath)
            mask = read_and_convert(self.MaskPath)
            rfs = RFSDetector(image_name, image, mask)
            nextPage = BuildModelController.BeforeResControl(self, rfs)
            nextPage.show()
            self.close()

    # this function will display the error massage.
    def display_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    # set help information for the user.
    def help_info(self):
        QMessageBox.about(self, "Information", "In this window you need to select image of the larynx area from the "
                                               "laryngoscopy examination and mask image that match to the larynx image."
                          " To select the images, click on the 'Upload Larynx Image' AND 'Upload Larynx Mask' buttons."
                          " To start the diagnosis, press on the 'Make Diagnosis' button.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    makeDiagnosisWindow = MakeDiagnosis()
    makeDiagnosisWindow.show()
    sys.exit(app.exec_())
