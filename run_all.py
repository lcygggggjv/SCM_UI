import pytest
import os


if __name__ == '__main__':

    # 指定模块, -vs 输出调试信息，包括打印详细信息， --alluredir 输出json文件报告  后面输出目录
    pytest.main(['-vs', '--alluredir', './test_reports'])
    # 产生报告，将报告保存，./test_reports获取这个目录中的json文件进行渲染，-o test_reports  生成的html文件，保存到这个目录中 clean清除
    os.system('allure generate ./test_reports  -0  ./test_reports --clean ')
