from selenium import webdriver
url = r"http://www.dootadutyfree.com/dutyfree/goods/list/2/100/200100020002//view.do?ctg_no=200100020002&mode=&type=&brndNo=&ctgNo=&lppp=&showDivId=&goodSearchArea=Y&priceChange=N&selPrice=notSearch&tMinPrice=4&tMaxPrice=1079&brandFlag=KOR&ctgNoSearch2=2001000200020001&ctgNoSearch2=2001000200020002&fromVal=4&toVal=1079&lppSearch=20&lppSearch=20"
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
img = chrome_driver.find_elements_by_css_selector("li.cat_item > a > img")
brand = chrome_driver.find_elements_by_css_selector("li.cat_item > strong.brand")
title = chrome_driver.find_elements_by_css_selector("li.cat_item > p.title")
price = chrome_driver.find_elements_by_css_selector("li.cat_item > strong.price")
discount = chrome_driver.find_elements_by_css_selector("li.cat_item > span.won")
# Json
import json
from collections import OrderedDict
LENGTH = min(len(img), len(brand), len(title), len(price), len(discount))
products = OrderedDict()
print("processing data to json")
for idx in range(0, LENGTH):
    products['no_' + str(idx + 1)] = {
        'img': img[idx].get_attribute("data-original"),
        'brand': brand[idx].text,
        'title': title[idx].text,
        'price': price[idx].text,
        'discount': discount[idx].text
    }
# json 저장
with open('dootadutyfree_tagheuer.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent="\t")
# 브라우저 종료, 웹 드라이버 종료
print("This job is finished and close the web browser")
chrome_driver.quit()

##우오아ㅗ아ㅗ아ㅗㅇ