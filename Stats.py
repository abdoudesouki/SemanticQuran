# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 08:54:30 2022

@author: abdel
"""

import io
xx=10
with io.open('D:\\\\Dropbox\\\\Web\\\\SemQuran\\\\Repo\\\\ayat.tsv', 'r',encoding='utf8') as f:
    for i in range(xx):
        aa = f.readline()
        print(i,aa)
#%%
import pandas as pd

ayat=pd.read_csv('D:\\\\Dropbox\\\\Web\\\\SemQuran\\\\Repo\\\\ayat.tsv', sep='\t',encoding='utf8')
print(ayat)
#%%
print(ayat['PartNo'].value_counts())

print(ayat['sw_id'].value_counts())
# آيات وردت ثلاث مرات أو أكثر
aa=ayat['text'].value_counts()
Res1=aa[aa>=3]
print(Res1)
