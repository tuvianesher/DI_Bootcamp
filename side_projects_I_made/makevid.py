import sys
from PIL import Image
import imageio
import os

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 5:
    print("Usage: python script.py folder_path output_file target_width target_height")
    sys.exit(1)

# Extract command-line arguments
folder_path = sys.argv[1]
output_file_base = sys.argv[2]
target_width = int(sys.argv[3])
target_height = int(sys.argv[4])

# Create a list of all the PNG files in the folder
files = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')])

# Create the output GIF file using imageio
gif_output_file = output_file_base + '.gif'
with imageio.get_writer(gif_output_file, mode='I', duration=1/60) as gif_writer:
    for i, file_name in enumerate(files):
        file_path = os.path.join(folder_path, file_name)
        
        # Add a progress bar to the console output
        print(f'Generating GIF: {i+1}/{len(files)}')
        
        # Open the image and resize it
        with Image.open(file_path) as img:
            img = img.resize((target_width, target_height), resample=Image.NEAREST)
            
            # Convert the PIL Image to a numpy ndarray
            img_array = imageio.core.asarray(img)
            
            # Append the image to the output GIF file
            gif_writer.append_data(img_array)

# Create the output MP4 video using imageio
mp4_output_file = output_file_base + '.mp4'
with imageio.get_writer(mp4_output_file, mode='I', fps=60, macro_block_size=8) as mp4_writer:
    for i, file_name in enumerate(files):
        file_path = os.path.join(folder_path, file_name)
        
        # Add a progress bar to the console output
        print(f'Generating MP4: {i+1}/{len(files)}')
        
        # Open the image and resize it
        with Image.open(file_path) as img:
            img = img.resize((target_width, target_height), resample=Image.NEAREST)
            
            # Convert the PIL Image to a numpy ndarray
            img_array = imageio.core.asarray(img)
            
            # Append the image to the output MP4 file
            mp4_writer.append_data(img_array)
