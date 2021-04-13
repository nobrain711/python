# -*- coding: utf-8 -*-
"""
시간을 입력 받아 초로 변화하는 프로그램
"""

hour = int(input("시간을 입력하세요."))
minu = int(input("분을 입력하세요."))
sen = hour * 60 * 60 + minu * 60
print(sen,"초")

