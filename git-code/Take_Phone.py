#将列表中的手机名称，在指定网站查询后，将“分辨率”信息爬下来存放在对应的手机名称后；
import re
import os
import urllib.request
import urllib
#根据给定的网址来获取网页详细信息，得到的html就是网页的源代码
def getHtml(url):
    headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('gbk')#这里通过查看网页源码的编码格式charset格式为GBK，将源码重新进行解码操作

# '(?=.*\d)(?=.*[a-zA-Z])(?<=主屏分辨率：)\d\w+'
def getphoneFB(html):
    regStr = '主屏分辨率：\\s*(.*?)像素'
    patter = re.compile(regStr)
    phonere = re.findall(patter,html)
    return phonere
#打开机型文件，放到列表中
file_path = 'D:\pythonCode\phone.txt'
phone_msg_list = {}
with open(file_path) as file_object:
    file = file_object.read().splitlines()
    x = 0
    while x < len(file):
        file[x] = "http://search.zol.com.cn/s/all.php?kword=" + file[x]
        try:
            phone_FB = getphoneFB(getHtml(file[x]))
            phone_msg_list[file[x]] = phone_FB
        except Exception:
            pass
        continue
        x += 1
print(phone_msg_list)

#
# #将所有地址组合好后，放到地址列表内等待查询使用
# for line in file:
#     uurl = "http://search.zol.com.cn/s/all.php?kword="+ line  #组合出所有机型的查询地址
#     try:
#         phone_FB = getphoneFB(getHtml(uurl))
#         phone_msg_list.append(phone_FB)
#     except Exception:
#         pass
#     continue
#
# print(phone_msg_list)

#使用列表中的地址，依次打开后将指定网页信息爬去下来，并与机型对应成字典
