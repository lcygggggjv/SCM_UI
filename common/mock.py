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
    def faker_data():

        faker = Faker()

        strs = faker.word()

        return strs


if __name__ == '__main__':

    mock = Mock()

    a2 = mock.faker_data()

    print(a2)

