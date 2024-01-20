
# Modification date: Sat Oct 14 01:43:05 2023

# Production date: Sat Oct 14 00:25:52 2023

from clear_screen import clear
import os

def getPaths():
    backslash = "\\"

    prefixes = input("Enter the prefix of the edited images: ")

    if prefixes == "" or prefixes == "conda activate imgedit":
        prefixes = ""
    else:
        prefixes = prefixes + "_"

    print(f"Using the prefix: {prefixes}")

    source_file_path = input("Enter the name of the source file: ")


    if source_file_path == "" or source_file_path == "conda activate imgedit":
        source_file_path = r'\sources\images'
    else:
        
        source_file_path = backslash + source_file_path

    print("Using the file: " + source_file_path[1:])
    
    

    #\\the_edited_images
    output_file_path = input("Enter the destination file: ")

    if output_file_path == "" or output_file_path == "conda activate imgedit":
        output_file_path = r'\destinations\the_edited_images'
    else:
        output_file_path = backslash + output_file_path
    
    print("Using the destination file: " + output_file_path[1:])

    print(f"\n\n\nUsing the prefix: {prefixes}\nUsing the file: {source_file_path[1:]}\nUsing the destination file: {output_file_path[1:]}")
    
    files = os.listdir(os.getcwd() + source_file_path)
    print("\nThe files in the said folder:")
    for file in files:
        print(file)
    
    the_answer = input("\nAre these paths good? (y for yes, put anything but y to reenter)\n: ")
    if the_answer == "y":  
        return source_file_path, output_file_path, prefixes
    else:
        clear()
        return getPaths()