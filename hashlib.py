# -*- coding:utf-8 -*-

import hashlib

z = hashlib.md5()
z.update('how to use md5 in python hashlib?')
print z.hexdigest()