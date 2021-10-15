import os

import cv2
import pandas as pd
import h5py
import numpy as np
from tomni import img_dim
from tomni.make_mask import make_mask_circle
from tqdm import tqdm


def process_images(all_image_names):
    result = pd.DataFrame(columns=["image_name", "colony_area", "ratio_cobelstone"])
    for filename in tqdm(all_image_names):
        with h5py.File(filename, "r") as f:
            # List all groups
            a_group_key = list(f.keys())[0]

            # Get the data
            data = np.array(f[a_group_key])

        img_dim_result = img_dim(data)
        mask = make_mask_circle(img_dim_result, int(min(img_dim_result) * 0.85))

        object_mask = (np.argmax(data, axis=-1) != 3) * mask * 255

        labels = cv2.connectedComponents(object_mask.astype(np.uint8))[1]
        num_biggest_colony = np.argmax(np.bincount(labels.flatten())[1:]) + 1
        mask_biggest_colony = labels == num_biggest_colony

        image_path, image_name = os.path.split(filename)
        colony_area = np.sum(mask_biggest_colony)
        result = result.append(
            {
                "image_name": image_name,
                "is_good": image_name[0].lower() == "g",
                "colony_area": colony_area,
                "ratio_inner_good": np.sum(
                    mask_biggest_colony * (np.argmax(data, axis=-1) == 0)
                )
                / colony_area,
                "ratio_outer_good": np.sum(
                    mask_biggest_colony * (np.argmax(data, axis=-1) == 1)
                )
                / colony_area,
                "ratio_cobelstone": np.sum(
                    mask_biggest_colony * (np.argmax(data, axis=-1) == 2)
                )
                / colony_area,
                "ratio_debri": np.sum(
                    mask_biggest_colony * (np.argmax(data, axis=-1) == 4)
                )
                / colony_area,
            },
            ignore_index=True,
        )
    return result



