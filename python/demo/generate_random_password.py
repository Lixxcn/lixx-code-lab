import random
import string


def generate_random_password(length=8):
    # 定义字符集
    characters = string.ascii_letters + string.digits + string.punctuation

    # 随机选择字符
    password = "".join(random.choice(characters) for _ in range(length))
    return password


# 生成一个随机密码
random_password = generate_random_password()
print(f"生成的随机密码是: {random_password}")
