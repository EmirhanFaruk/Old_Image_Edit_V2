
# Modification date: Sat Oct 14 14:35:25 2023

# Production date: Sat Oct 14 00:05:01 2023

import os
from PIL import Image
import time
from datetime import datetime
import random

from GetPaths import getPaths
from LoadingBar import loadingBar

# Getting the
source_file_path, output_file_path, prefixes = getPaths()

path = os.getcwd()

arr = os.listdir(path + source_file_path)

larr = len(arr)
for i in range(larr):
    arr[i] = f"{path}{source_file_path}\\" + arr[i]

full_source_file_path = f"{path}{source_file_path}\\"

start_time_ = datetime.now()
start_time2 = time.time()
start_time = [start_time_.year, start_time_.month, start_time_.day, start_time_.hour, start_time_.minute,
              start_time_.second]
# start_time[3] + start_time[4] + start_time[5] for h/m/s


delta_time = [0, 0, 0]
photos_done = 0
total_photos = larr
# 1/80
will_black_line = [True]
for i in range(149):
    will_black_line.append(False)

will_disorted = [True]
for i in range(19):
    will_disorted.append(False)

for i in range(len(arr)):
    image = Image.open(arr[i])
    if image.mode != "RGBA":
        image = image.convert("RGBA")
    width, height = image.size

    the_image_time = loadingBar(delta_time, start_time, photos_done, total_photos, arr, i)
    for w in range(width):
        random_number = random.randint(0, 500)
        if random_number == 20:  # random.choice(will_black_line):
            w1 = True
        else:
            w1 = False
        # time things
        img_break_time = time.time()
        current_running_time = int(img_break_time - start_time2)

        for h in range(height):
            if w1:
                image.putpixel((w, h), (0, 0, 0, 0))
            else:
                r, g, b, a = image.getpixel((w, h))

                # Calculate the grayscale tone
                the_gray_tone = (r + g + b) // 3

                if random.choice(will_disorted):
                    da_tone = random.randint(0, 30)
                    liste = ["brighter", "darker", "gray"]
                    secim = random.choice(liste)
                    if secim == "brighter":
                        # Increase the tone, taking into account the alpha channel
                        r2 = min(the_gray_tone + da_tone, 255)
                        g2 = min(the_gray_tone + da_tone, 255)
                        b2 = the_gray_tone * 2 // 5
                    elif secim == "darker":
                        # Decrease the tone, taking into account the alpha channel
                        r2 = max(the_gray_tone - da_tone, 0)
                        g2 = max(the_gray_tone - da_tone, 0)
                        b2 = the_gray_tone * 2 // 5
                    else:
                        r2 = the_gray_tone
                        g2 = the_gray_tone
                        b2 = the_gray_tone * 2 // 5

                    # Set the modified pixel back into the image
                    image.putpixel((w, h), (r2, g2, b2, a))
                else:
                    # Set the modified pixel back into the image
                    image.putpixel((w, h), (the_gray_tone, the_gray_tone, the_gray_tone * 2 // 5, a))
    path2 = f"{path}{output_file_path}\\{prefixes}{str(str(arr[i]).split(full_source_file_path)[1])[:-3]}" + ".png"
    image.save(path2, "png")
    image.close()
    photos_done += 1

    the_image_time_end = datetime.now()
    the_image_time_end = [the_image_time_end.hour, the_image_time_end.minute, the_image_time_end.second]
    delta_time = [the_image_time_end[0] - the_image_time[0], the_image_time_end[1] - the_image_time[1],
                  the_image_time_end[2] - the_image_time[2]]
    if delta_time[2] < 0:
        delta_time[2] = delta_time[2] + 60
        delta_time[1] -= 1
    if delta_time[1] < 0:
        delta_time[1] = delta_time[1] + 60
        delta_time[0] -= 1

finish = time.time()

total_time = finish - start_time2

now2 = datetime.now()
# dd/mm/YY H:M:S
dt_string = start_time_.strftime("%d/%m/%Y %H:%M:%S")
print("Started at ", dt_string)
# dd/mm/YY H:M:S
dt_string = now2.strftime("%d/%m/%Y %H:%M:%S")

print("Ended at ", dt_string)
print(f"All done in {total_time}")
input("Press Enter to exit...")
