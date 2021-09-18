import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from GUI import result_controller, images_results_single
from PyQt5 import QtGui


# this is the controller for images_results_single.
# initialize new window and the parameters for the screen.
class ImagesResControl(QMainWindow, images_results_single.Ui_images_result_single):
    def __init__(self, parent=None, RFS_table=None):
        super(ImagesResControl, self).__init__(parent)
        self.setupUi(self)
        self.rfs = RFS_table  # RFS table save the detections results.
        self.set_symptom1_left()
        self.exit_btn.clicked.connect(exit)
        self.back_btn.clicked.connect(self.back)
        self.help_btn.clicked.connect(self.help_info)
        # the following buttons are the symptom images buttons.
        # the user will select the images of the symptoms by pressing them.
        self.s1L_btn.clicked.connect(self.set_symptom1_left)
        self.s1R_btn_2.clicked.connect(self.set_symptom1_right)
        self.s2L_btn.clicked.connect(self.set_symptom2_left)
        self.s2R_btn.clicked.connect(self.set_symptom2_right)
        self.s3L_btn.clicked.connect(self.set_symptom3_left)
        self.s3R_btn.clicked.connect(self.set_symptom3_right)
        self.s4L_btn.clicked.connect(self.set_symptom4_left)
        self.s4R_btn.clicked.connect(self.set_symptom4_right)
        self.s5_btn.clicked.connect(self.set_symptom5)
        self.s6_btn.clicked.connect(self.set_symptom6)
        self.s7_btn.clicked.connect(self.set_symptom7)
        self.s8_btn.clicked.connect(self.set_symptom8)

    # in the following section, we open on the screen the relevant image and set the symptom name in the title,
    # according to the user selection with the buttons on the screen.
    def set_symptom1_left(self):
        self.symptom_name_title.setText("Symptom name: Subglottic edema left side")
        self.image.setPixmap(QtGui.QPixmap("../data/images/1.Subglottic edema left_1.png"))
        self.result_lbl.setText(self.rfs.symptoms[0].detection_res[0].get_class_name())
        self.confident.setText(str(self.rfs.symptoms[0].detection_res[0].get_confidence_score()) + "%")

    def set_symptom1_right(self):
        self.symptom_name_title.setText("Symptom name: Subglottic edema right side")
        self.image.setPixmap(QtGui.QPixmap("../data/images/1.Subglottic edema right_1.png"))
        self.result_lbl.setText(self.rfs.symptoms[0].detection_res[1].get_class_name())
        self.confident.setText(str(self.rfs.symptoms[0].detection_res[1].get_confidence_score()) + "%")

    def set_symptom2_left(self):
        self.symptom_name_title.setText("Symptom name: Ventricular obliteration left side")
        self.image.setPixmap(QtGui.QPixmap("../data/images/2.Ventricular obliteration left_2.png"))
        self.result_lbl.setText(self.rfs.symptoms[1].detection_res[0].get_class_name())
        self.confident.setText(str(self.rfs.symptoms[1].detection_res[0].get_confidence_score()) + "%")

    def set_symptom2_right(self):
        self.symptom_name_title.setText("Symptom name: Ventricular obliteration right side")
        self.image.setPixmap(QtGui.QPixmap("../data/images/2.Ventricular obliteration right_2.png"))
        self.result_lbl.setText(self.rfs.symptoms[1].detection_res[1].get_class_name())
        self.confident.setText(str(self.rfs.symptoms[1].detection_res[1].get_confidence_score()) + "%")

    def set_symptom3_left(self):
        self.symptom_name_title.setText("Symptom name: Erythema left side")
        self.image.setPixmap(QtGui.QPixmap("../data/images/3.Erythema 1 left_3.png"))
        self.result_lbl.setText(self.rfs.symptoms[2].detection_res[0].get_class_name())
        self.confident.setText(str(self.rfs.symptoms[2].detection_res[0].get_confidence_score()) + "%")

    def set_symptom3_right(self):
        self.symptom_name_title.setText("Symptom name: Erythema right side")
        self.image.setPixmap(QtGui.QPixmap("../data/images/3.Erythema 2 right_3.png"))
        self.result_lbl.setText(self.rfs.symptoms[2].detection_res[1].get_class_name())
        self.confident.setText(str(self.rfs.symptoms[2].detection_res[1].get_confidence_score()) + "%")

    def set_symptom4_left(self):
        self.symptom_name_title.setText("Symptom name: Vocal fold edema left side")
        self.image.setPixmap(QtGui.QPixmap("../data/images/4.Vocal fold edema left_4.png"))
        self.result_lbl.setText(self.rfs.symptoms[3].detection_res[0].get_class_name())
        self.confident.setText(str(self.rfs.symptoms[3].detection_res[0].get_confidence_score()) + "%")

    def set_symptom4_right(self):
        self.symptom_name_title.setText("Symptom name: Vocal fold edema right side")
        self.image.setPixmap(QtGui.QPixmap("../data/images/4.Vocal fold edema right_4.png"))
        self.result_lbl.setText(self.rfs.symptoms[3].detection_res[1].get_class_name())
        self.confident.setText(str(self.rfs.symptoms[3].detection_res[1].get_confidence_score()) + "%")

    def set_symptom5(self):
        self.symptom_name_title.setText("Symptom name: Diffuse laryngeal edema")
        self.image.setPixmap(QtGui.QPixmap("../data/images/5.Diffuse laryngeal edema_5.png"))
        self.result_lbl.setText(self.rfs.symptoms[4].detection_res[0].get_class_name())
        self.confident.setText(str(self.rfs.symptoms[4].detection_res[0].get_confidence_score()) + "%")

    def set_symptom6(self):
        self.symptom_name_title.setText("Symptom name: Posterior commissure hypertrophy")
        self.image.setPixmap(QtGui.QPixmap("../data/images/6.Posterior commissure hypertrophy_6.png"))
        self.result_lbl.setText(self.rfs.symptoms[5].detection_res[0].get_class_name())
        self.confident.setText(str(self.rfs.symptoms[5].detection_res[0].get_confidence_score()) + "%")

    def set_symptom7(self):
        self.symptom_name_title.setText("Symptom name: Granuloma")
        self.image.setPixmap(QtGui.QPixmap("../data/images/7.Granuloma_7.png"))
        self.result_lbl.setText(self.rfs.symptoms[6].detection_res[0].get_class_name())
        self.confident.setText(str(self.rfs.symptoms[6].detection_res[0].get_confidence_score()) + "%")

    def set_symptom8(self):
        self.symptom_name_title.setText("Symptom name: Thick endolaryngeal mucus")
        self.image.setPixmap(QtGui.QPixmap("../data/images/8.Thick endolaryngeal mucus_8.png"))
        self.result_lbl.setText(self.rfs.symptoms[7].detection_res[0].get_class_name())
        self.confident.setText(str(self.rfs.symptoms[7].detection_res[0].get_confidence_score()) + "%")

    # this function opens the previous screen.
    def back(self):
        previousPage = result_controller.ResultControl(self, self.rfs)
        previousPage.show()
        self.close()

    # this function open the information/help screen
    def help_info(self):
        QMessageBox.about(self, "Information", "In this window you can see the areas of each symptom that the system "
                                               "was selected. To navigate between the different symptoms,"
                                               " press the buttons bellow according to the symptom number that you"
                                               " want to view. under each symptom area, "
                                               "you can see the detection result and the confidence number of the "
                                               "system. To go back to the RFS table, press on the 'back' button.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    img_window = ImagesResControl()
    img_window.show()
    sys.exit(app.exec_())
