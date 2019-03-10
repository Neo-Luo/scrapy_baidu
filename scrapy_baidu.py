# -*- coding:utf-8 -*-
import os
import requests
import time
import csv
import re
from bs4 import BeautifulSoup
import urllib2
from jparser import PageModel
import url2io

# 设置默认encoding方式
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

PAGE_NUM = 2
token = 'CHgsuVPJQcO56K0ZGpT8Qw'
api = url2io.API(token)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
}

SAVE_DIR = 'scrapy_data' #抓取数据存储路径
if not (os.path.isdir(SAVE_DIR)):
    os.makedirs(SAVE_DIR)
    
def main():
    reader = csv.reader(open( 'query_text.csv', 'rb'))
    index = 0
    for line in reader:
        record_id = 1
        print('---------%i---------' % index)
        query_all = line[0]
        csvfile = open( SAVE_DIR +'/scrapy_result_%i.csv' % (index), 'wb')
        writer = csv.writer(csvfile)
        data = ['record_id','query','title','abstract','link','content']
        writer.writerows([data])
        index += 1
 
        query_array = re.split(u"[，；。！？]", query_all.decode('utf-8'))
        if(len(query_array[-1])<5):
            query_array.pop(-1)
        flag = len(query_array)-1
        i = -1
        while (i<flag):
            i += 1
            if(i>flag-1):
                break
            elif(len(query_array[i])<38):
                if(len(query_array[i])+len(query_array[i+1])>38):
                    continue
                else:
                    query_array[i+1] = query_array[i] + query_array[i+1]
                    query_array.pop(i)
                    flag -= 1
                    i -= 1
            else:
                continue

        if(len(query_array)):
            for query in query_array:
                print(query)
                if(len(query)<8):
                    PAGE_NUM = 1
                else:
                    PAGE_NUM = 1
                
                for k in range(0, PAGE_NUM):
                    try:
                        #待抓取的网页地址
                        url = 'http://www.baidu.com/s?wd=%s&pn=%i' % (query,k*10)
                        content = requests.get(url,headers=headers)
                        #使用BeautifulSoup解析html
                        soup = BeautifulSoup(content.text,'html.parser')
                        title = []
                        abstract = []
                        link = []
                        content = []
                        allNews = soup.find_all('div', { 'id', 'result c-container '})
                        for hotNews in allNews:
                            h3 = hotNews.find(name = "h3", attrs = { "class": re.compile( "t")}).find('a')
                            title.append(h3.text.replace("\"",""))
                            div = hotNews.find(name = "div", attrs = { "class": re.compile( "c-abstract")})
                            abstract.append(div.text.replace("\"",""))
                            a = hotNews.find(name = "a", attrs = { "class": re.compile( "c-showurl")})
                            detail_url = a.get('href')
                            link.append(detail_url)
                            try:
                                ret = api.article(url=detail_url, fields=['text', 'next'])
                                content.append(ret['text'].replace('\r','').replace('\n',''))
                            except:
                                try:
                                    time.sleep(1)
                                    ret = api.article(url=detail_url, fields=['text'])
                                    content.append(ret['text'].replace('\r','').replace('\n',''))
                                except:
                                    try:
                                        try:
                                            html = requests.get(detail_url,headers=headers).text.decode('utf-8')
                                        except:
                                            html = requests.get(detail_url,headers=headers).text.decode('gbk')
                                        pm = PageModel(html)
                                        result = pm.extract()
                                        ans = [ x['data'] for x in result['content'] if x['type'] == 'text']
                                        content.append(''.join(ans))
                                    except Exception as e:
                                        print(e)
                                        print(detail_url)
                                        content.append('')
                                        pass

                            #将数据写入csv
                        data = []                        
                        for i in range( 0, len(title)):
                            try:
                                data.append((record_id,query,title[i],abstract[i],link[i],content[i]))
                                record_id += 1
                            except Exception as err:
                                print(err)
                        writer.writerows(data)
                        print("Page: " + str(k+1) + " finished!")

                    except Exception as err:
                        print(err)
                        pass

                time.sleep(1)
                # break
            
        csvfile.close()


if __name__ == '__main__':

    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    print('starting...')

    main()

    print('finished')
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
