from selenium import webdriver
url = r"https://www.jdcdutyfree.com/category.htm?c1=53#c1=53&hashChange=true&orderType=best"
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
img = chrome_driver.find_elements_by_css_selector("div.product_list > ul> li.product_box > div.thumbnail > img")
brand = chrome_driver.find_elements_by_css_selector("div.product_list > ul > li.product_box > div.product_info > p.brand")
name = chrome_driver.find_elements_by_css_selector("div.product_list > ul > li.product_box > div.product_info > p.productname")
price_origin = chrome_driver.find_elements_by_css_selector("div.product_list > ul > li.product_box > div.product_info > p.price > span.discount_price")
price_final = chrome_driver.find_elements_by_css_selector("div.product_list > ul > li.product_box > div.product_info > p.price > span.product_price")
# Json
import json
from collections import OrderedDict
LENGTH = min(len(img), len(brand), len(name), len(price_origin), len(price_final))
products = OrderedDict()
print("processing data to json")
for idx in range(0, LENGTH):
    products['no_' + str(idx + 1)] = {
        'img': img[idx].get_attribute("data-original"),
        'brand': brand[idx].text,
        'name': name[idx].text,
        'price': {
            'sale': price_origin[idx].text,
            'won': price_final[idx].text
        }
    }
# json 저장
with open('jdcdutyfree_cosmetics.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent="\t")
# 브라우저 종료, 웹 드라이버 종료
print("This job is finished and close the web browser")
chrome_driver.quit()