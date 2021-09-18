import cv2
from RFS_Detector import RFSDetector, init_symptoms
import numpy as np
from PIL import Image
from System.Image_Utilities import draw_coordinates_on_image, align_image
from symptom_detection import get_detections


# The following section allows you to run the system through the console.
# By running the code through the console, you will have a number of other options such as:
# manually selecting the coordinates, viewing the image alignment process and more.
# Please follow the system instructions in the console.

######## IMPORTANT!!!!!!  #######
# If the code is run through the console and not through the GUI, you must update the following paths:
# inside 'symptom_detection.py' code:
# 1. enable the "parameters for console running" at the top of the file,
# 2. and disable the "parameters for GUI running"
# inside 'RFS_Detector.py' code:
# 3. change the path to yolo output folder from this: "../data/images", to this: "data/images"
# 4. locate the image and the mask inside the main system folder (LPR_System) and update the names for the images in the
# top of the main function.
# 5. run the code.
def main():
    # load image and mask from path
    image_path = '173 (1).png'  # save the image inside the project main folder an update her name her.
    mask_path = '173 (2).png'  # save the mask inside the project main folder an update her name her.
    image_name = image_path[0:3]
    image = cv2.imread(image_path)  # read larynx image.
    mask = cv2.imread(mask_path)  # read larynx mask.
    # initialize new RFS table detector
    rfs = RFSDetector(image_name, image, mask)
    # auto find coordinates in the mask
    rfs.find_triangle(rfs.mask)
    # check if its the correct coordinates. if not, select the coordinates manually
    temp_img = draw_coordinates_on_image(rfs.mask, rfs.tri_vertices)
    cv2.imshow('coordinates found on the mask', temp_img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    temp_img = draw_coordinates_on_image(rfs.image, rfs.tri_vertices)
    cv2.imshow('coordinates found in the mask draw on the original image', temp_img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    print('Do you want to select other coordinates? y or n ?')
    to_select_coordinates = input(' ')
    while to_select_coordinates == 'y':
        print("select the coordinates in this order: left, right and bottom by clicking on the image.")
        print("when done, press enter")
        rfs.set_triangle_coordinates()
        temp_img = draw_coordinates_on_image(rfs.image, rfs.tri_vertices)
        print("To approve the coordinates, type 'n' and press enter")
        print("To select again, type 'y' and press enter")
        cv2.imshow('New coordinates on the image', temp_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        to_select_coordinates = input(' ')
    # align the image according to the larynx coordinate
    rfs.aligned_image, rfs.tri_vertices = align_image(rfs.image, rfs.tri_vertices)
    original_img = draw_coordinates_on_image(rfs.aligned_image, rfs.tri_vertices)
    cv2.imshow("after", original_img)
    cv2.waitKey(0)
    # crop all symptoms areas and save them in the input folder of yolo
    rfs.find_all_symptoms(rfs.aligned_image, rfs.tri_vertices)
    # detect the symptoms with yolo
    get_detections(rfs.symptoms)
    rfs.make_diagnosis()
    rfs.print_table()

    # # section number 2: Testing mod
    # # initialize new RFS table detector
    # rfs = RFSDetector("image_name", None, None)
    # rfs.symptoms = init_symptoms()
    # # Put the images for testing inside 'data/images' folder
    # get_detections(rfs.symptoms)
    # rfs.make_diagnosis()
    # rfs.print_table()


if __name__ == "__main__":
    main()
