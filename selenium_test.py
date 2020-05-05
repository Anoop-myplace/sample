'''
A sample website is taken to perform scapping operation inorder not to disturb other web sites
there are some flaws in the this website with the products details which can be observed in the
results lately.
'''

from selenium import webdriver
from tqdm import tqdm
import pandas as pd

driver = webdriver.Chrome(executable_path='C:\Driver\chromedriver_win32\chromedriver.exe')
driver.get("https://webscraper.io/test-sites/e-commerce/static")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='side-menu']/li[2]/a").click()
driver.find_element_by_xpath("//*[@id='side-menu']/li[2]/ul/li[1]/a").click()

listoflinks = []
condition = True

while condition:
    products = driver.find_elements_by_class_name("thumbnail")
    for ele in products:
        pp2 = ele.find_element_by_tag_name('a')
        listoflinks.append(pp2.get_attribute('href'))
        
        try:
            p = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/ul/li[14]")
            p1=p.get_attribute('aria-disabled')
            if (p1 == "true"):
                print("All products has been feetched and then terminated the loop")
                condition = False
        except:
            pass
        
    driver.find_elements_by_class_name("page-link")[-1].click()
        
print(len(listoflinks))

all_products = []
for i in tqdm(listoflinks):
    driver.get(i)
    name = driver.find_elements_by_tag_name("h4")[-1].text
    price = driver.find_elements_by_tag_name("h4")[0].text
    reviews = driver.find_element_by_class_name("ratings").text
    description = driver.find_element_by_class_name("description").text

    tempj = {'Name_of_Product':name,
             'Price':price,
             'Reviews':reviews,
             'Description':description,
             'Link_to_the_Product':i,
             }
    all_products.append(tempj)

finish = pd.DataFrame(all_products)
finish.to_csv("Products_scrapped.csv")

driver.quit()
