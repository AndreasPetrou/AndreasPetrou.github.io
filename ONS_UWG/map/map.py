#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 15:59:32 2022

@author: andreaspetrou
"""

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/martinjc/UK-GeoJSON/master/json/electoral/gb/eer.json') as response:
    counties = json.load(response)

counties["features"][0]