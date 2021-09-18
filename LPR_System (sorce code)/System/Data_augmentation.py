import random
import cv2
import numpy as np
import os

# This code will enable you to preform data augmentation to your data set. To do so, save your images inside the
# input path: "LPR_System/System/" folder. The images must be in '.png' format. the output images will be saved inside
# "LPR_System/System/Data augmentation/" folder.
# select your parameter in the
# 'training_set_augmentation' function below and run the code.

Folder_name = "Data augmentation"  # output path.
Extension = ".png"


# this is the augmentations functions section.
def loadImage(path="."):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.png')]


def scale_image(image, fx, fy, name):
    image = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(Folder_name + "/Scale-" + str(fx) + str(fy) + name + Extension, image)


def sharpen_image(image, name):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    image = cv2.filter2D(image, -1, kernel)
    cv2.imwrite(Folder_name + "/Sharpen-" + name + Extension, image)


def flip_image(image, dir, name):
    image = cv2.flip(image, dir)
    cv2.imwrite(Folder_name + "/flip-" + str(dir) + name + Extension, image)


def add_light(image, name, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")

    image = cv2.LUT(image, table)
    if gamma >= 1:
        cv2.imwrite(Folder_name + "/light-" + str(gamma) + name + Extension, image)
    else:
        cv2.imwrite(Folder_name + "/dark-" + str(gamma) + name + Extension, image)


def fill(img, h, w):
    img = cv2.resize(img, (h, w), cv2.INTER_CUBIC)
    return img


def zoom(img, value, i):
    if value > 1 or value < 0:
        print('Value for zoom should be less than 1 and greater than 0')
        return img
    value = random.uniform(value, 1)
    h, w = img.shape[:2]
    h_taken = int(value * h)
    w_taken = int(value * w)
    h_start = random.randint(0, h - h_taken)
    w_start = random.randint(0, w - w_taken)
    img = img[h_start:h_start + h_taken, w_start:w_start + w_taken, :]
    img = fill(img, h, w)
    cv2.imwrite(Folder_name + "/zoom-" + i + Extension, img)


def rotation(img, angle, i):
    angle = int(random.uniform(-angle, angle))
    h, w = img.shape[:2]
    M = cv2.getRotationMatrix2D((int(w / 2), int(h / 2)), angle, 1)
    img = cv2.warpAffine(img, M, (w, h))
    cv2.imwrite(Folder_name + "/rotation-" + i + Extension, img)


# in this function you can select which type of augmentation to preform on your images.
def training_set_augmentation():
    filenames = loadImage()  # lode images from the input folder: 'LPR_System/System'
    images = []
    for file in filenames:
        images.append(cv2.imread(file, cv2.IMREAD_UNCHANGED))

    # select the augmentations to preform by enable the function below.
    for i, image in enumerate(images):
        # scale_image(image, 0.3, 0.3, str(i))
        # scale_image(image, 3, 3, str(i))
        # sharpen_image(image, str(i))
        flip_image(image, 0, str(i))  # horizontal
        flip_image(image, 1, str(i))  # vertical
        # zoom(image, 0.0001, str(i))
        # rotation(image, 30, str(i))
        # flip_image(image, -1, str(i))  # both
        # add_light(image, str(i), 2.0)
        # add_light(image, str(i), 0.7)


def main():
    training_set_augmentation()


if __name__ == "__main__":
    main()
