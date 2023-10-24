import numpy as np
import pandas as pd
from skimage import io, measure

# Load the image and mask image
image_path = 'imgs/img2.jpeg'
mask_path = 'mask.npy'

image = io.imread(image_path)
markers = np.load(mask_path)

pixels_to_um = 0.325  # 1 pixel = 325 nm

# Now, time to extract properties of detected cells
# regionprops function in skimage measure module calculates useful parameters for each object.
regions = measure.regionprops(markers, intensity_image=image)

# convert the list of region properties into a Pandas dataframe
df = pd.DataFrame(columns=['ID',
                           'Area (Pixel)',
                           'Area (um)',
                           'equivalent_diameter',
                           'MajorAxisLength',
                           'MinorAxisLength',
                           'Perimeter',
                           'MinIntensity',
                           'MaxIntensity'])

for id, region in enumerate(regions):
    new_row = {'ID': id + 1,    # ID is 1-based, instead of 0-based like Python
               'Area (Pixel)': region.area,
               'Area (um)': region.area * pixels_to_um ** 2,
               'equivalent_diameter': region.equivalent_diameter,
               'MajorAxisLength': region.major_axis_length,
               'MinorAxisLength': region.minor_axis_length,
               'Perimeter': region.perimeter,
               'MinIntensity': region.min_intensity,
               'MaxIntensity': region.max_intensity}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# save to csv with .2 precision
df = df.round(2)
df.to_csv('cell_measurements.csv', index=False)