#!/usr/bin/env python
# coding: utf-8

# In[2]:


print('조의 주피터서버에 오신것을 환영합니다.')


# In[5]:


print('2번째 셀 실행')


# # 내가 주석

# ## 나는 누구?

# * 나는 누구?
# * 나는 두번째 목록
# * 나는 세번째 목록

# ** 나는 더 작은 목록
# ** 나는 더작은 목록2

# In[11]:


### 나는 더 작은 제목


# # 나 는 제목이다.

# 나도 **제목**임

# # 제일 큰 제목
# ## 그다음 큰제목
# ### 아주 작은제목

# * 아침식사
# * 점심식사
# * 저녁식사
#     * 우동
#     * 라면

# * 삐뚫어질거야*
# ** 찐해질거야**
# *** 나느 찐하게 삐뚤어질거야***

# In[14]:


import pandas as pd


# In[26]:


df_2010 = pd.read_csv("../Documents/TjoeunData/2010.csv", encoding='euc-kr')
df_2011 = pd.read_csv("../Documents/TjoeunData/2011.csv", encoding='euc-kr')
df_2012 = pd.read_csv("../Documents/TjoeunData/2012.csv", encoding='euc-kr')


# In[37]:


total_jumsu = pd.concat([df_2012, df_2011, df_2012], ignore_index=True)


# In[40]:


total_jumsu['국어']


# In[42]:


total_jumsu['수학']


# In[44]:


total_jumsu['영어']


# In[48]:


total_jumsu.iloc[1]


# In[51]:


total_jumsu.iloc[0:2]


# In[52]:


total_jumsu.iloc[:,0] #iloc[행,열], iloc[행]


# In[53]:


# <div align='center'><img src="../Documents/TjoeunData/9937603E5DD4AF0419.png">
# <div align='center'><img src="../Documents/TjoeunData/9972874E5DD4B7201B.png">


# In[54]:


df_con1 = pd.read_csv("../Documents/TjoeunData/concat_1.csv", encoding='euc-kr')
df_con2 = pd.read_csv("../Documents/TjoeunData/concat_2.csv", encoding='euc-kr')
df_con3 = pd.read_csv("../Documents/TjoeunData/concat_3.csv", encoding='euc-kr')


# In[64]:


df_con2


# In[69]:


total = pd.concat([df_con1, df_con2, df_con3], sort=True, ignore_index=True)


# In[70]:


total


# In[71]:


total['A']


# In[74]:


total.iloc[:,6]


# In[76]:


total.iloc[2]


# In[78]:


total.iloc[4,:]


# In[81]:


row_append = df_con1.append(df_con2, ignore_index=True, sort=True)


# In[83]:


row_append


# In[84]:


type(row_append)


# In[85]:


row_append.columns


# In[89]:


inner_result = pd.concat([df_con1, df_con2, df_con3], join='inner')
inner_result


# In[94]:


inner_result2 = pd.concat([df_con1, df_con3], join='inner')
inner_result2


# In[100]:


inner_result3 = pd.concat([df_con1, df_con3], join='outer')
inner_result3


# In[106]:


df_country = pd.read_csv("../Documents/TjoeunData/archive (2)/country_wise_latest.csv")


# In[107]:


df_country


# In[116]:


df_exercise = pd.read_csv("../Documents/TjoeunData/exercise.csv", encoding='euc-kr')


# In[117]:


df_exercise


# In[ ]:




