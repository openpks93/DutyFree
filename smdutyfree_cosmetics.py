from selenium import webdriver
url = r"http://www.smdutyfree.com/fdp001.do?goTo=gList&ct_cd1=100000&ct_cd2=&ct_cd3=#1"
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
brand = chrome_driver.find_elements_by_css_selector("div.goods_item_title > div.vertical_inner > p.vertical_outter")
name = chrome_driver.find_elements_by_css_selector("div.goods_item_contents > div.vertical_inner > div.vertical_outter > p")
price = chrome_driver.find_elements_by_css_selector("div.goods_item_price > div.vertical_inner > div.vertical_outter > p")
won = chrome_driver.find_elements_by_css_selector("div.goods_item_price > div.vertical_inner > div.vertical_outter > span")
# Json
import json
from collections import OrderedDict
LENGTH = min(len(brand), len(name), len(price), len(won))
products = OrderedDict()
print("processing data to json")
for idx in range(0, LENGTH):
    products['no_' + str(idx + 1)] = {
        'brand': brand[idx].text,
        'name': name[idx].text,
        'price': price[idx].text,
        'won': won[idx].text
    }
# json 저장
with open('smdutyfree_cosmetics.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent="\t")

# 브라우저 종료, 웹 드라이버 종료
print("This job is finished and close the web browser")
chrome_driver.quit()

