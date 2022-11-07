from init import mysql_conn as conf

# 配置文件

# mysql数据库配置
MYSQL_CONFIG = conf.get_mysql_conn('./conf/key')

# {
#     # 'host':'127.0.0.1',
#     'host': '101.43.61.66',
#     'port': 3306,
#     'user': 'root',
#     'password': 'weston987',
#     'database': 'cls_sys',
#     'charset': 'utf8',
# }
