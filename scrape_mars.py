#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import os
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import pymongo
import requests
import time
from selenium import webdriver


# In[22]:


browser = Browser('chrome')


# In[23]:


# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
get_ipython().system('which chromedriver')


# In[25]:


#executable_path = {'executable_path':'</usr/local/bin/chromedriver>'}


# In[26]:


executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# In[27]:


url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[28]:


print(soup.prettify())


# In[29]:


titulo = soup.find("div", class_="content_title").get_text()
parrafo = soup.find("div", class_="article_teaser_body").get_text()


# ## NASA Mars News

# In[ ]:





# In[30]:


print(f"{titulo}:{parrafo}")


# ## JPL Mars Space Images

# In[31]:


executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# In[40]:


url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[155]:


image_url = soup.footer.find("a", class_="button fancybox")["data-fancybox-href"]
featured_image_url = "https://www.jpl.nasa.gov" + image_url


# In[174]:


print(featured_image_url)


# ## Mars Weather

# In[181]:


executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

url = "https://twitter.com/marswxreport?lang=en"
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[215]:


tweets = soup.find_all("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")


# In[253]:


for tweet in tweets:
    tweet_parent = tweet.find_parent("div", class_="content")
    tweet_id = tweet_parent.find("a", class_="account-group js-account-group js-action-profile js-user-profile-link js-nav")["href"]
    
    if tweet_id == '/MarsWxReport':
        mars_weather = tweet_parent.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()
        break


# In[275]:


mars_weather


# In[276]:


## Mars Facts


# In[277]:


url = 'https://space-facts.com/mars/'


# In[280]:


info = pd.read_html(url)
info


# In[333]:


df = info[0]
df.columns = ["Descripcion", "Valor"]
df.set_index(df["Descripcion"], inplace=True)


# In[349]:


df = df[["Valor"]]


# In[389]:


html_info = df.to_html()
html_info = html_info.replace('\n', '')
html_info


# In[390]:


## Mars Hemispheres


# In[473]:


executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, "html.parser")

h3s = soup.find_all("h3")


# In[474]:


titles = []
for h3 in h3s:
    h3 = str(h3)
    h3 = h3[4:-14]
    titles.append(h3)
titles


# In[475]:


img_urls = []
for title in titles:
    browser.click_link_by_partial_text(title)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    img_urls.append(soup.find("div", class_="downloads").find("a")["href"])
img_urls


# In[535]:


hemisphere_image_urls = []
for title, img_url in zip(titles, img_urls):
    hemisphere_image_urls.append({"title": title, "img_url":img_url})

hemisphere_image_urls


# In[ ]:




