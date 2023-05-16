from git import Repo
import os

url_template = "http://vip.stock.finance.sina.com.cn/q//view/vGold_Matter_History.php?page={}&pp=0&pz={}&start={}&end={}"
                # http://vip.stock.finance.sina.com.cn/q//view/vGold_Matter_History.php?page=2&pp=0&pz=11&start=2023-04-25&end=2023-05-15
                # http://vip.stock.finance.sina.com.cn/q//view/vGold_Matter_History.php?page=1&pp=0&pz=11&start=2023-04-25&end=2023-05-15

def url_generate(no="11", date_start="2023-05-08", date_end="2023-05-08", page="1", url=url_template):

    url = url.format(page, no, date_start, date_end)
    # print(url)

    return url


def down_load(url):

    pass


def git_push(dirfile=""):

    # dirfile = os.path.abspath('') # code的文件位置，我默认将其存放在根目录下
    repo = Repo(dirfile)

    g = repo.git
    g.add("--all")
    g.commit("-m auto update")
    g.push()
    # print("Successful push!")


