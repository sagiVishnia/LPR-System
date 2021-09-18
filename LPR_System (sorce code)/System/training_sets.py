# import the necessary packages
import cv2
from System import Image_Utilities as utils
import RFS_Detector as rfs
from System import Symptoms_Regions as regions
import os


# The next section lets you create training sets for your system All you need to do is to select the symptom number
# and type in the 'main' function at the bottom. Please know that you need to save your images for the training set
# inside "LPR_System/System" folder and they need to be in '.png' format, the output will be saved in new folder
# inside System folder. IF YOU HAVE COORDINATES '.TXT' FILE FOR YOU IMAGES, SAVE THEM ALSO INSIDE 'System' FOLDER. IF
# YOU DON'T HAVE THE COORDINATES, THE SYSTEM WILL GUID YOU TO SELECT THE COORDINATE MANUALLY AND WILL SAVE YOUR
# SELECTION IN NEW '.TXT' FILE.

def loadImage(path="."):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.png')]


def loadImageNames(path="."):
    names = []
    for f in os.listdir(path):
        if f.endswith('.png'):
            name = f.split(".")
            names.append(name[0])
    return names


# for each image set manually the coordinates for max accuracy
def cut_training_set(images, images_names, symptom_number, class_type):
    # create output directory
    dirname = 'training set for symptom number - ' + str(symptom_number)
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    for image, image_name in zip(images, images_names):
        # global actions for all symptoms
        table = rfs.RFSDetector(image_name, image, None)
        coordinate = image_name + ' ' + 'triangle.txt'
        if os.path.exists(coordinate): # check if coordinates file exist.
            f = open(coordinate, "r")
            table.reade_coordinates_from_file(f)
            table.aligned_image, table.tri_vertices = utils.align_image(table.image, table.tri_vertices)
        else:  # else select coordinate
            approved = False
            while not approved:
                table.set_triangle_coordinates()
                # save the selected coordinates manually
                table.write_coordinates_to_file(dirname)
                table.aligned_image, table.tri_vertices = utils.align_image(table.image, table.tri_vertices)
                draw_img = utils.draw_coordinates_on_image(table.aligned_image, table.tri_vertices)
                cv2.imshow("View result: after aligned the image", draw_img)
                cv2.waitKey()
                cv2.destroyAllWindows()
                print("If you want to select the coordinates again press 'y' else press 'n':  ")
                answer = input(' ')
                if answer == 'n':
                    approved = True
        # start cutting the image according the symptom number
        if symptom_number == 1:
            r_bbox, l_bbox = regions.find_symptom_1(table.tri_vertices)
            left_side_img = utils.four_point_transform(table.aligned_image, l_bbox)
            right_side_img = utils.four_point_transform(table.aligned_image, r_bbox)
            # draw selected area result before crop
            symptom_area = utils.draw_coordinates_on_image(table.aligned_image, r_bbox)
            cv2.imwrite(os.path.join(dirname, image_name + '_Symptom 1 right area.png'), symptom_area)
            symptom_area = utils.draw_coordinates_on_image(table.aligned_image, l_bbox)
            cv2.imwrite(os.path.join(dirname, image_name + '_Symptom 1 left area.png'), symptom_area)
            cv2.imwrite(os.path.join(dirname, image_name + ' ' + class_type + '_Symptom 1 left area.png'),
                        left_side_img)
            cv2.imwrite(os.path.join(dirname, image_name + ' ' + class_type + '_Symptom 1 right area.png'),
                        right_side_img)
        if symptom_number == 2:
            r_bbox, l_bbox = regions.find_symptom_2(table.tri_vertices)
            left_side_img = utils.four_point_transform(table.aligned_image, l_bbox)
            right_side_img = utils.four_point_transform(table.aligned_image, r_bbox)
            # draw selected area result before crop
            symptom_area = utils.draw_coordinates_on_image(table.aligned_image, r_bbox)
            cv2.imwrite(os.path.join(dirname, image_name + '_Symptom 2 right area.png'), symptom_area)
            symptom_area = utils.draw_coordinates_on_image(table.aligned_image, l_bbox)
            cv2.imwrite(os.path.join(dirname, image_name + '_Symptom 2 left area.png'), symptom_area)
            cv2.imwrite(os.path.join(dirname, image_name + ' ' + class_type + '_Symptom 2 left area.png'),
                        left_side_img)
            cv2.imwrite(os.path.join(dirname, image_name + ' ' + class_type + '_Symptom 2 right area.png'),
                        right_side_img)
        if symptom_number == 3:
            r_bbox, l_bbox = regions.find_symptom_3(table.tri_vertices)
            left_side_img = utils.four_point_transform(table.aligned_image, l_bbox)
            right_side_img = utils.four_point_transform(table.aligned_image, r_bbox)
            # draw selected area result before crop
            symptom_area = utils.draw_coordinates_on_image(table.aligned_image, r_bbox)
            cv2.imwrite(os.path.join(dirname, image_name + '_Symptom 3 right area.png'), symptom_area)
            symptom_area = utils.draw_coordinates_on_image(table.aligned_image, l_bbox)
            cv2.imwrite(os.path.join(dirname, image_name + '_Symptom 3 left area.png'), symptom_area)
            cv2.imwrite(os.path.join(dirname, image_name + ' ' + class_type + '_Symptom 3 left area.png'),
                        left_side_img)
            cv2.imwrite(os.path.join(dirname, image_name + ' ' + class_type + '_Symptom 3 right area.png'),
                        right_side_img)
        if symptom_number == 4:
            r_bbox, l_bbox = regions.find_symptom_4(table.tri_vertices)
            left_side_img = utils.four_point_transform(table.aligned_image, l_bbox)
            right_side_img = utils.four_point_transform(table.aligned_image, r_bbox)
            # draw selected area result before crop
            symptom_area = utils.draw_coordinates_on_image(table.aligned_image, r_bbox)
            cv2.imwrite(os.path.join(dirname, image_name + '_Symptom 4 right area.png'), symptom_area)
            symptom_area = utils.draw_coordinates_on_image(table.aligned_image, l_bbox)
            cv2.imwrite(os.path.join(dirname, image_name + '_Symptom 4 left area.png'), symptom_area)
            cv2.imwrite(os.path.join(dirname, image_name + ' ' + class_type + '_Symptom 4 left area.png'),
                        left_side_img)
            cv2.imwrite(os.path.join(dirname, image_name + ' ' + class_type + '_Symptom 4 right area.png'),
                        right_side_img)
        if symptom_number == 5:
            bbox = regions.find_symptom_5(table.tri_vertices)
            cropped_img = utils.four_point_transform(table.aligned_image, bbox)
            # draw selected area result before crop
            symptom_area = utils.draw_coordinates_on_image(table.aligned_image, bbox)
            cv2.imwrite(os.path.join(dirname, image_name + '_Symptom 5 area.png'), symptom_area)
            cv2.imwrite(os.path.join(dirname, image_name + ' ' + class_type + '_Symptom 5 area.png'), cropped_img)
        if symptom_number == 6:
            bbox = regions.find_symptom_6(table.tri_vertices)
            cropped_img = utils.four_point_transform(table.aligned_image, bbox)
            # draw selected area result before crop
            symptom_area = utils.draw_coordinates_on_image(table.aligned_image, bbox)
            cv2.imwrite(os.path.join(dirname, image_name + '_Symptom 6 area.png'), symptom_area)
            cv2.imwrite(os.path.join(dirname, image_name + ' ' + class_type + '_Symptom 6 area.png'), cropped_img)
        if symptom_number == 7:
            bbox = regions.find_symptom_7(table.tri_vertices)
            cropped_img = utils.four_point_transform(table.aligned_image, bbox)
            # draw selected area result before crop
            # symptom_area = utils.draw_coordinates_on_image(table.aligned_image, bbox)
            # cv2.imwrite(os.path.join(dirname, image_name + '_Symptom 7 area.png'), symptom_area)
            cv2.imwrite(os.path.join(dirname, image_name + ' ' + class_type + '_Symptom 7 area_7.png'), cropped_img)
        if symptom_number == 8:
            bbox = regions.find_symptom_8(table.tri_vertices)
            cropped_img = utils.four_point_transform(table.aligned_image, bbox)
            # draw selected area result before crop
            symptom_area = utils.draw_coordinates_on_image(table.aligned_image, bbox)
            cv2.imwrite(os.path.join(dirname, image_name + '_Symptom 8 area.png'), symptom_area)
            cv2.imwrite(os.path.join(dirname, image_name + ' ' + class_type + '_Symptom 8 area.png'), cropped_img)


def create_training_set(symptom_number, class_type):
    filenames = loadImage()
    images = []
    names = loadImageNames()
    for file in filenames:
        images.append(cv2.imread(file, cv2.IMREAD_UNCHANGED))
    cut_training_set(images, names, symptom_number, class_type)


def main():
    # select the symptom number that you want to create training set for and the region type, then run the code.
    # type must be 'sick' or 'healthy'. symptom number must be in range of 1 to 8.
    symptom_number = 7
    region_type = "sick"
    create_training_set(symptom_number, region_type)


if __name__ == "__main__":
    main()
