import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from GUI import result, images_results_controller, MakeDiagnosisController


# this is the controller for 'result' screen.
# initialize new window and the parameters for the screen.
class ResultControl(QMainWindow, result.Ui_ResultWindow):
    def __init__(self, parent=None, RFS_table=None):
        super(ResultControl, self).__init__(parent)
        self.setupUi(self)
        if RFS_table is not None:
            self.set_screen(RFS_table)  # show results on screen
        self.exit_btn.clicked.connect(exit)
        self.back_btn.clicked.connect(self.back)
        self.help_btn.clicked.connect(self.help_info)
        self.veiw_image_btn.clicked.connect(self.show_images)
        self.rfs_tbl = RFS_table

    # this function get the RFS table with the detection results and display them on the screen.
    def set_screen(self, rfs):
        symptoms = rfs.symptoms
        self.score_1.setText(str(symptoms[0].final_rfs_score))
        self.score_2.setText(str(symptoms[1].final_rfs_score))
        self.score_3.setText(str(symptoms[2].final_rfs_score))
        self.score_4.setText(str(symptoms[3].final_rfs_score))
        self.score_5.setText(str(symptoms[4].final_rfs_score))
        self.score_6.setText(str(symptoms[5].final_rfs_score))
        self.score_7.setText(str(symptoms[6].final_rfs_score))
        self.score_8.setText(str(symptoms[7].final_rfs_score))
        self.Total_score.setText(str(rfs.table_score))
        if rfs.table_score >= 7:
            self.finale_res.setText("Have LPR")

    # this function is for the back button. it will return the user to the 'make diagnosis' screen.
    def back(self):
        previousPage = MakeDiagnosisController.MakeDiagnosis(self)
        previousPage.show()
        self.close()

    # set help information for the user.
    def help_info(self):
        QMessageBox.about(self, "Information", "In this window we display the detection results. you can see the score "
                                               "of each symptom and the finale diagnosis based on the total score. "
                                               " To view the images of the symptoms, please press on the "
                                               "'View symptoms images' button. To make new diagnosis, press"
                                               " on the 'back' button.")

    # this function will opens the images from the detection and there results.
    def show_images(self):
        nextPage = images_results_controller.ImagesResControl(self, self.rfs_tbl)
        nextPage.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    res_window = ResultControl()
    res_window.show()
    sys.exit(app.exec_())
