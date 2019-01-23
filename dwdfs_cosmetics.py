from selenium import webdriver
url = r"http://www.dwdfs.com/category/main/midCategory.dw?PARENTCATID=10011"
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
img = chrome_driver.find_elements_by_css_selector("div.sub-list1 > ul.product-list > li > div.product-item > div.product-item__wrap > div.product-item__img > img")
brand = chrome_driver.find_elements_by_css_selector("div.sub-list1 > ul.product-list > li > div.product-item > div.product-item__wrap > div.product-item__brand1")
name = chrome_driver.find_elements_by_css_selector("div.sub-list1 > ul.product-list > li > div.product-item > div.product-item__wrap > div.product-item__tit1")
dollar = chrome_driver.find_elements_by_css_selector("div.sub-list1 > ul.product-list > li > div.product-item > div.product-item__wrap > div.product-item__price1 > span.price-dollar")
won = chrome_driver.find_elements_by_css_selector("div.sub-list1 > ul.product-list > li > div.product-item > div.product-item__wrap > div.product-item__price1 > span.price-won")

# Json
import json
from collections import OrderedDict
LENGTH = min(len(img), len(brand), len(name), len(dollar), len(won))
products = OrderedDict()
print("processing data to json")
for idx in range(0, LENGTH):
    products['no_' + str(idx + 1)] = {
        'img': img[idx].get_attribute("data-original"),
        'brand': brand[idx].text,
        'name': name[idx].text,
        'price': {
            'sale': dollar[idx].text,
            'won': won[idx].text
        }
    }
# json 저장
with open('dwdfs_cosmetics.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent="\t")
# 브라우저 종료, 웹 드라이버 종료
print("This job is finished and close the web browser")
chrome_driver.quit()