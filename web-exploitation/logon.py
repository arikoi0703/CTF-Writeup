import requests
import re

url = 'https://2019shell1.picoctf.com/problem/37907/flag'

cookie = input('cookie: ')

r1 = requests.get(url, headers={'Cookie': cookie})
print(r1.text)
