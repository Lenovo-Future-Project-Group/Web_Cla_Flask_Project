import os

from dotenv import load_dotenv
from tool import get_file as file


def get_mysql_conn(file_path):
    """
    It connects to a MySQL database.

    :param file_path: The path to the directory where the .env and .pem files are located
    :return: A connection to the database.
    """
    load_dotenv(file.get_all_file(file_path, 0, '.env')['file_path'])

    data = {
        'host': os.getenv('HOST'),
        'user': os.getenv('USERNAMI'),
        'password': os.getenv('PASSWORD'),
        'database': os.getenv('DATABASE'),
        'port': 3306,
        'charset': 'utf8',
        # 'ssl': {'ca': file.get_all_file(file_path, 0, '.pem')['file_path'], },
    }

    return data
