#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 导入正则的包，这个包系统自带
import re
 
# 统计手机号的方法
def count():
 
    #手机号正则,"1"代表数字1开头，"[3|4|5|7|8]"代表第2位是3/4/5/7/8中任一个，"\d"代表0~9的数字，"{9}"代表按前面的规则取9次
    pattern_mob = re.compile('1[3|4|5|7|8|9]\d{9}')
    #打开html文件
    f = open("1.txt")
    #用正则匹配html文件中的内容，匹配结果放在变量result中，结果是list形式，如果匹配到两个就这样['13699999999', '17399999999']
    result = pattern_mob.findall(f.read())
    #返回匹配结果
    return result
    
# 主函数
if __name__ == '__main__':
    
    # 调用count()函数,并打印返回值
    print(list(set(count())))