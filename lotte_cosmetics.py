from selenium import webdriver
url = r"http://kor.lottedfs.com/kr/display/category/first?dispShopNo1=1100050&treDpth=1"
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
img = chrome_driver.find_elements_by_css_selector("ul.listUl > li.productMd > a > div.img > img")
brand = chrome_driver.find_elements_by_css_selector("div.info > div.brand")
propro = chrome_driver.find_elements_by_css_selector("div.info > div.product")
price = chrome_driver.find_elements_by_css_selector("div.discount > strong")
discount = chrome_driver.find_elements_by_css_selector("div.discount > span")
# Json
import json
from collections import OrderedDict
LENGTH = min(len(img), len(brand), len(propro), len(price), len(discount))
products = OrderedDict()
print("processing data to json")
for idx in range(0, LENGTH):
    products['no_' + str(idx + 1)] = {
        'brand': brand[idx].text,
        'propro': propro[idx].text,
        'price': price[idx].text,
        'discount': discount[idx].text
    }
# json 저장
with open('lotte_cosmetics.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent="\t")
# 브라우저 종료, 웹 드라이버 종료
print("This job is finished and close the web browser")

import pandas

# xlsx 형식으로 만들기
pandas.read_json('lotte_cosmetics.json',  encoding='UTF8').to_excel('lotte_cosmetics.xlsx', encoding='UTF8')
chrome_driver.quit()