
import os
import subprocess

# 获取testcase目录的绝对路径
base_dir = os.path.dirname(os.path.abspath(__file__))
testcase_dir = os.path.join(base_dir, 'test_case')
print(testcase_dir)

# 按照以下文件顺序执行
test_files = [os.path.join(testcase_dir, 'basic_information_case', 'test_currency_case.py'),
              os.path.join(testcase_dir, 'basic_information_case', 'test_reason_case.py'),
              os.path.join(testcase_dir, 'basic_information_case', 'test_tax_rate_case.py'),
              os.path.join(testcase_dir, 'material_case', 'test_material_category_case.py'),
              os.path.join(testcase_dir, 'material_case', 'test_material_signal_case.py'),
              os.path.join(testcase_dir, 'material_case', 'test_material_unit_case.py'),
              os.path.join(testcase_dir, 'material_case', 'test_material_case.py'),
              os.path.join(testcase_dir, 'business_partner_case', 'test_partner_case.py'),
              os.path.join(testcase_dir, 'material_case', 'test_material_unit_conversion_case.py')
              ]

# 使用subprocess模块执行命令行命令， alluredir 后面是存放报告的目录文件
for test_file in test_files:
    subprocess.run(['pytest', test_file, '--alluredir', 'test_reports'])

# 生成allure报告， 指定了’test_reports’目录作为结果文件目录，‘-o’参数指定了生成报告保存的目录为’allure-report’，
# '–clean’参数表示在生成报告前先清空之前的报告
subprocess.run(['allure', 'generate', 'test_reports', '-o', 'allure-report', '--clean'])

""" 命令行执行 ，运行 pytest --alluredir=test_reports
查看报告执行，allure serve test_reports

"""