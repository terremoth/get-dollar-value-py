#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Made By Terremoth

import requests
from bs4 import BeautifulSoup

page = requests.get("https://dolarhoje.com")

if page.status_code == 200:
    parser = BeautifulSoup(page.content, 'html.parser')
    dolar_value_str = parser.find(id='nacional').get('value')
    dolar_value_float = float(dolar_value_str.replace(',','.'))
    print(dolar_value_float)
    
else:
    print("Failed to load page, because HTTP status code is: ", page.status_code)

