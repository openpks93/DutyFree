from selenium import webdriver
url = r"http://www.galleria-dfs.com/dispctg/initDispCtg.idf?depth_no=1&disp_ctg_no=1501000000&shop_type_cd=10"
print("set url : " + url)
# Chrome Headless 전용 옵션, Firefox 사용시 모두 주석
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# Chrome 드라이버 생성(둘 중 하나만 켤것)
chrome_driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
chrome_driver.implicitly_wait(3)
print("webdriver's ready")
# 크롤링할 사이트 호출
print("getting url site")
chrome_driver.get(url)
print("parsing data")
#context = driver.find_elements_by_class_name("facet-product-list")
brand = chrome_driver.find_elements_by_css_selector("div.ctg_goods > ul.ctg_gd > li > a > dl.info > dt > em")
name = chrome_driver.find_elements_by_css_selector("div.ctg_goods > ul.ctg_gd > li > a > dl.info > dt > strong")
dr = chrome_driver.find_elements_by_css_selector("div.ctg_goods > ul.ctg_gd > li > a > dl.info > dd.prc > span.dr")
won = chrome_driver.find_elements_by_css_selector("div.ctg_goods > ul.ctg_gd > li > a > dl.info > dd.prc > span.on")

# Json
import json
from collections import OrderedDict
LENGTH = min(len(brand), len(name), len(dr), len(won))
products = OrderedDict()
print("processing data to json")
for idx in range(0, LENGTH):
    products['no_' + str(idx + 1)] = {
        'brand': brand[idx].text,
        'name': name[idx].text,
        'dr': dr[idx].text,
        'won': won[idx].text
    }

# json 저장
with open('galleria_cosmetics.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent="\t")


# xlsx 형식으로 만들기
import pandas
pandas.read_json('galleria_cosmetics.json', encoding='UTF8', orient='index').to_excel('galleria_cosmetics.xlsx', encoding='UTF8')
pandas.read_json('galleria_cosmetics.json', encoding='UTF8').to_csv('galleria_cosmetics.csv', encoding='UTF8')

# # xlsx 행열 변환
# import csv
# import itertools
#
# with open('galleria_cosmetics.csv', 'r', encoding='UTF8') as f:
#     reader = csv.reader(f)
#     keys, vals = set(), []
#     for key, group in itertools.groupby(reader, lambda i:i[0]):
#         keys.add(key)
#         vals.append(list(map(lambda i:i[1], group)))
#
#     print('\t'.join(keys))
#     for name, val in zip(vals[0], vals[1]):print('{}\t{}'.format(name, val))


# 브라우저 종료, 웹 드라이버 종료
print("This job is finished and close the web browser")
chrome_driver.quit()
