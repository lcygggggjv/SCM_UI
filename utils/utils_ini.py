
import configparser
import os.path

"""os.path.dirname获取当前文件父级目录，__file__当前文件路径。 abspath把路径转换绝对路径，获取当前父级目录绝对路径"""
base_dir = os.path.dirname(os.path.abspath(__file__))

# rot_path = os.path.abspath(os.path.join(os.getcwd(), '..'))

# con_path = os.path.join(rot_path, 'utils/utils.ini')
# print(con_path)

'''拼接ini文件路径'''
utils_dir = os.path.join(base_dir, 'utils.ini')
# print(utils_dir)

config_parser = configparser.ConfigParser()  # 获取configparser对象
config_parser.read(utils_dir, encoding='utf-8')  # 要先读取ini文件

pick = config_parser.get("pick", "env")  # 获取配置项pick， env是键， 传给pick变量

env = config_parser.get(pick, "env")
account = config_parser.get(pick, "account")
password = config_parser.get(pick, "password")
tenantcode = config_parser.get(pick, "tenantcode")


class EnvironMent:
    """ env,account等全局变量。类里直接调用"""

    @staticmethod
    def get_env_url():

        return "https://" + env + ".tele" + "tr" + "aan.io"

    @staticmethod
    def account():

        return account

    @staticmethod
    def password():

        return password

    @staticmethod
    def tenantcode():

        return tenantcode


if __name__ == '__main__':

    c = EnvironMent()

    ss = c.get_env_url()

    d = c.account()
    print(ss)
