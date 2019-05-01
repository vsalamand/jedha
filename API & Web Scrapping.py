#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


r = requests.get("https://publish.twitter.com/oembed?url=https://twitter.com/Interior/status/463440424141459456")


# In[3]:


r.status_code


# In[4]:


html = r.json()["html"]


# In[5]:


content = open("twitter_api.html", "w")
content.write(html)
content.close()


# In[6]:


r_2 = requests.get("https://twitter.com/TwitterDev")


# In[7]:


r_2.text


# In[8]:


content = open("twitter_api_timeline.html", "w")
content.write(r_2.text)
content.close()


# In[9]:


r_w = requests.get("https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal")


# In[10]:


dark_sky = requests.get("https://api.darksky.net/forecast/073ed950bcd367ad35e76ea60cf5511c/48.8566,2.3522")


# In[11]:


dark_sky.json()


# In[12]:


(dark_sky.json()["currently"]["temperature"]-32)*5/9


# In[13]:


current_location = requests.get("http://api.ipstack.com/check", params={"access_key":"55896dde6c19b26566166b446fe84094"})


# In[14]:


ip = current_location.json()["ip"]


# In[57]:


location = requests.get("http://api.ipstack.com/{}".format(ip), params={"access_key":"55896dde6c19b26566166b446fe84094"})


# In[58]:


lat = location.json()["latitude"]
long = location.json()["longitude"]


# In[59]:


dark_sky = requests.get("https://api.darksky.net/forecast/073ed950bcd367ad35e76ea60cf5511c/{},{}".format(lat,long))


# In[61]:


dark_sky.json()


# In[15]:


(dark_sky.json()["currently"]["temperature"]-32)*5/9


# In[16]:


r_3 = requests.get('https://avatars.githubusercontent.com/u/1227972?')


# In[21]:


from PIL import Image
from io import BytesIO


# In[ ]:


i

