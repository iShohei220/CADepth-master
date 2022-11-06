import os
import numpy as np

from .mono_dataset import MonoDataset

import albumentations as A

class DashcamDataset(MonoDataset):
    def __init__(self, *args, **kwargs):
        super(DashcamDataset, self).__init__(*args, **kwargs)
        # Note that we here assume original dashcam images with resolusion 1920 x 1080 
        # are resized into 1920 x 540 by center-cropping 
        # to make their aspect ratio close to the one of KITTI (1242 x 375)
        self.K = np.array([[0.53, 0, 0.5, 0],
                           [0, 1.89, 0.5, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]], dtype=np.float32)

        self.full_res_shape = (1920, 540)

    def check_depth(self):
        return False

    def get_color(self, folder, frame_index, side, do_flip):
        color = self.loader(self.get_image_path(folder, frame_index))

        if do_flip:
            color = A.augmentations.transforms.HorizontalFlip(p=1)(image=color)['image']

        return color

    def get_image_path(self, folder, frame_index):
        f_str = "{:010d}{}".format(frame_index, self.img_ext)
        image_path = os.path.join(
            self.data_path, folder, f_str)
        return image_path
