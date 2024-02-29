'''Write a program that walks through a folder tree and searches for exceptionally large files or 
folders—say, ones that have a file size of more than 100MB.

'''
import os



def find_large_files(folder_path, threshold_size):

    #walk over the folder tree
    for foldername, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            # Check if the file size exceeds the threshold size

            file_size = os.path.getsize(file_path)
            if file_size > threshold_size:
                print(f"File:{file_path} - Size: {file_size} bytes")
       
            
# Specify the folder path to search and the threshold size in bytes (100MB = 100 * 1024 * 1024 bytes)
      
folder_to_search = '/home/peter/Videos'
threshold_size = 2 * 1024 * 1024 #100MB

find_large_files(folder_to_search, threshold_size)
