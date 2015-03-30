#coding:utf-8
__author__ = 'Li'

import urllib2
import re

#search in today.hit.edu.cn
def use_urllib2(item):
    url = 'http://www.baidu.com/s?wd={0}%20site%3Atoday.hit.edu.cn&rsv_spt=1&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=0&rsv_pq=e788fcff0000594c&rsv_t=f068Z6%2Frj3lCclXENntCfEAwJsde24MFQ%2BfPDv7xonJWY%2FD4dQKPB4d9aaT3gZBi2fR1&inputT=11732'
    search_url = url.format(item)
    print search_url
    try:
        f = urllib2.urlopen(search_url,timeout=50).read()
    except urllib2.URLError, e:
        print e.reason
    print len(f)
    print f
    file = open('search.html','w')
    file.write(f)
    file.close()

def translate(item):
    url ='http://fanyi.baidu.com/translate?query={0}&keyfrom=baidu&smartresult=dict&lang=auto2zh#en/zh/{1}'.format(item,item)
    print url
    search_url = url.format(item)
    print search_url
    try:
        f = urllib2.urlopen('http://fanyi.baidu.com/#en/zh/hello',timeout=5).read()
    except urllib2.URLError, e:
        print e.reason
    print len(f)
    print f
    file = open('translate.html','w')
    file.write(f)
    file.close()
if __name__ == '__main__':
    item = '假期'
    # use_urllib2(item)
    item2 = 'hello'
    translate(item2)