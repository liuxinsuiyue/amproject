#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# !/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)
第一层字典，第二层列表，第三层字典，字典里是key-value键值对
{
	"q": "",
	"p": false,
	"bs": "",
	"csor": "0",
	"err_no": 0,
	"errmsg": "",
	"g": [{
		"type": "his_normal",
		"sa": "h_1",
		"q": "怎么看报文有没有对密码进行加密"
	}, {
		"type": "his_normal",
		"sa": "h_2",
		"q": "虞书欣工作室再发文"
	}],
	"queryid": "0x9431deddb12a58"
}