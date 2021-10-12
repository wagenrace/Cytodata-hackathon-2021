import os
import sys
import cv2
from pathlib import Path

from tomni.bbox_fitting import bbox_fitting

basefolder_loc = Path(os.path.abspath("")).parents[0]
sys.path.append(str(basefolder_loc))

from feature_engineering.load_data import load_biobit_features

result_location = os.path.join(os.path.abspath(""), "training_data")
os.makedirs(result_location, exist_ok=True)
bitbio_data = load_biobit_features()

good_loc = r"D:\CytoData2021\Training\Good"
bad_loc = r"D:\CytoData2021\Training\Bad"

all_image_names = bitbio_data.index.to_numpy()
for image_name in all_image_names:
    bouding_boxes = bitbio_data.loc[[image_name]]
    if image_name.startswith("Good"):
        image_loc = os.path.join(good_loc, image_name)
    else:
        image_loc = os.path.join(bad_loc, image_name.replace(".tiff", ".tif"))
    full_image = cv2.imread(image_loc)
    for index, row in bouding_boxes.iterrows():
        if row.ObjectNumber != 1:
            continue
        bounding_box = row[
            [
                "AreaShape_BoundingBoxMinimum_X",
                "AreaShape_BoundingBoxMinimum_Y",
                "AreaShape_BoundingBoxMaximum_X",
                "AreaShape_BoundingBoxMaximum_Y",
            ]
        ]
        colony_image = bbox_fitting(full_image, *bounding_box.to_numpy())

        output_image_name = index.replace(".tiff", f"_{row.ObjectNumber}.jpeg").replace(".tif", f"_{row.ObjectNumber}.jpeg")

        cv2.imwrite(os.path.join(result_location, output_image_name), colony_image)
