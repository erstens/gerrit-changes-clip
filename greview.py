#!/usr/bin/python
# -*- coding: UTF-8 -*-

##gerrit review 信息粘贴到剪贴板快捷脚本。
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
append = ''
user = ''
_os = ''

def __init__():
 cf = ConfigParser.ConfigParser()
 cf.read("global.conf")

 global append
 global site
 global user
 global _os

 append = cf.get("global", "append")
 site = cf.get("global", "site")
 user = cf.get("global", "user")
 _os = cf.get("global", "os")


def addToClipBoard(text):
 os_map = {
 	'mac':'pbcopy',
 	'win':'clip'
 }
 clipborad = os_map[_os]
 command = 'echo ' + text.strip() + '| ' + clipborad
 os.system(command)


def getAccountId():
 header = {
	 'Authorization':'Basic d2FuZ2FvOndhbmdhbw=='
 }
 r = requests.get(site + '/accounts/?q=' + user, headers=header)
 obj = json.loads(r.text[4:])
 return obj[0]['_account_id']


def getXhrData(_account_id):
 header = {
 	'Authorization':'Basic d2FuZ2FvOndhbmdhbw=='
 }

 payload = {'q' : 'is:open','O':'881'}
 status = 'NEW'

 r = requests.get(site + '/changes/', params=payload, headers=header)

 j = r.text[4:]
 obj = json.loads(j)

 s = ''

 for i in obj :
	 if status == i['status'] and _account_id == i['owner']['_account_id']:
		 s += site + '/' + str(i['_number']) + '\r'

 return s

##初始化
__init__()

##获取用户 id
_account_id = getAccountId()

##获取 changes 下面的 xhr 数据
s = getXhrData(_account_id)

##写到剪贴板
s += append
addToClipBoard(s)
