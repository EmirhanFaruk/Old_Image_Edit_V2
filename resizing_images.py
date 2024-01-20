
# Modification date: Mon Jan  3 19:01:38 2022

# Production date: Sat Oct 14 00:05:01 2023

import os
from PIL import Image


arr = os.listdir("C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\Python\\image_old_edit\\sources\\they_hunger_long_frames")

for i in range(len(arr)):
    image = Image.open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit\\sources\\they_hunger_long_frames\\{arr[i]}")
    image = image.resize((1280, 720))
    image.save(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit\\sources\\they_hunger_long_frames2\\resized_to_720p_they_hunger_long_frames_{arr[i]}", "png")
    image.close()