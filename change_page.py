from bs4 import BeautifulSoup
import time
import requests


def get_web(currenturl):
    try:
        res = requests.get(currenturl)
        res.raise_for_status()
        return res.content
    except requests.RequestException as e:
        print(e)
        return ''


def remove_punctuation(sentence):
    return sentence.replace('“', '').replace('’', "").replace('”', '').replace('—', '-').strip()


def newPage(start_page, end_page):
    url = "https://www.nhs.uk"
    url1 = "https://www.nhs.uk/news/?page="
    for i in range(start_page, end_page):
        url2 = url1 + str(i)
        text = get_web(url2)
        time.sleep(1)
        soup = BeautifulSoup(text, 'html.parser')
        para_list = soup.select("li a")
        ff = open("nhs_url.txt", "a")
        for j in para_list:
            para = j.get('href')
            child_url = url + para
            ff.write(child_url + "\n")
            #print(child_url)
        ff.close()
        print(i)


def main():
    start_page, end_page = 1, 200
    newPage(start_page, end_page)


main()
