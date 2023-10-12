import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from segment_anything import sam_model_registry, SamPredictor

from utils import *

class SAM(SamPredictor):
    def __init__(self, sam_checkpoint="checkpoints/sam_vit_h_4b8939.pth", model_type="vit_h", device="cuda"):

        sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
        sam.to(device=device)
        self.predictor = super().__init__(sam)

# model parameters
sam_checkpoint = "checkpoints/sam_vit_h_4b8939.pth"
model_type = "vit_h"
device = "cuda"
predictor = SAM()

image_path = select_file()
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image = adjust_histogram_gui(image)

plt.figure(figsize=(10,10))
plt.imshow(image)
plt.axis('on')
plt.show()

predictor.set_image(image)

points, _, labels = annotate_image_gui(image)
input_point = np.array(points)
input_label = np.array(labels)

masks, scores, logits = predictor.predict(
    point_coords=input_point,
    point_labels=input_label,
    box = np.array((0, 0, image.shape[1], image.shape[0])),
    multimask_output=True)

for i, (mask, score) in enumerate(zip(masks, scores)):
    plt.figure(figsize=(10,10))
    plt.imshow(image)
    show_points(input_point, input_label, plt.gca())
    show_mask(mask, plt.gca())
    plt.title(f"Mask {i+1}, Score: {score:.3f}", fontsize=18)
    plt.axis('off')
    plt.show()

# save mask
best_mask = 3

input_name = os.path.splitext(image_path)[0]
output_name = input_name + '_mask' + os.path.splitext(image_path)[1]
cv2.imwrite(output_name, np.array(masks[best_mask -1, ...]*255, dtype=np.uint8))

print('mask saved as: {}'.format(output_name))

