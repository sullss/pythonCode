import time
import datetime
import webbrowser
def music_break(self):
    #每天休息的次数
    #total_breaks = 4
    #判断休息循环结束的数值
    #break_count = 0
    #打印出程序开始的时间，ctime是获取当时时间函数
    print("程序于{0}开始启动".format(time.ctime()))
    time_num = self.ISOString2Time()
    return time_num
print(music_break(time.ctime()))
''' 
while(break_count<total_breaks):s


    #循环满足条件后，打开网页播放喜欢的音乐
#这里是让程序等待一段时间
time.sleep(2*60*60)
#打开指定网页
webbrowser.open('http://www.kugou.com/song/mp9twfd.html#hash=CA23D88A821DAEC640AC2417FD974BE7&album_id=0')
break_count +=1
print("程序于{0}结束，其中你休息了{1}次，真JB厉害！".format(time.ctime(),total_breaks))
'''

#将小时格式转化成秒
def ISOString2Time(self,s):
    d = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    return time.mktime(d.timetuple())
