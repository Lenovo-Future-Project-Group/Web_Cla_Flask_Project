def get_mysql_list(file_path):
    """
    It reads a file, strips out comments and blank lines, splits the file into a list of SQL statements, and returns the
    list

    :param file_path: The path to the file containing the SQL statements
    :return: A list of strings.
    """

    with open(file_path, 'r', encoding='utf-8') as f:
        data = [_ for _ in ''.join([_.strip('\n') for _ in f.readlines() if not _.lstrip('\n').startswith('--') and _.strip('\n') != '']).split(';') if _ != '']
    return data
