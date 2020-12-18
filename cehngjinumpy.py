# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 07:50:50 2020

@author: 123
"""

import   numpy  as  np
xuehao=np.arange(1, 51,)
xuehao=np.transpose([xuehao])
chengji=np.random.randint(40, 100, size=(50,3))
e = np.concatenate((xuehao,chengji),axis=1)
c = e.copy() 
print("学号|课一|课二|课三|总分")
zongchengji=np.sum(chengji,axis=1)
zongchengji=np.transpose([zongchengji])
e = np.concatenate((e,zongchengji),axis=1)
print (e)
print("--------------------------------")
d = e.copy()
d=-d
d = d[d[:,4].argsort()]
dd=np.argsort(d[:,4])+1
ddd=np.transpose([dd])
d=-d
e = np.concatenate((d,ddd),axis=1)
print("学号|课一|课二|课三|总分|总分排名")
print (e)
mmm=np.mean(chengji,axis=0)
print("课程一课程二课程三的均值分别为:")
print(mmm)
vvv=np.var(chengji,axis=0)
print("课程一课程二课程三的方差分别为:")
print(vvv)
sss=np.std(chengji,axis=0)
print("课程一课程二课程三的标准差分别为:")
print(sss)





