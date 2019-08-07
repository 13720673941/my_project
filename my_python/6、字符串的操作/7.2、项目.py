# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/4 15:37

import pyperclip

text = "list of a."+"\n"+"list of b."+"\n"+"list of c."


lines = text.split('\n')

for i in range(len(lines)):

    lines[i] = "* " + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)

text = pyperclip.paste()

print(text)

