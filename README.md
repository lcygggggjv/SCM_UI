# SCM_UI

### 如何使用：

### 1.安装依赖库

pip install install -r requirements.txt

### 2.运行测试用例

命令行输入； pytest --alluredir=test_reports

### 3.查看报告

命令行输入；allure serve test_reports

# 项目介绍：

本项目为某工业互联网SaaS平台中SCM项目（基础数据中心）的UI自动化测试项目。采用Python + pytest + Selenium 技术栈完成。

### 设计模式

采用PO设计模式。

### 实现细节:

1.page_manger包内含封装的一些页面方法，关于元素定位基本采用Xpath定位方式，并灵活运用Xpath轴定位及显式等待方式令脚本整体稳定性得到较大提升。

2.basepage.py文件内含一些页面跳转，及显性等待，双击删除，判断元素存在和获取alert信息等公共方法。

3.utils包内含一些工具类：读取环境，账号，密码等数据。common包含所需mock数据。

4.test_case包内含测试用例方法，其中灵活使用parametrize/fixture等装饰器实现用例参数化、前后置操作及其他具体需求。
