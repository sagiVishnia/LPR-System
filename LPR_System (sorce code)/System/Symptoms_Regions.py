# import the required library
import numpy as np
from System import Image_Utilities


# In the next section we implement the algorithms we wrote in Part I and find the areas of interest for each symptom.

# Subglottic edema symptom relevant area
def find_symptom_1(vertices):
    upper_l, upper_r, bottom = vertices
    # Find right side of the symptom
    width = (Image_Utilities.get_distance(upper_l, upper_r)) / 2
    rect_upper_l = [upper_r[0] - (width / 2), upper_r[1]]  # inside
    rect_upper_r = [rect_upper_l[0] + width, rect_upper_l[1] + (width / 4)]
    rect_down_l = [bottom[0], bottom[1]]  # inside
    rect_down_r = [rect_down_l[0] + width, rect_down_l[1] + (width / 4)]
    right_bounding_box = np.array([rect_upper_l, rect_upper_r, rect_down_r, rect_down_l], dtype="float32")
    # Find left side of the symptom
    rect_upper_r = [upper_l[0] + (width / 2), upper_l[1]]  # inside
    rect_upper_l = [rect_upper_r[0] - width, rect_upper_r[1] + (width / 4)]
    rect_down_r = [bottom[0], bottom[1]]  # inside
    rect_down_l = [rect_down_r[0] - width, rect_down_r[1] + (width / 4)]
    left_bounding_box = np.array([rect_upper_l, rect_upper_r, rect_down_r, rect_down_l], dtype="float32")
    return right_bounding_box, left_bounding_box


# Ventricular obliteration relevant area
def find_symptom_2(vertices):
    upper_l, upper_r, bottom = vertices
    mid_point = Image_Utilities.get_mid_point(upper_l, upper_r)
    mid_point = Image_Utilities.get_mid_point(mid_point, bottom)  # mid_point = larynx center
    width = (Image_Utilities.get_distance(upper_l, upper_r)) / 2
    # Find right side of the symptom
    rect_down_l = [bottom[0], bottom[1] + width / 2]  # Anchor
    rect_upper_l = [upper_r[0] + 10, mid_point[1] - 50]
    rect_upper_r = [rect_upper_l[0] + width, rect_upper_l[1]]
    rect_down_r = [rect_down_l[0] + width, rect_down_l[1]]
    right_bounding_box = np.array([rect_upper_l, rect_upper_r, rect_down_r, rect_down_l], dtype="float32")
    # Find left side of the symptom
    rect_down_r = [bottom[0], bottom[1] + width / 2]  # Anchor
    rect_upper_r = [upper_l[0] - 10, mid_point[1] - 50]
    rect_upper_l = [rect_upper_r[0] - width, rect_upper_l[1]]
    rect_down_l = [rect_down_r[0] - width, rect_down_l[1]]
    left_bounding_box = np.array([rect_upper_l, rect_upper_r, rect_down_r, rect_down_l], dtype="float32")
    return right_bounding_box, left_bounding_box


# erythema relevant area
def find_symptom_3(vertices):
    upper_l, upper_r, bottom = vertices
    width = Image_Utilities.get_distance(upper_l, upper_r)
    # Find right side of the symptom
    rect_upper_l = [upper_r[0], upper_r[1] - width]
    rect_upper_r = [rect_upper_l[0] + width * 2, rect_upper_l[1]]
    rect_down_l = [upper_r[0], upper_r[1] + width]
    rect_down_r = [rect_down_l[0] + width * 2, rect_down_l[1]]
    right_bounding_box = np.array([rect_upper_l, rect_upper_r, rect_down_r, rect_down_l], dtype="float32")
    # Find left side of the symptom
    rect_upper_r = [upper_l[0], upper_l[1] - width]
    rect_upper_l = [rect_upper_r[0] - width * 2, rect_upper_r[1]]
    rect_down_r = [upper_l[0], upper_l[1] + width]
    rect_down_l = [rect_down_r[0] - width * 2, rect_down_r[1]]
    left_bounding_box = np.array([rect_upper_l, rect_upper_r, rect_down_r, rect_down_l], dtype="float32")
    return right_bounding_box, left_bounding_box


# Vocal fold edema symptom relevant area
def find_symptom_4(vertices):
    upper_l, upper_r, bottom = vertices
    # Find right side of the symptom
    width = ((Image_Utilities.get_distance(upper_l, upper_r)) / 2)
    rect_upper_l = [upper_r[0] - 10, upper_r[1]]
    rect_upper_r = [rect_upper_l[0] + (2 * width), rect_upper_l[1]]
    rect_down_l = [bottom[0] - (width / 4), bottom[1] + width / 2]
    rect_down_r = [rect_down_l[0] + width, rect_down_l[1]]
    right_bounding_box = np.array([rect_upper_l, rect_upper_r, rect_down_r, rect_down_l], dtype="float32")
    # Find left side of the symptom
    rect_upper_r = [upper_l[0] + 10, upper_l[1]]
    rect_upper_l = [rect_upper_r[0] - (2 * width), rect_upper_r[1]]
    rect_down_r = [bottom[0] + (width / 4), bottom[1] + width / 2]
    rect_down_l = [rect_down_r[0] - width, rect_down_r[1]]
    left_bounding_box = np.array([rect_upper_l, rect_upper_r, rect_down_r, rect_down_l], dtype="float32")
    return right_bounding_box, left_bounding_box


# Diffuse laryngeal edema symptom relevant area
def find_symptom_5(vertices):
    upper_l, upper_r, bottom = vertices
    # "upper_l, upper_r, bottom" are the upper left, upper right and bottom triangle coordinates.
    width = Image_Utilities.get_distance(upper_r, upper_l) / 2
    rect_upper_l = [upper_l[0] - width, upper_l[1] - width]
    rect_upper_r = [upper_r[0] + width, upper_r[1] - width]
    rect_down_l = [rect_upper_l[0], bottom[1] + width]
    rect_down_r = [rect_upper_r[0], rect_down_l[1]]
    bounding_box = np.array([rect_upper_l, rect_upper_r, rect_down_r, rect_down_l], dtype="float32")
    return bounding_box


# Posterior commissure hypertrophy symptom relevant area
def find_symptom_6(vertices):
    upper_l, upper_r, bottom = vertices
    # "upper_l, upper_r, bottom" are the upper left, upper right and bottom triangle coordinates.
    width = Image_Utilities.get_distance(upper_l, upper_r) / 2
    rect_down_l = [upper_l[0] - (width * (2 / 3)), upper_l[1] + width / 3]
    rect_down_r = [upper_r[0] + (width * (2 / 3)), upper_r[1] + width / 3]
    rect_upper_l = [rect_down_l[0], upper_l[1] - width * 1.5]
    rect_upper_r = [rect_down_r[0], upper_r[1] - width * 1.5]
    bounding_box = np.array([rect_upper_l, rect_upper_r, rect_down_r, rect_down_l], dtype="float32")
    return bounding_box


# Granuloma symptom relevant area, the same as symptom 5
def find_symptom_7(vertices):
    upper_l, upper_r, bottom = vertices
    # "upper_l, upper_r, bottom" are the upper left, upper right and bottom triangle coordinates.
    width = Image_Utilities.get_distance(upper_r, upper_l) / 2
    rect_upper_l = [upper_l[0] - width / 2, upper_l[1] - width / 2]
    rect_upper_r = [upper_r[0] + width / 2, upper_r[1] - width / 2]
    rect_down_l = [rect_upper_l[0], bottom[1] + width / 2]
    rect_down_r = [rect_upper_r[0], rect_down_l[1]]
    bounding_box = np.array([rect_upper_l, rect_upper_r, rect_down_r, rect_down_l], dtype="float32")
    return bounding_box


# Thick endolaryngeal mucus symptom relevant area, the same as symptom 5
def find_symptom_8(vertices):
    bounding_box = find_symptom_7(vertices)
    return bounding_box

