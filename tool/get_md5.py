import hashlib


def create_token(password):
    """ 根据password生成token """

    # 生成MD5对象
    md5 = hashlib.md5()
    # 对数据加密
    md5.update(password.encode('utf-8'))
    # 获取密文
    data = md5.hexdigest()
    return data


if __name__ == '__main__':
    print(create_token('123'))
