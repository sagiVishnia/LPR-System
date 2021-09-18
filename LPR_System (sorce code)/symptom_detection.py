from PIL import Image
import cv2
import numpy as np
import tensorflow as tf
from yolov3_tf2.models import YoloV3
from yolov3_tf2.dataset import transform_images, load_tfrecord_dataset
from yolov3_tf2.utils import draw_outputs
import os

# global parameters for YoloV3 model
size = 416  # size images are resized to for the model
num_classes = 2  # number of classes in model
# parameters for GUI running
classes_path = '../data/labels/LPR.names'  # path to classes names
output_path = '../detections/'  # path to output folder where images with detections are saved
weights_dir = '../weights'  # path to weights directory
images_path = "../data/images"  # path to input images
# parameters for console running
# classes_path = 'data/labels/LPR.names'  # path to classes names
# output_path = 'detections/'  # path to output folder where images with detections are saved
# weights_dir = 'weights'  # path to weights directory
# images_path = "data/images"  # path to input images


def set_model():  # initialize the model
    # check for CPU/GPU requirement
    physical_devices = tf.config.experimental.list_physical_devices('GPU')
    if len(physical_devices) > 0:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
    # built yolo model
    yolo = YoloV3(classes=num_classes)
    # load classes from classes_path
    class_names = [c.strip() for c in open(classes_path).readlines()]
    print('classes loaded')
    return yolo, class_names


# the function 'loadImage' create list of '.png' images in the input folder - "data/images"
def loadImage(path=images_path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.png')]


# the function 'get_detections' detect the symptoms from the images in the input folder
# and returns the classes found in them
def get_detections(symptoms_arr):
    yolo, class_names = set_model()
    raw_images = []  # images for detection in yolo format
    image_names = []  # the images names for detection
    temp_images = []  # temp array that open images, append them to raw_images and return there names
    loaded_weight = -1  # this parameter signal the model if the correct weight was loaded
    img_cnt = 0  # image counter to write the images to folder

    # get all files from the input folder
    filenames = loadImage()
    # read all images in the list and append them to temp_images
    for file in filenames:
        temp_images.append(Image.open(file))
    # for every image in temp_images, transform it to yolo format and append to raw_images
    for image in temp_images:
        image_name = image.filename
        image_names.append(image_name)
        image.save(os.path.join(os.getcwd(), image_name))
        img_raw = tf.image.decode_image(open(image_name, 'rb').read(), channels=3)
        raw_images.append(img_raw)

    for j in range(len(raw_images)):
        img_cnt += 1
        raw_img = raw_images[j]
        img = tf.expand_dims(raw_img, 0)
        img = transform_images(img, size)
        img_name = image_names[j]
        # for each image we load the symptom weights into the model according to the symptom number: 1-8
        if img_name.endswith('_1.png') and loaded_weight != 1:
            weights_path = weights_dir + '/1/yolov3.tf'
            yolo.load_weights(weights_path).expect_partial()
            loaded_weight = 1
            print('symptom 1 weights loaded')
        elif img_name.endswith('_2.png') and loaded_weight != 2:
            weights_path = weights_dir + '/2/yolov3.tf'
            yolo.load_weights(weights_path).expect_partial()
            loaded_weight = 2
            print('symptom 2 weights loaded')
        elif img_name.endswith('_3.png') and loaded_weight != 3:
            weights_path = weights_dir + '/3/yolov3.tf'
            yolo.load_weights(weights_path).expect_partial()
            loaded_weight = 3
            print('symptom 3 weights loaded')
        elif img_name.endswith('_4.png') and loaded_weight != 4:
            weights_path = weights_dir + '/4/yolov3.tf'
            yolo.load_weights(weights_path).expect_partial()
            loaded_weight = 4
            print('symptom 4 weights loaded')
        elif img_name.endswith('_5.png') and loaded_weight != 5:
            weights_path = weights_dir + '/5/yolov3.tf'
            yolo.load_weights(weights_path).expect_partial()
            loaded_weight = 5
            print('symptom 5 weights loaded')
        elif img_name.endswith('_6.png') and loaded_weight != 6:
            weights_path = weights_dir + '/6/yolov3.tf'
            yolo.load_weights(weights_path).expect_partial()
            loaded_weight = 6
            print('symptom 6 weights loaded')
        elif img_name.endswith('_7.png') and loaded_weight != 7:
            weights_path = weights_dir + '/7/yolov3.tf'
            yolo.load_weights(weights_path).expect_partial()
            loaded_weight = 7
            print('symptom 7 weights loaded')
        elif img_name.endswith('_8.png') and loaded_weight != 8:
            weights_path = weights_dir + '/8/yolov3.tf'
            yolo.load_weights(weights_path).expect_partial()
            loaded_weight = 8
            print('symptom 8 weights loaded')
        # 'yolo(img)' do the detection and return the results
        boxes, scores, classes, nums = yolo(img)
        symptom_position = loaded_weight - 1
        Temp = 'None'
        tbl_num = str(loaded_weight)
        # save the detection results
        if str(range(nums[0])) == "range(0, 0)":
            symptoms_arr[symptom_position].add_result("Unknown", -1, -1, tbl_num)

        for i in range(nums[0]):
            Temp = class_result = str(class_names[int(classes[0][i])])
            class_num = int(classes[0][i])
            confidence = str(float("{0:.2f}".format(np.array(scores[0][i]) * 100)))
            symptoms_arr[symptom_position].add_result(class_result, class_num, confidence, tbl_num)
        print('image name: ', img_name, '\nYolo result = ' + Temp)
        # # use this section if you want to write the result images to detection folder. # #
        # img = cv2.cvtColor(raw_img.numpy(), cv2.COLOR_RGB2BGR)
        # img = draw_outputs(img, (boxes, scores, classes, nums), class_names)
        # cv2.imshow('symptom', img)
        # cv2.waitKey()
        # cv2.destroyAllWindows()
        # cv2.imwrite(output_path + 'detection' + img_name + '.png', img)
        # print('output saved to: {}'.format(output_path + 'detection' + str(img_cnt) + '.jpg'))