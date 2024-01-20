
# Modification date: Sat Oct 14 14:24:22 2023

# Production date: Sat Oct 14 00:39:13 2023

import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
from clear_screen import clear
from datetime import datetime


# Loading bar. Returns the start of the time of the image as [hour, minute, second].
def loadingBar(delta_time, start_time, photos_done, total_photos, arr, i):
    clear()
    backslash = "\\"
    print("Full path of the image: " + arr[i])
    print(
        f"The loop started at {start_time[0]}/{start_time[1]}/{start_time[2]}, {start_time[3]}:{start_time[4]}:{start_time[5]}")
    print(f"Last image done in {delta_time[0]} hours, {delta_time[1]} minutes and {delta_time[2]} seconds.")
    print(f"Image {i + 1} of {total_photos}")
    print(f"The file: {str(arr[i]).split(backslash)[-1]}")
    green_bars_num = int((photos_done / len(arr)) * 100)
    green_bars = " " * green_bars_num
    white_bars = " " * (100 - green_bars_num)
    print(Back.GREEN + green_bars + Back.RED + white_bars)
    the_image_time = datetime.now()
    the_image_time = [the_image_time.hour, the_image_time.minute, the_image_time.second]
    return the_image_time
