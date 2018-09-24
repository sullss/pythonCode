Index: git-share/python.py
===================================================================
--- git-share/python.py	(revision c8c75999d798943218ec74f807bbd3aa54dfe04d)
+++ git-share/python.py	(revision c8c75999d798943218ec74f807bbd3aa54dfe04d)
@@ -0,0 +1,34 @@
+import urllib.request
+import re
+import os
+import urllib
+#根据给定的网址来获取网页详细信息，得到的html就是网页的源代码
+def getHtml(url):
+    #增加了伪装成浏览器的设置
+    #设置一个请求头
+    headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")
+    #创建一个opener
+    opener = urllib.request.build_opener() #将创建的headers加到opener中
+    opener.addheaders= [headers]
+    urllib.request.install_opener(opener)
+    page = urllib.request.urlopen(url)
+    html = page.read()
+    return html.decode('UTF-8')
+
+def getImg(html):
+    reg = r'src="(.+?\.jpg)"'
+    imgre = re.compile(reg)
+    imglist = imgre.findall(html)
+    x = 0
+    path = 'D:\\test'
+    #将图片保存到D盘text文件夹中，如果么有则创建
+    if not os.path.isdir(path):
+        os.makedirs(path)
+    paths = path + "\\"
+    for imgurl in imglist:
+        urllib.request.urlretrieve(imgurl, '{0}{1}.jpg'.format(paths,x))#打开imglist中保存的图片网址，并下载图片保存在本地，format格式化字符串
+        x = x + 1
+    return imglist
+html_1 = getHtml("www.baid.com")#获取该网址网页详细信息，得到的html就是网页的源代码
+print(getImg(html_1))#从网页源代码中分析并下载保存图片
+
