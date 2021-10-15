import os

import cv2
import pandas as pd
from process_filters import process_images

bad_image_loc = r"D:\CytoData2021\Training\Bad_jpg"
all_bad_image_names = [
    os.path.join(bad_image_loc, i)
    for i in os.listdir(bad_image_loc)
    if i.endswith("_Probabilities.h5")
]

good_image_loc = r"D:\CytoData2021\Training\Good_jpg"
all_good_image_names = [
    os.path.join(good_image_loc, i)
    for i in os.listdir(good_image_loc)
    if i.endswith("_Probabilities.h5")
]

all_image_names = all_good_image_names + all_bad_image_names

result = process_images(all_image_names)
result.to_csv("results_training.csv")

import matplotlib.pyplot as plt

x = result.colony_area
y = result.ratio_cobelstone
colors = result.is_good

plt.xlabel("colony_area")
plt.ylabel("ratio_cobelstone")
plt.scatter(x, y, c=colors, alpha=0.5)
plt.figure(figsize=(16, 16))
plt.show()
