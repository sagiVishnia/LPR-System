# this structure save YOLOv3 detection results
class ImageYoloResult:

    def __init__(self):
        self.class_name = None
        self.class_number = None
        self.confidence_score = None
        self.symptom_number = None

    # save the results parameters
    def add_result(self, class_name, class_number, confidence_score, symptom_number):
        self.class_name = class_name
        self.class_number = class_number
        self.confidence_score = confidence_score
        self.symptom_number = symptom_number

    def get_class_name(self):
        return self.class_name

    def get_class_number(self):
        return self.class_number

    def get_confidence_score(self):
        return self.confidence_score

    def get_symptom_number(self):
        return self.symptom_number
