#!/usr/bin/env python
# coding: utf-8

# In[20]:


import os
#os.chdir(r'C:\\Users\11852\Desktop')
dic={}
header=1
r=open('out_statics','w')
with open ('snp_merge.txt') as f:
    for lineL in f:
        if header:
            header-=1
        else:
            line=lineL.strip().split('\t')
            if line[0] not in dic:
                dic[line[0]]=[int(line[1])]
            else:
                dic[line[0]].append(int(line[1]))


for k,v in dic.items():
    v=sorted(v)
    if v[-1]-v[0]>100000:
        for i in (range(len(v))):
            if v[i]+100000<v[-1]:
                count=len([j for j in filter(lambda x: x<=(v[i]+100000),v[i:-1])])
                r.write(k+"\t"+str(v[i])+"\t"+str(v[i]+100000)+"\t"+str(count)+"\n")
            else:
                count=len([j for j in filter(lambda x: x<=v[-1],v[i:-1])])
                r.write(k+"\t"+str(v[i])+"\t"+str(v[-1])+"\t"+str(count)+"\n")
    else:
        count=len([j for j in filter(lambda x: x<=v[-1],v[i:-1])])
        r.write(k+"\t"+str(v[0])+"\t"+str(v[-1])+"\t"+str(count)+"\n")
                
        
r.close()
