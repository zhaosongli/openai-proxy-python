# -*- coding: utf-8 -*-

import requests
import sys
import json

args = sys.argv
prompt = args[1]

url = 'http://54.174.76.96:8000/v1/chat/completions'

data = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "prompt": args[1]
}

# ��������
x = requests.post(url, data = json.dumps(data))

# ������ҳ����
print(x.text)
