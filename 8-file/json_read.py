"""

{'keywords': ['key1', 'key2'], 'categories': ['woman', 'man']}
"""

import json
import os
import re
import time
import pandas as pd



def get_time_from_file_name(file_name):
    l = re.split(r'_', file_name)
    t = l[0]
    time_local = time.localtime(int(t))
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt

def get_json_from_csv(csv_file):
    df = pd.read_csv(u'uevent.csv')
    js001 = df.to_json()
    return js001

def get_urls_from_json(json_path):
    json_name = '1462451334_sam_keywords.json'
    dt = get_time_from_file_name(json_name)

    with open('1462451334_sam_keywords.json') as json_file:
        data = json.load(json_file)
        json_dict = data
        amazon_url = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3D"

        keywords = json_dict['keywords']
        categories = json_dict['categories']
        urls = []

        for category in categories:
            for keyword in keywords:
                url = amazon_url + category + '&field-keywords=' + keyword
                urls.append(url)

        print(urls)

if __name__ == '__main__':
    get_json_from_csv(u'stocks.csv')
