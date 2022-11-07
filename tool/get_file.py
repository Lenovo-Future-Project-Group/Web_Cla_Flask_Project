import os


def get_all_file(file_dir, file_num=0, file_type='.txt'):
    """
    It returns a dictionary with three keys: file_path, file_name, and file_lens.

    The value of file_path is a list of all the file paths of the files in the directory.

    The value of file_name is a list of all the file names of the files in the directory.

    The value of file_lens is the number of files in the directory.

    The function takes three arguments: file_dir, file_num, and file_type.

    file_dir is the directory of the files.

    file_num is the index of the file you want to get.

    file_type is the type of the files.

    The default value of file_num is 0, which means the first file in the directory.

    The default value of file_type is '.txt', which means the files are text files

    :param file_dir: the directory of the file
    :param file_num: the number of the file you want to get, defaults to 0 (optional)
    :param file_type: the type of file you want to get, default is '.txt', defaults to .txt (optional)
    :return: A dictionary with three keys: file_path, file_name, and file_lens.
    """
    data = {'file_path': [os.path.join(root, file) for root, dirs, files in os.walk(file_dir) for file in files if
                          os.path.splitext(file)[1] == file_type][file_num],
            'file_name': [file for file in os.listdir(file_dir) if os.path.splitext(file)[1] == file_type][file_num],
            'file_lens': len([file for file in os.listdir(file_dir) if os.path.splitext(file)[1] == file_type])}

    return data
