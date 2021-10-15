import os

import cv2
import pandas as pd
from process_filters import process_images

image_loc = r"D:\CytoData2021\Test\Test_1_jpg"
all_image_names = [
    os.path.join(image_loc, i)
    for i in os.listdir(image_loc)
    if i.endswith("_Probabilities.h5")
]


result = process_images(all_image_names)
result.to_csv("results_test1.csv")

