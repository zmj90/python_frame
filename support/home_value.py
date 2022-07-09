"""

"""


class PV:
    URL_HOME = "https://www.douban.com/"

    # FRAME_NODE = '//div[@class="login"]/iframe'  # xpath
    FRAME_NODE = '.login>iframe'  # css

    # PW_LOGIN_NODE = '//li[text()="密码登录"]'  # xpath
    PW_LOGIN_NODE = '.account-tab-account'  # css
