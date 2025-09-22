import os


def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    dir_list = os.listdir(full_path)
    if str(directory) not in os.listdir(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(directory):
        return f'"{directory}" is not a directory'
    # items = [
    #     f"{item}: filesize={os.path.getsize(item)}, is_dir={os.path.isdir(item)}"
    #     for item in dir_list
    # ]
    # print(items)
