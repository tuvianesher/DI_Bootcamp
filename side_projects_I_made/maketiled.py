from PIL import Image
import imageio
import os

# Set the path to the folder containing the PNG images
folder_path = '380846273'

# Set the output video file name
output_file = 'output101b.mp4'

# Set the target width and height
target_width, target_height = 240, 240

# Set the final video resolution (1080p)
video_width, video_height = 1080, 1920

# Calculate the number of rows and columns needed for tiling
num_rows = video_height // target_height
num_cols = video_width // target_width * 3

# Create a list of all the PNG files in the folder
files = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')])

# Calculate the total number of frames needed to animate the grid
total_frames = len(files)

# Create the output video file using imageio
with imageio.get_writer(output_file, mode='I', fps=60, macro_block_size=8) as writer:
    
    for frame_number in range(total_frames):
        
        # Calculate the frame position within the grid
        x_offset = int((frame_number // (3 + 1/3)))  # Convert to integer
        
        # Create a blank image to use as the frame
        frame_image = Image.new('RGBA', (video_width, video_height), (0, 0, 0, 0))
        
        # Select an image to tile (cycle through images)
        image_index = frame_number % len(files)
        selected_image = files[image_index]
        selected_image_path = os.path.join(folder_path, selected_image)
        
        # Resize the selected image
        with Image.open(selected_image_path) as img:
            img = img.resize((target_width, target_height), resample=Image.NEAREST)
        
        # Create 18 copies of the selected image on the frame
        for i in range(96):
            row = i // num_cols
            col = i % num_cols
            x = col * target_width - x_offset
            y = row * target_height
            frame_image.paste(img, (x, y))
        
        # Convert the PIL Image to a numpy ndarray
        img_array = imageio.core.asarray(frame_image)
        
        # Print the frame and image information
        print(f'Frame {frame_number+1}/{total_frames} - Image {image_index+1}/{len(files)} - Tile Location: x_offset={x_offset}')
        # Crop the resized image
        img = img.crop()

        # Append the image to the output video file
        writer.append_data(img_array)
