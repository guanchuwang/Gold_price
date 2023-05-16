from git import Repo
import os
import numpy as np
import datetime
import requests
import re
# from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from utils import url_generate, url_template








ISOTIMEFORMAT = '%Y-%m-%d' # %H:%M:%S,f'

theTime_str = datetime.datetime.now().strftime(ISOTIMEFORMAT)
print(theTime_str)

theTime_date = datetime.datetime.strptime(theTime_str, ISOTIMEFORMAT)

delta = datetime.timedelta(days=20)
lastTime_date = theTime_date - delta
lastTime_str = lastTime_date.strftime('%Y-%m-%d')
print(lastTime_str)

gold_no = "11"

web_url_pp0 = url_generate(gold_no, date_start=lastTime_str, date_end=theTime_str, page="1", url=url_template)
response = requests.get(web_url_pp0)
regex = re.compile('共(.*)页&nbsp')
# regex = re.compile('共.*?页&nbsp')
pages = regex.findall(response.text)[0]

print(pages)

date_buf = []
brand_buf = []
price_buf = []

for page_idx in range(int(pages)+1):
    page_str = str(page_idx)
    web_url = url_generate(gold_no, date_start=lastTime_str, date_end=theTime_str, page=page_str, url=url_template)

    print(web_url)

    tables = pd.read_html(web_url)
    table = tables[0]
    # print(table)

    for key in table.keys():
#     print(list(table[key]))
        if "日期" in list(table[key]):
            # print(list(table[key]))
            date_buf.extend(list(table[key][1:]))

        if "品牌" in list(table[key]):
            # print(list(table[key]))
            brand_buf.extend(list(table[key][1:]))

        if "价格" in list(table[key]):
            # print(list(table[key]))
            price_buf.extend(list(table[key][1:]))

print(date_buf)
print(brand_buf)
print(price_buf)

print(np.unique(brand_buf))
print(len(price_buf))




date_buf_sorted = sorted(date_buf)
print(date_buf_sorted)


price_date_buf = {}
for idx, brand in enumerate(brand_buf):
    if brand not in price_date_buf.keys():
        price_date_buf[brand] = {"date_str": [], "price": [], "date_int": []}
    else:
        price_date_buf[brand]["date_str"].append(date_buf[idx])
        price_date_buf[brand]["price"].append(float(price_buf[idx]))


def interval_estimation(date1, date2):

    theTime_date1 = datetime.datetime.strptime(date1, ISOTIMEFORMAT)
    theTime_date2 = datetime.datetime.strptime(date2, ISOTIMEFORMAT)
    interval = (theTime_date2 - theTime_date1).days

    return interval


date_start_str = date_buf[-1]
for brand in brand_buf:

    date_brand_str = price_date_buf[brand]["date_str"]
    date_brand_int = []
    for date_str in date_brand_str:
        date_brand_int.append(interval_estimation(date_start_str, date_str))

    price_date_buf[brand]["date_int"] = date_brand_int


for brand in brand_buf:
    plt.plot(price_date_buf[brand]["date_int"], price_date_buf[brand]["price"], label=brand)
    plt.xticks(price_date_buf[brand]["date_int"], price_date_buf[brand]["date_str"], fontsize=15)

plt.xlabel("Date", fontsize=15)
plt.ylabel("Price", fontsize=15)

plt.savefig("figures/price_vs_time.png")
plt.close()


#
# # print(tables)
#
# keywords = ["品牌", "价格", "日期"]
# table = tables[0]
# for key in table.keys():
#     print(list(table[key]))
#     print("品牌" in list(table[key]))




#
#
# response = requests.get(web_url)
# print(response.text)
# soup = BeautifulSoup(response.text, 'html.parser')
# table = soup.find('table', {'id': 'datalist'})
# rows = table.findAll('tr')
#
# for row in rows[1:]:
#     cols = row.findAll('td')
#     date = cols[0].text.strip()
#     price = cols[1].text.strip()
#     print(f'{date}: {price}')




