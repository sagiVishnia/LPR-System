import numpy as np
import cv2
import os
from System import Image_Utilities as util
from System import Symptom_Structure
from System import Symptoms_Regions

path = "../data/images"  # path to yolo input folder


def init_symptoms():  # this function  initializing new array for symptoms. each with his name and his RFS value.
    symptoms_arr = [Symptom_Structure.Symptom('Subglottic edema', 2),
                    Symptom_Structure.Symptom('Ventricular obliteration', 2),
                    Symptom_Structure.Symptom('Erythema', 2),
                    Symptom_Structure.Symptom('Vocal fold edema', 2),
                    Symptom_Structure.Symptom('Diffuse laryngeal edema', 2),
                    Symptom_Structure.Symptom('Posterior commissure hypertrophy', 2),
                    Symptom_Structure.Symptom('Granuloma', 2),
                    Symptom_Structure.Symptom('Thick endolaryngeal mucus', 2)]
    return symptoms_arr


# the RFSDetector class saves all relevant diagnostic information.
# finds the coordinates, saves the diagnostic results and finds the symptom areas.
class RFSDetector:

    def __init__(self, patient_num, image, mask):
        self.patient_num = patient_num
        self.image = image
        self.mask = mask
        self.aligned_image = None
        self.symptoms = init_symptoms()
        # The order of the coordinates in 'tri_vertices' is: upper left, upper right, bottom.
        self.tri_vertices = None  # array of larynx coordinates.
        self.table_score = 0  # finale RFS score after diagnosis.

    def find_triangle(self, mask):  # this function finds the Larynx coordinates from mask image.
        # Read the mask of image.
        gray_mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        # Attempt to improve accuracy by smoothing the image.
        blur_mask = cv2.GaussianBlur(gray_mask, (5, 5), 0)
        smooth_mask = cv2.addWeighted(blur_mask, 1.5, gray_mask, -0.5, 0)
        # detect corners with the openCV function called goodFeaturesToTrack.
        triangle_corners = cv2.goodFeaturesToTrack(smooth_mask, 40, 0.01, 10, useHarrisDetector=5)
        triangle_corners = np.int0(triangle_corners)
        # Initializing the vertices values.
        up_left_x = 1000
        up_left_y = 1000
        up_right_x = 0
        up_right_y = 1000
        bottom_coord_x = 0
        bottom_coord_y = 0
        # We iterate through each corner in order to find the triangle vertices.
        for i in triangle_corners:
            x, y = i.ravel()
            if x < up_left_x:
                up_left_x = x
                up_left_y = y
            elif x > up_right_x:
                up_right_x = x
                up_right_y = y
            elif y > bottom_coord_y:
                bottom_coord_y = y
                bottom_coord_x = x
        # Check that the top vertices are indeed at the top of the triangle(And not just deviation in the mask).
        for i in triangle_corners:
            x, y = i.ravel()
            if y - up_left_y < -35 and abs(x - up_left_x) < 40:
                up_left_x = x
                up_left_y = y
            elif y - up_right_y < -35 and abs(x - up_right_x) < 40:
                up_right_x = x
                up_right_y = y
        # for i in triangle_corners:
        #     x, y = i.ravel()
        #     if y > bottom_coord_y:
        #         bottom_coord_x = x
        #         bottom_coord_y = y
        coordinates_arr = np.array([[up_left_x, up_left_y], [up_right_x, up_right_y], [bottom_coord_x, bottom_coord_y]])
        self.tri_vertices = coordinates_arr
        return coordinates_arr

    def find_all_symptoms(self, image, coordinates):  # this function gets larynx image and array of three coordinates.
        # cut the symptom from the image, and save the cut images in YOLOv3 input folder (inside: data/images)
        img = image
        coor = coordinates
        symptoms_arr = self.symptoms
        for symptom in symptoms_arr:
            if symptom.symptom_name == 'Subglottic edema':  # 1
                r_bbox, l_bbox = Symptoms_Regions.find_symptom_1(coor)
                left_side = util.four_point_transform(img, l_bbox)
                right_side = util.four_point_transform(img, r_bbox)
                ### use this section to draw the selected area on the original image ###
                # symptom_area = util.draw_coordinates_on_image(img, r_bbox)
                # cv2.imwrite('Subglottic edema right area.png', symptom_area)
                # symptom_area = util.draw_coordinates_on_image(img, l_bbox)
                # cv2.imwrite('Subglottic edema left area.png', symptom_area)
                ######
                # write the cropped images to the yolo input folder in 'path'
                cv2.imwrite(os.path.join(path, "1.Subglottic edema left_1.png"), left_side)
                cv2.imwrite(os.path.join(path, "1.Subglottic edema right_1.png"), right_side)
            if symptom.symptom_name == 'Ventricular obliteration':  # 2
                r_bbox, l_bbox = Symptoms_Regions.find_symptom_2(coor)
                left_side = util.four_point_transform(img, l_bbox)
                right_side = util.four_point_transform(img, r_bbox)
                ## use this section to draw the selected area on the original image ###
                # symptom_area = util.draw_coordinates_on_image(img, r_bbox)
                # cv2.imwrite('Ventricular obliteration right area.png', symptom_area)
                # symptom_area = util.draw_coordinates_on_image(img, l_bbox)
                # cv2.imwrite('Ventricular obliteration left area.png', symptom_area)
                ####
                cv2.imwrite(os.path.join(path, "2.Ventricular obliteration left_2.png"), left_side)
                cv2.imwrite(os.path.join(path, "2.Ventricular obliteration right_2.png"), right_side)
            if symptom.symptom_name == 'Erythema':  # 3
                r_bbox, l_bbox = Symptoms_Regions.find_symptom_3(coor)
                left_side = util.four_point_transform(img, l_bbox)
                right_side = util.four_point_transform(img, r_bbox)
                cv2.imwrite(os.path.join(path, "3.Erythema 1 left_3.png"), left_side)
                cv2.imwrite(os.path.join(path, "3.Erythema 2 right_3.png"), right_side)
            if symptom.symptom_name == 'Vocal fold edema':  # 4
                r_bbox, l_bbox = Symptoms_Regions.find_symptom_4(coor)
                left_side = util.four_point_transform(img, l_bbox)
                right_side = util.four_point_transform(img, r_bbox)
                ## use this section to draw the selected area on the original image ######
                # symptom_area = util.draw_coordinates_on_image(img, r_bbox)
                # cv2.imwrite('Vocal fold edema right area.png', symptom_area)
                # symptom_area = util.draw_coordinates_on_image(img, l_bbox)
                # cv2.imwrite('Vocal fold edema left area.png', symptom_area)
                ######
                cv2.imwrite(os.path.join(path, "4.Vocal fold edema left_4.png"), left_side)
                cv2.imwrite(os.path.join(path, "4.Vocal fold edema right_4.png"), right_side)
            if symptom.symptom_name == 'Diffuse laryngeal edema':  # 5
                bbox = Symptoms_Regions.find_symptom_5(coor)
                cropped = util.four_point_transform(img, bbox)
                ## use this section to draw the selected area on the original image ######
                # symptom_area = util.draw_coordinates_on_image(img, bbox)
                # cv2.imwrite('Diffuse laryngeal edema area.png', symptom_area)
                ######
                cv2.imwrite(os.path.join(path, "5.Diffuse laryngeal edema_5.png"), cropped)
            if symptom.symptom_name == 'Posterior commissure hypertrophy':  # 6
                bbox = Symptoms_Regions.find_symptom_6(coor)
                cropped = util.four_point_transform(img, bbox)
                ## use this section to draw the selected area on the original image ######
                # symptom_area = util.draw_coordinates_on_image(img, bbox)
                # cv2.imwrite('Posterior commissure hypertrophy area.png', symptom_area)
                #####
                cv2.imwrite(os.path.join(path, "6.Posterior commissure hypertrophy_6.png"), cropped)
            if symptom.symptom_name == 'Granuloma':  # 7
                bbox = Symptoms_Regions.find_symptom_7(coor)
                cropped = util.four_point_transform(img, bbox)
                ## use this section to draw the selected area on the original image ######
                # symptom_area = util.draw_coordinates_on_image(img, bbox)
                # cv2.imwrite('Granuloma area.png', symptom_area)
                cv2.imwrite(os.path.join(path, "7.Granuloma_7.png"), cropped)
            if symptom.symptom_name == 'Thick endolaryngeal mucus':  # 8
                bbox = Symptoms_Regions.find_symptom_7(coor)
                cropped = util.four_point_transform(img, bbox)
                ## use this section to draw the selected area on the original image ######
                # symptom_area = util.draw_coordinates_on_image(img, bbox)
                # cv2.imwrite('Thick endolaryngeal mucus area.png', symptom_area)
                cv2.imwrite(os.path.join(path, "8.Thick endolaryngeal mucus_8.png"), cropped)
        self.symptoms = symptoms_arr
        return symptoms_arr

    def set_triangle_coordinates(self):  # this function enable to the user to manually select the larynx coordinates.
        def mouse_drawing(event, x, y, flags, params):
            if event == cv2.EVENT_LBUTTONDOWN:
                new_vertices.append((x, y))

        image = np.copy(self.image)
        cv2.namedWindow("Frame")
        cv2.setMouseCallback("Frame", mouse_drawing)
        new_vertices = []
        while True:
            for center_position in new_vertices:
                cv2.circle(image, center_position, 5, (0, 0, 255), -1)
            cv2.imshow("Frame", image)
            key = cv2.waitKey(1)
            if key == 13 and len(new_vertices) == 3:
                self.tri_vertices = np.array([[new_vertices[0][0], new_vertices[0][1]],
                                              [new_vertices[1][0], new_vertices[1][1]],
                                              [new_vertices[2][0], new_vertices[2][1]]])
                break
            elif key == 13 and len(new_vertices) != 3:
                print('You must select 3 coordinates, select again')
                new_vertices = []
                image = np.copy(self.image)
        cv2.destroyAllWindows()

    def reade_coordinates_from_file(self, file):  # this function read coordinates from .txt file.
        arr = []
        fileLines = file.readlines()
        for line in fileLines:
            coord = line.split(",")
            for value in coord:
                arr.append(float(value))
        self.tri_vertices = np.array([[arr[0], arr[1]],
                                      [arr[2], arr[3]],
                                      [arr[4], arr[5]]])

    def write_coordinates_to_file(self, path=None):  # this function write the selected coordinates to .txt file.
        fileName = self.patient_num + ' ' + 'triangle.txt'
        if path is not None:
            fileName = os.path.join(path, fileName)
        f = open(fileName, "w+")
        for vertex in self.tri_vertices:
            f.write(str(vertex[0]) + "," + str(vertex[1]) + "\n")
        f.close()

    # this function sum the detection score from 'symptoms' array and calculate the finale result.
    def make_diagnosis(self):
        self.table_score = 0
        for symptom in self.symptoms:
            symptom.calculate_final_result()
            self.table_score += symptom.final_rfs_score

    def print_table(self):  # this function print the RFS table to console after detection.
        for symptom in self.symptoms:
            print("symptom name: " + symptom.symptom_name + "\tScore: " + str(symptom.final_rfs_score))
        print("\nFinal Score is: " + str(self.table_score))
        if self.table_score >= 7:
            print("Have LPR")
        else:
            print("healthy")
