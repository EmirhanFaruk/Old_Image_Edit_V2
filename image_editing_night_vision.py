
# Modification date: Sat Jan  8 14:47:02 2022

# Production date: Sat Oct 14 00:05:01 2023

import os
from PIL import Image
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from clear_screen import clear#clear()
from datetime import datetime
import random
import math



def paths():

    prefixes = str(input("Enter the prefix of the edited images: "))

    if prefixes == "" or prefixes == "conda activate imgedit":
        prefixes = "file_name_"
    else:
        prefixes = prefixes + "_"

    print(f"Using the prefix: {prefixes}")

    the_name_of_the_file = input("Enter the name of the source file: ")


    if the_name_of_the_file == "" or the_name_of_the_file == "conda activate imgedit":
        the_name_of_the_file = "\\sources\\used\\the_images"
    else:
        the_name_of_the_file = "\\" + the_name_of_the_file

    print("Using the file: " + the_name_of_the_file[1:])
    the_name_of_the_file2 = the_name_of_the_file.split("\\", 1)[1]

    #\\the_edited_images
    the_destination_file = input("Enter the destination file: ")

    if the_destination_file == "" or the_destination_file == "conda activate imgedit":
        the_destination_file = "\\destinations\\the_edited_images\\used2"
    else:
        the_destination_file = "\\" + the_destination_file
    
    print("Using the destination file: " + the_destination_file[1:])


    try:
        starting_point = int(input("Enter the starting point: "))
        print("Using starting point: " + starting_point)
    except Exception as expection:
        print("Error: " + str(expection) + "\nAccepting starting point as 0.")
        starting_point = 0
    

    try:
        ending_point = int(input("Enter the ending point: "))
        print("Using ending point: " + ending_point)
    except Exception as expection:
        print("Error: " + str(expection) + "\nAccepting ending point as the last image.")
        ending_point = -1





    print(f"\n\n\nUsing the prefix: {prefixes}\nUsing the file: {the_name_of_the_file[1:]}\nUsing the destination file: {the_destination_file[1:]}\nUsing the starting point: {starting_point}\nUsing the ending point: {ending_point}")
    the_answer = input("\nAre those paths good? (y for yes, put anything but y to reenter)\n: ")
    if the_answer == "y":  
        return the_name_of_the_file, the_destination_file, the_name_of_the_file2, prefixes, starting_point, ending_point
    else:
        clear()
        return paths()

the_name_of_the_file, the_destination_file, the_name_of_the_file2, prefixes, starting_point, ending_point = paths()


arr = os.listdir("C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit" + the_name_of_the_file)

larr = len(arr)
for i in range(larr):
    arr[i] = f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\Python\\image_old_edit{the_name_of_the_file}\\" + arr[i]

"""
if ending_point == -1:
    arr = arr[starting_point:]
else:
    arr = arr[starting_point:ending_point]
"""
arr = arr[1335:]
larr = len(arr)

sussy_file_name = f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\Python\\image_old_edit{the_name_of_the_file}\\"
"""
for i in range(len(arr)):
        arr[i] = "C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\Python\\image_old_edit\\the_images\\" + arr[i]
        os.rename(arr[i], f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\Python\\image_old_edit\\the_images\\sc_{i + 1}.png")
"""

start_time = datetime.now()
start_time2 = time.time()
start_time3 = datetime.now()
start_time = [start_time.year, start_time.month, start_time.day, start_time.hour, start_time.minute, start_time.second]
#start_time[3] + start_time[4] + start_time[5] for h/m/s


# Loading bar. Returns the start of the time of the image as [hour, minute, second].
def load_bar(delta_time, start_time, photos_done, total_photos, arr, i):
    clear()
    print("Using the folder: " + the_name_of_the_file[1:])
    print(f"The loop started at {start_time[0]}/{start_time[1]}/{start_time[2]}, {start_time[3]}:{start_time[4]}:{start_time[5]}")
    print(f"Last image done in {delta_time[0]} hours, {delta_time[1]} minutes and {delta_time[2]} seconds.")
    print(f"Image {i + 1} of {total_photos}")
    print(f"The file: {str(arr[i]).split(sussy_file_name)[1]}")
    green_bars_num = int((((photos_done) / len(arr)) * 100))
    green_bars = " " * green_bars_num
    white_bars = " " * (100 - green_bars_num)
    print(Back.GREEN + green_bars + Back.RED + white_bars)
    the_image_time = datetime.now()
    the_image_time = [the_image_time.hour, the_image_time.minute, the_image_time.second]
    return the_image_time



line = []
with open("C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit\\The_Try.txt", "r") as f:
    line = f.readlines()
f.close()
n_try = int(line[0])
with open("C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit\\The_Try.txt", "w") as f:
    line = f.write(str(n_try + 1))
f.close()


f = open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit\\the_logs.txt", "a")
f.write(f"\n\n\n---------------------------------------------------------------------\n\n\nTry {n_try}, using the folder {the_name_of_the_file[1:]}, using the night vision edit started at {start_time[0]}/{start_time[1]}/{start_time[2]}, {start_time[3]}:{start_time[4]}:{start_time[5]}\n\n\n")
f.close()

now_for_imgs = datetime.now()
delta_time = [0, 0, 0]
photos_done = 0
total_photos = larr

dissortion_list = ["bright", "dark"]
for i in range(18):
	dissortion_list.append("normal")

for i in range(len(arr)):
    now_for_imgs = datetime.now()
    dt_string1 = now_for_imgs.strftime("%d/%m/%Y %H:%M:%S")
    image = Image.open(arr[i])
    width, height = image.size
    
    the_image_time = load_bar(delta_time, start_time, photos_done, total_photos, arr, i)

	
	
    the_cercle_list = []
	
    for w in range(width):
        #print(f"{w}/{width}")
        for h in range(height):
            rgb = image.getpixel((w, h))
            rgbs = rgb[0] + rgb[1] + rgb[2]
            da_choice = random.choice(dissortion_list)
            origin_x = width // 2
            origin_y = height // 2
            curr_x = w - origin_x
            curr_y = h - origin_y


            radius = width // 9
            point_distance = math.sqrt((abs(curr_x)**2) + (abs(curr_y)**2))
            probability_circle = [False]
            for j in range(4):
                probability_circle.append(True)
                continue
            if point_distance <= radius:
                if random.choice(probability_circle):
                    dans_le_cercle = True
                else:
                    dans_le_cercle = False
            else:
                dans_le_cercle = False
            


            if point_distance < radius + 3 and not dans_le_cercle:
                    if 2 == random.randint(1, 3):
                        dans_le_cercle = True
            if point_distance < radius + 5 and not dans_le_cercle:
                if 2 == random.randint(1, 4):
                    dans_le_cercle = True
            if point_distance < radius + 7 and not dans_le_cercle:
                if 2 == random.randint(1, 5):
                    dans_le_cercle = True
            if point_distance < radius + 9 and not dans_le_cercle:
                if 2 == random.randint(1, 6):
                    dans_le_cercle = True

            if point_distance < radius + 11 and not dans_le_cercle:
                if 2 == random.randint(1, 7):
                    dans_le_cercle = True

            if point_distance < radius + 13 and not dans_le_cercle:
                if 2 == random.randint(1, 8):
                    dans_le_cercle = True



            radius_petit = width // 10
            point_distance_petit = math.sqrt((abs(curr_x)**2) + (abs(curr_y)**2))
            #dans_le_petit_cercle = radius_petit >= point_distance_petit
            if point_distance_petit > radius_petit:
                dans_le_petit_cercle = False
            else:
                dans_le_petit_cercle = True
            
            #print(f"{w}, {h}  dans_le_petit_cercle = {dans_le_petit_cercle}, dans_le_cercle = {dans_le_cercle}")

            green = rgb[1]
            
            if dans_le_petit_cercle:   #w > width//3 and w < (width//3)*2 and h > height//3 and h < (height//3)*2:
                the_cercle_list.append([(rgb), [w, h]])
                    
                if da_choice == "normal":
                    rgb2 = (0, rgbs, 0)
                    image.putpixel((w, h), rgb2)
                elif da_choice == "dark":
                    if rgbs - 40 <= 0:
                        green = random.randint(0, rgbs)
                    else:
                        green = random.randint(rgbs - 40, rgbs)
                    rgb2 = (0, green, 0)
                    image.putpixel((w, h), rgb2)
                elif da_choice == "bright":
                    if rgbs >= 255:
                        rgbs = 255
                    elif rgbs + 40 >= 255:
                        green = random.randint(rgbs, 255)
                    else:
                        green = random.randint(rgbs, rgbs + 40)
                    rgb2 = (0, green, 0)
                    image.putpixel((w, h), rgb2)
            elif dans_le_cercle:
                if da_choice == "normal":
                    rgb2 = (0, rgbs, 0)
                    image.putpixel((w, h), rgb2)
                elif da_choice == "dark":
                    if rgbs - 40 <= 0:
                        green = random.randint(0, rgbs)
                    else:
                        green = random.randint(rgbs - 40, rgbs)
                    rgb2 = (0, green, 0)
                    image.putpixel((w, h), rgb2)
                elif da_choice == "bright":
                    if rgbs >= 255:
                        rgbs = 255
                    elif rgbs + 40 >= 255:
                        green = random.randint(rgbs, 255)
                    else:
                        green = random.randint(rgbs, rgbs + 40)
                    rgb2 = (0, green, 0)
                    image.putpixel((w, h), rgb2)
            else:
                if da_choice == "normal":
                    rgb2 = (0, rgb[1], 0)
                    image.putpixel((w, h), rgb2)
                elif da_choice == "dark":
                    if rgb[1] - 40 <= 0:
                        green = random.randint(0, rgb[1])
                    else:
                        green = random.randint(rgb[1] - 40, rgb[1])
                    rgb2 = (0, green, 0)
                    image.putpixel((w, h), rgb2)
                elif da_choice == "bright":
                    if green >= 255:
                        green = 255
                    elif rgb[1] + 40 >= 255:
                        green = random.randint(rgb[1], 255)
                    else:
                        green = random.randint(rgb[1], rgb[1] + 40)
                    rgb2 = (0, green, 0)
                    image.putpixel((w, h), rgb2)


    somme = 0
    for piksel in the_cercle_list:
        somme += piksel[0][1]
        #print(f"somme = {somme}, piksel = {piksel}")

    moyenne = int(somme / len(the_cercle_list))

    if moyenne < 60:
        for da_baby in the_cercle_list:
            w, h = da_baby[1][0], da_baby[1][1]





            another_probability_list = [False]
            for j in range(99):
                another_probability_list.append(True)
            if random.choice(another_probability_list):
                rgbs = da_baby[0][0] + da_baby[0][1] + da_baby[0][2] + 40
            else:
                rgbs = da_baby[0][0] + da_baby[0][1] + da_baby[0][2]
            if rgbs > 255:
                rgbs = 255
            if da_choice == "normal":
                rgb2 = (0, rgbs, 0)
                image.putpixel((w, h), rgb2)
            elif da_choice == "dark":
                if rgbs - 40 <= 0:
                    rgbs = random.randint(0, rgbs)
                else:
                    rgbs = random.randint(rgbs - 40, rgbs)
                rgb2 = (0, rgbs, 0)
                image.putpixel((w, h), rgb2)
            elif da_choice == "bright":
                if rgbs >= 255:
                    rgbs = 255
                elif rgbs + 40 >= 255:
                    rgbs = random.randint(rgbs, 255)
                else:
                    rgbs = random.randint(rgbs, rgbs + 40)
                rgb2 = (0, rgbs, 0)
                image.putpixel((w, h), rgb2)





    path = f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit{the_destination_file}\\{the_name_of_the_file2}{the_name_of_the_file2}{str(str(arr[i]).split(sussy_file_name)[1])[:-3]}%#05d" % (i+1) + ".png"
    image.save(path, "png")
    image.close()
    photos_done += 1
    
    the_image_time_end = datetime.now()
    the_image_time_end = [the_image_time_end.hour, the_image_time_end.minute, the_image_time_end.second]
    delta_time = [the_image_time_end[0] - the_image_time[0], the_image_time_end[1] - the_image_time[1], the_image_time_end[2] - the_image_time[2]]
    if delta_time[2] < 0:
        delta_time[2] = delta_time[2] + 60
        delta_time[1] -= 1
    if delta_time[1] < 0:
        delta_time[1] = delta_time[1] + 60
        delta_time[0] -= 1
    f = open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit\\the_logs.txt", "a")
    f.write(f"\n\nImage {i + 1} ({str(arr[i]).split(sussy_file_name)[1]}) from the folder {the_name_of_the_file[1:]}, using the night vision edit has been done in {delta_time[0]} hours, {delta_time[1]} minutes and {delta_time[2]} seconds.")
    f.close()



finish = time.time()

total_time = finish - start_time2

now2 = datetime.now()
# dd/mm/YY H:M:S
dt_string = start_time3.strftime("%d/%m/%Y %H:%M:%S")
print("Started at ", dt_string)	
# dd/mm/YY H:M:S
dt_string = now2.strftime("%d/%m/%Y %H:%M:%S")


f = open(f"C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit\\the_logs.txt", "a")

f.write(f"\n\n\nTry {n_try}, using the folder {the_name_of_the_file[1:]}, using the night vision edit, all done in {int(total_time)} seconds({int(total_time/60)} minutes and {int(total_time % 60)} seconds). The program ended at {dt_string}")

f.close()

print("Ended at ", dt_string)	
print(f"All done in {total_time}")

input("Press enter to continue...")
