
# Modification date: Thu Jun 16 20:07:36 2022

# Production date: Sat Oct 14 00:05:01 2023

"""

Source: https://stackoverflow.com/questions/44947505/how-to-make-a-movie-out-of-images-in-python


"""




import cv2
import os

image_folder = 'C:\\Users\\emirh\\OneDrive\\Bureau\\My_World_Dont_Change\\dosyalar\\Kodlarim\\Python\\image_old_edit\\destinations\\new vid frames edited\\walk'
video_name = 'walk.mp4'
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
"""
images2 = []
counter = 1
for i in range(len(images)):
    if counter == 4:
        images2.append(images[i])
        counter = 1
    else:
        counter += 1
print("loop done")
"""
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video = cv2.VideoWriter(video_name, fourcc, 60, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
