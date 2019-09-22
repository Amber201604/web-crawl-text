from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def click_newPage(website, prefix, doc0, inlst, urlfile, totalpage, divider):
    chrome_option = Options()
    chrome_option.add_argument("--headless")
    browser = webdriver.Chrome("/Users/Amber/Desktop/research/New_spider/chromedriver", chrome_options = chrome_option)
    url = website
    url1 = prefix
    browser.get(url)
    SCROLL_PAUSE_TIME = 2
    i = 1
    print("start printing")
    while (i < totalpage):
        # Scroll down to bottom
        browser.execute_script("window.scrollBy(0, 10000);")
        browser.execute_script("window.scrollBy(0, -300);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        print("scroll ", i)
        if(i % divider == 0):
            print("writing", i)
            html = browser.page_source
            doc = pq(html)
            get_url = doc(doc0).items()
            f = open(urlfile, "w")
            for j in get_url:
                #j = j.remove_namespaces()
                print(j)
                child_url = url1 + j.find(inlst).attr('href')
                f.write(child_url+'\n')
            f.close()
        i += 1



click_newPage("https://www.yahoo.com/lifestyle/tagged/health", "https://www.yahoo.com", '#YDC-Stream ul li div div div h3', 'a', "yahoo-url.txt", 200, 2)


