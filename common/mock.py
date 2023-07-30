import random
import string

from faker import Faker


class Mock:

    @staticmethod
    def mock_data(strs='tc'):

        strings = string.digits + string.ascii_letters

        random_str = ''.join(random.sample(strings, 4))

        return random_str + strs

    @staticmethod
    def faker_data_61():

        faker = Faker()

        strs = faker.pystr(max_chars=61)

        return strs

    @staticmethod
    def faker_pystr():
        # max_chars最大位数，min_chars最小，numerify=True表示生成的字符串只包含数字字符。
        faker = Faker()

        strs = faker.pystr(max_chars=5)

        return strs

    @staticmethod
    def faker_pystr_21():

        faker = Faker()
        strs = faker.pystr(max_chars=21)

        return strs

    @staticmethod
    def faker_pystr_15():

        faker = Faker()
        strs = faker.pystr(max_chars=15)

        return strs

    @staticmethod
    def faker_num_18():

        faker = Faker()

        st = faker.pystr(max_chars=18)

        return st

    @classmethod
    def random_int(cls):
        """随机0-99整数"""
        return random.randint(0, 99)

    @classmethod
    def rand_phone_num(cls):
        # 以156开头
        prefix = '156'
        # 生成后8位随机数字 下划线 _ 是一个常用的习惯用法，在循环中表示一个临时变量，通常用于表示我们在循环中不需要使用到的值。
        suffix = ''.join(random.choice('0123456789') for _ in range(8))
        # 拼接前缀和后缀
        return prefix + suffix

    @classmethod
    def ran_phone2(cls):
        # 以77开头
        phone = '77'
        # 列表推导式，下划线 _ 是一个常用的习惯用法，在循环中表示一个临时变量，通常用于表示我们在循环中不需要使用到的值。
        str2 = ''.join(random.choice('0123456789') for _ in range(6))

        return phone + str2


if __name__ == '__main__':

    mock = Mock()

    a2 = mock.ran_phone2()

    print(a2)

