import os


def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory)) + os.sep

    if not full_path.startswith(os.path.abspath(working_directory + os.sep)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    try:
        file_list = os.listdir(full_path)
    except PermissionError:
        return f'Error: Perssion denied listing "{directory}"'
    except OSError as err:
        return f'Error: Could not list "{directory}": {err}'

    dir_list_formatted = []
    for item in file_list:
        fp_item = os.path.join(full_path, item)
        fp_item_size = os.path.getsize(fp_item)
        fp_item_is_dir = os.path.isdir(fp_item)
        dir_list_formatted.append(
            f"- {item}: filesize={fp_item_size} bytes, is_dir={fp_item_is_dir}"
        )

    return "\n".join(dir_list_formatted)
