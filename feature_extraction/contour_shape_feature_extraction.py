import glob
import math
import os

import cv2
import numpy as np
import pandas as pd
from skimage.filters.rank import entropy
from skimage.morphology import disk
from tomni import img_dim
from tomni.make_mask import make_mask_circle
from tomni.transformers import labels2contours
from tqdm import tqdm

def extract_shape_features(image_loc):
    img = cv2.imread(image_loc, 0)

    result_np = entropy(np.array(img).astype(np.uint8), disk(15))

    img_dim_result = img_dim(result_np)
    mask = make_mask_circle(img_dim_result, int(min(img_dim_result) * 0.85))

    masked_results = result_np * mask

    thresholded_results = masked_results > 3

    labels = cv2.connectedComponents(thresholded_results.astype(np.uint8))[1]
    all_contours = labels2contours(labels)

    if len(all_contours) == 0:
        return {
        "radius_enclosing_circle": 0,
        "area": 0,
        "arc_length": 0,
        "area_convex": 0,
        "arc_length_convex": 0,
        "circularity": 0,
        "max_entropy": float(np.max(masked_results))
    }

    biggest_contour = max(
        all_contours, key=lambda cnt: cv2.contourArea(cnt.astype(np.float32))
    ).astype(np.float32)

    area = cv2.contourArea(biggest_contour)
    arc_length = cv2.arcLength(biggest_contour, True)

    convex_contour = cv2.convexHull(biggest_contour)
    _, radius_enclosing_circle = cv2.minEnclosingCircle(biggest_contour)

    area_convex = cv2.contourArea(convex_contour)
    arc_length_convex = cv2.arcLength(convex_contour, True)

    circularity = area / (radius_enclosing_circle ** 2 * math.pi)

    return {
        "radius_enclosing_circle": radius_enclosing_circle,
        "area": area,
        "arc_length": arc_length,
        "area_convex": area_convex,
        "arc_length_convex": arc_length_convex,
        "circularity": circularity,
        "max_entropy": float(np.max(masked_results))
    }

results = []
for file_name in tqdm(glob.glob(r"D:\CytoData2021\Training\*\*.tif")):
    features = extract_shape_features(file_name)
    features["name"] = str(os.path.split(file_name)[1])
    results.append(features)

results_df = pd.DataFrame(results)
results_df.to_csv("shape_features.tsv", sep="\t")