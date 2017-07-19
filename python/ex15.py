'''urllib test'''
import urllib.request
import json

urlresult = urllib.request.urlopen("http://www.sina.com.cn/")
html = urlresult.read().decode("UTF-8")
translateResult = json.loads(html)
print(translateResult)
