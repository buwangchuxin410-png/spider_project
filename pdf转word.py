# -*- coding: utf-8 -*-
# @Time    : 2024/3/16 17:23
# @Author  : 茶茶
# @File    : pdf转word
# @Software: PyCharm
print('\033[32m', end='')
from pdf2docx import Converter

pdf_file = r'F:\新建文件夹\12.pdf'
docx_file = r'F:\新建文件夹\12.docx'

cv = Converter(pdf_file)
cv.convert(docx_file, start_page=0, end_page=0, end=None)
cv.close()



