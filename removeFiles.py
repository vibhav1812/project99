import os
import shutil
import time

def main():
    deleted_folders_count = 0
    deleted_files_count = 0

    path = input("Enter the name of the directory to be deleted")
    days = 30

    #converting days into seconds 
    seconds = time.time() - (days*24*60*60)

    if os.path.exists(path):
        list_of_files = os.walk(path)
        print(list_of_files)
        for root_folder, folders, files in list_of_files:
            if seconds >= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deleted_folders_count += 1
                break
            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder, folder)
                    if seconds >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folders_count += 1
                for file in files:
                    file_path = os.path.join(root_folder, file)
                    if seconds >= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deleted_files_count += 1
        else:
            if seconds >= get_file_or_folder_age(file_path):
                remove_file(file_path)
                deleted_files_count += 1
    else:
        print("Path does not exist")


def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

def remove_folder(path):
    if shutil.rmtree(path):
        print(f"{path} is removed successfully")
    else:
        print(f"{path} Path is unable to be deleted")

def remove_file(path):
    if os.remove(path):
        print(f"{path} is removed successfully")
    else:
        print(f"{path} Unable to delete the path")