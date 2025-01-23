import os


def cleanup_temp_files(file_list):
    for file in file_list:
        if os.path.exists(file):
            os.remove(file)
