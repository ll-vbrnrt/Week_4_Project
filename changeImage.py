#!/usr/bin/env python3
import os
from PIL import Image

current_working_dir = os.getcwd()
image_dir = current_working_dir+"/supplier-data/images"

files = [file for file in os.listdir(image_dir) if file.endswith('.tiff')]

print(files)
