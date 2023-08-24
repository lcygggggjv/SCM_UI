
from webdriver_manager.chrome import ChromeDriverManager


class A:

    def __init__(self, url='111'):

        self.url = url

    def get_datas(self):

        return "父类"


class B(A):

    def __init__(self):

        super().__init__()
        self.url = '2222'

    def get_datas(self):

        return super().get_datas()


# s = B()
# d = s.url
# print(d)


class NewDownLoadUrl(ChromeDriverManager):

    def __init__(self):

        super().__init__()

        # self.latest_release_url = 'https://googlechromelabs.github.io/chrome-for-testing/'
        self.latest_release_url = 'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/win64/' \
                                  'chromedriver-win64.zip'


a = NewDownLoadUrl()
w = a.latest_release_url
print(w)
