#!/usr/bin/python
# -*- coding: UTF-8 -*-

##gerrit 打印信息：指定 gerrit 下的所有项目clone 地址，然后粘贴到 shell 执行。
'''
require:
	python2.x
	requests:
		npm to install requests
'''
import ConfigParser
import json
import requests

import os

##全局变量
site = ''
_os = ''

def __init__():
 cf = ConfigParser.ConfigParser()
 cf.read("global.conf")

 global site
 global _os

 site = cf.get("global", "site")
 _os = cf.get("global", "os")


def addToClipBoard(text):
 os_map = {
 	'mac':'pbcopy',
 	'win':'clip'
 }
 clipborad = os_map[_os]
 command = 'echo ' + text.strip() + '| ' + clipborad
 os.system(command)


def getXhrData():
 header = {
 	'Authorization':'Basic d2FuZ2FvOndhbmdhbw=='
 }

 r = requests.get(site + '/projects/?d', headers=header)

 j = r.text[4:]
 obj = json.loads(j)
 
 s = ''

 for i in obj :
 	 print i
	 #s += 'git clone ssh://wangao@gerrit.dev.aixuexi.com:29418/' + i + ' && ' + '\r' 
	 #print s

 return s

##初始化
__init__()

##获取 changes 下面的 xhr 数据
s = getXhrData()

print s
