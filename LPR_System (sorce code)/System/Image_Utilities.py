# import the necessary packages
import numpy as np
import cv2
import math
from PIL import Image


# The following functions are utilities functions that we use in our system for image processing.


def four_point_transform(image, pts):
    # unpack the points individually
    # rectangle order is: topLeft, topRight, bottomRight,bottomLeft
    rect = pts
    (tl, tr, br, bl) = rect
    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # or the top-right and top-left
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # or the top-left and bottom-left
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    # now that we have the dimensions of the new image, construct
    # the set of destination points, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left order
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")
    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    # return the warped image
    return warped


def draw_coordinates_on_image(image, points):
    # the function gets image and set of coordinates, draw the coordinates on the image and return the new image.
    img = np.copy(image)
    for point in points:
        img = cv2.circle(img, (int(point[0]), int(point[1])), 4, 255, -1)
    return img


def get_mid_point(point1, point2):
    # this function calculate middle point.
    x1, y1 = point1
    x2, y2 = point2
    mid_point = ((x1 + x2) / 2, (y1 + y2) / 2)
    return mid_point


def get_distance(point1, point2):
    # this function calculate distance of two point.
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    return distance


def get_rotation_parameter(vertices):
    # this function gets array of three coordinates and calculate the rotation parameters for 'align_image' function
    left, right, bottom = vertices
    upper_middle = get_mid_point(left, right)
    larynx_center = get_mid_point(upper_middle, bottom)
    yiter = get_distance(left, right)
    # [0] = 'axis-x' value, [1] = 'axis-y' value
    if right[1] < left[1]:  # rotation to the right
        destPoint = np.array([[left[0]], [right[1]]])
        nitav = get_distance(destPoint, right)
        angle = math.degrees(math.acos(nitav / yiter))
        return larynx_center, -angle
    else:  # rotation to the left
        destPoint = np.array([[right[0]], [left[1]]])
        nitav = get_distance(destPoint, left)
        angle = math.degrees(math.acos(nitav / yiter))
        return larynx_center, angle


def align_image(image, vertices):
    # this function gets image and array of three coordinates and align the larynx area.
    center, theta = get_rotation_parameter(vertices)
    # grab the dimensions of the image.
    (height, width) = image.shape[:2]
    (cX, cY) = (width // 2, height // 2)  # center of the original image - optional for rotation
    M = cv2.getRotationMatrix2D(center, theta, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    # compute the new bounding dimensions of the image
    nW = int((height * sin) + (width * cos))
    nH = int((height * cos) + (width * sin))
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    # perform the actual rotation and return the image
    rotated_image = cv2.warpAffine(image, M, (nW, nH))
    # after the image rotation, calculate the new position of the larynx vertices
    new_bb = list(vertices)
    for i, coord in enumerate(vertices):
        # Prepare the vector to be transformed
        v = [coord[0], coord[1], 1]
        calculated = np.dot(M, v)
        new_bb[i] = (calculated[0], calculated[1])
    new_bb = np.array([[new_bb[0][0], new_bb[0][1]],
                       [new_bb[1][0], new_bb[1][1]],
                       [new_bb[2][0], new_bb[2][1]]])
    return rotated_image, new_bb


# this function transform PIL image format to OpenCv image format
def read_and_convert(image_path):
    openCV_image = np.array(Image.open(image_path))
    openCV_image = openCV_image[:, :, ::-1].copy()
    return openCV_image


# this function extract and return the image name from her path.
def image_name_from_path(image_path):
    image_name = image_path.split('/')
    size = len(image_name)
    name = image_name[size - 1]
    return name
