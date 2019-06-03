# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
torport = 9050
proxies = {
        'http': "socks5://localhost:{}".format(torport),
        'https': "socks5://localhost:{}".format(torport)
        }

print(requests.get('http://icanhazip.com').content)
print(requests.get('http://icanhazip.com', proxies=proxies).content)