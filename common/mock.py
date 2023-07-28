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
    def faker_num():

        faker = Faker()

        st = faker.random_number(digits=5)

        return st


if __name__ == '__main__':

    mock = Mock()

    a2 = mock.faker_data_61()

    print(a2)

