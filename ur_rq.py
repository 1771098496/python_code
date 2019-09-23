#! /usr/bin/python3
# _*_ coding:utf-8 _*_

import urllib.request

response = urllib.request.urlopen("https://www.python.org")
print(response.read().decode("  utf-8"))