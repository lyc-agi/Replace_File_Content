# -*- encoding: utf-8 -*-
# 替换性修改文件内容
__author__ = 'Liuyichuan'

import re
import os

pattern1 = re.compile(r'": "[a-f0-9]{18}')#分别需要替换两个
pattern2 = re.compile(r'数据为"[a-f0-9]{18}')


flag1 = 0#标记是否找到了要替换的文本
flag2 = 0
id10 = None
id20 = None

with open('test3.py', 'r', encoding='utf8') as f_read, open('test4.py', 'w', encoding='utf8') as f_write: #文件读写

    for line in f_read:  # 循环读取原文件的内容并写入新建的文件里
        if flag1 == 0:#找要替换的文本
            id10 = pattern1.search(line)
        if flag2 == 0:
            id20 = pattern2.search(line)

        if id10 != None and flag1 == 0:
            id10mid = id10.group()[23:]
            id10newmid = "123456"  #新的文本
            flag1 = 1  # 标记
        if id20 != None and flag2 == 0:
            id20mid = id20.group()[23:]
            id20newmid = "7890"  # 新的文本
            flag2 = 1  # 标记

        newline = line  # 每行内容默认不变
        if flag1 == 1:
            newline = newline.replace(id10mid, id10newmid)#替换旧的
            #print(newline)
        if flag2 == 1:
            newline = newline.replace(id20mid, id20newmid)
        f_write.write(newline)


f_read.close()#关闭文件
f_write.close()
os.remove('test3.py')#新文件替换旧文件
os.rename('test4.py', 'test3.py')
print("提示：成功更新test3.py")

