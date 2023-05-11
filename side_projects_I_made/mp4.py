import os
import imageio
from PIL import Image

# Set the path to the folder containing the PNG images
folder_path = 'proj_12_i'

# Set the output video file name
output_file = 'output.mp4'

# Set the target width and height
target_width, target_height = 1080, 1920

# Create a list of all the PNG files in the folder
files = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')])

# Create a list of PIL Image objects, resizing each image to the target size
images = [Image.open(os.path.join(folder_path, f)).resize((target_width, target_height), resample=Image.NEAREST) for f in files]

# Create the output video file using imageio
with imageio.get_writer(output_file, mode='I', fps=60) as writer:
    for i, img in enumerate(images):
        # Convert the PIL Image to a numpy ndarray
        img_array = imageio.core.asarray(img)
        
        # Add a progress bar to the console output
        print(f'Processing frame {i+1}/{len(images)}...')
        
        # Append the image to the output video file
        writer.append_data(img_array)
