import os


def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory)) + os.sep

    if not full_path.startswith(os.path.abspath(working_directory + os.sep)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    for item in os.listdir(full_path):
        print(f"{item}: filesize={os.path.getsize(os.path.abspath(os.path.join(full_path, item)))}, is_dir={os.path.isdir(os.path.abspath(dir_item))}")

    # items = [
    #     f"{item}: filesize={os.path.getsize(item)}, is_dir={os.path.isdir(item)}"
    #     for item in dir_list
    # ]
    # print(items)
