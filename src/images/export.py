import os
import shutil

# Specify source folder containing images
src_folder = 'src/images'

# Specify destination folder where you want to move/copy the entire folder
dest_folder = 'src/main.py'

# Create destination folder if it doesn't exist
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

# Copy the entire folder (including subdirectories and files) to the destination
shutil.copytree(src_folder, dest_folder)

# Now you have exported the entire "images" folder to the specified destination.
