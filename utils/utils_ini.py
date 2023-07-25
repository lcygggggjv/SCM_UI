
import configparser
import os.path

"""os.path.dirname获取当前文件父级目录，__file__当前文件路径。 abspath把路径转换绝对路径，获取当前父级目录绝对路径"""
base_dir = os.path.dirname(os.path.abspath(__name__))

'''拼接ini文件路径'''
utils_dir = os.path.join(base_dir, 'utils_ini')
