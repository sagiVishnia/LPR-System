from System.yolo_result import ImageYoloResult


# this structure save all information for symptom.
class Symptom:
    def __init__(self, symptom_name, rfs_value):
        self.symptom_name = symptom_name  # the name of the symptom
        self.rfs_value = rfs_value  # 'rfs_value' is the value of sick area from the RFS table
        self.symptom_images = []  # 'symptom_images' is array of images for specific symptom for detection
        self.detection_res = []  # 'detection_res' is array with list of 'ImageYoloResult'
        self.final_result = None  # save the finale result for symptom
        self.final_rfs_score = None  # save the finale score for symptom

    def add_symptom_image(self, image):
        self.symptom_images.append(image)

    # add YOLOv3 detection result
    def add_result(self, class_result, class_number, confidence_score, symptom_tbl_number):
        new_result = ImageYoloResult()
        new_result.add_result(class_result, class_number, confidence_score, symptom_tbl_number)
        self.detection_res.append(new_result)

    def calculate_final_result(self):
        for res in self.detection_res:
            class_name = res.get_class_name()
            if class_name == 'sick area':
                self.final_result = 'sick area'
                self.final_rfs_score = 2
                return
        self.final_result = 'healthy area'
        self.final_rfs_score = 0
