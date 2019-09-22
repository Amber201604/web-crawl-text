import requests
import re
from bs4 import BeautifulSoup
import json
import time
import unicodedata

def get_web(currenturl):
    try:
        res = requests.get(currenturl)
        res.raise_for_status()
        return res.content
    except requests.RequestException as e:
        print(e)
        return


def get_para(output, currenturl, num, dom, domain, website, text_start, text_end):
    article = []
    time.sleep(1)
    text = get_web(currenturl)
    soup = BeautifulSoup(text, 'html.parser')
    para_list = soup.find_all('p')[text_start:text_end] # all paragraphs
    # full text
    for i in range(len(para_list)):
        p1 = re.sub('<[^<]+?>', '', str(para_list[i]))
        p2 = re.sub(' +\t*\n*', ' ', p1)
        p3 = re.sub('\t*\n*', '', p2)
        p4 = re.sub("\u2019", "'", p3)
        p5 = re.sub('\u2014', '-', p4)
        p6 = re.sub('\u201c', '"', p5)
        p7 = re.sub('\u201d', '"', p6)
        p8 = re.sub('\u2026', '...', p7)
        p9 = re.sub("\u2018", "'", p8)
        p10 = re.sub("\u2022", "•", p9)
        p11 = re.sub("\u00a0", ' ', p10)
        p12 = re.sub("\u2009", '', p11)
        p13 = re.sub("\u20ac", '€', p12)
        p14 = re.sub("\u00a3", '£', p13)
        p15 = re.sub("\u00a2", '¢', p14)
        p16 = re.sub("\u2009", '', p15)  # new -- xy
        p17 = re.sub("\xa0", '', p16)  # new -- xy
        p18 = re.sub("\2010", '-', p17)  # new -- xy
        para1 = unicodedata.normalize("NFKD", p18)
        para2 = ' '.join(para1.split())
        article.append(para2)

    f = open(output, "a", encoding='utf-8')
    dct = {}
    dct['article ID'] = dom + str(num).zfill(6)
    dct['url'] = currenturl
    dct["domain"] = domain
    dct["website"] = website
    dct['full text'] = article
    # write the dictionary
    f.writelines(json.dumps(dct))
    # time.sleep(1)
    f.writelines('\n')
    f.close()

    return


def main():
    input = "url-md.txt"
    output = "amd_articles.txt"
    dom = 'H'
    domain = 'Health'
    website = "medical daily"
    num = 1  # starting ID
    text_start, text_end = 0, -1

    # no duplicate url(articles)
    q = []
    with open(input) as f:
        for line in f:
            currenturl = line.strip('\n')
            if currenturl not in q:
                q.append(currenturl)
                get_para(output, currenturl, num, dom, domain, website, text_start, text_end)
                print('finished URL' + str(num))
                num += 1
    return


main()
