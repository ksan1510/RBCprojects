# Dependencies
from bs4 import BeautifulSoup
import time
from splinter import Browser
import requests
import pymongo
import pandas as pd
import json

def init_browser():
    
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    mars_data = {}

    # visit marsnews.com
    MarsNews='https://mars.nasa.gov/news/'
    browser.visit(MarsNews)
    time.sleep(10)
    html = browser.html
    
    #create a soup object from the HTML
    soup = BeautifulSoup(html, 'html.parser')
    article = soup.find("div", class_='list_text')

    #scrape latest news title and paragraph
    news_title = article.find("div", class_="content_title").text
    news_p = article.find("div", class_ ="article_teaser_body").text
    mars_data["news"]= news_title
    mars_data["newsp"]= news_p

    #scrape Mars features image
    nasafeature= 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(nasafeature)
    time.sleep(10)
    html = browser.html
    
    #create soup object for HTML
    soup1 = BeautifulSoup(html, 'html.parser')
    image = soup1.find("article", class_="carousel_item")
    image_url = "https://www.jpl.nasa.gov" + image["style"][23:75]
    mars_data["featured_image"]= image_url


    #scrape mars weather Twitter account 
    twitter = "https://twitter.com/marswxreport?lang=en"
    response = requests.get(twitter)

    #create soup object for html and scrape latest weather tweet
    soup2 = BeautifulSoup(response.text, "html.parser")
    mweather = soup2.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    mweather = mweather.replace("\n", " ")
    mars_data["weather"]=mweather


    #scrape mars facts from mars facts website
    marsFacts = "https://space-facts.com/mars/"
    tables = pd.read_html(marsFacts , encoding= "utf-8")
    type(tables)
    tables
    df = tables[0]
    df.columns = ['Mars Facts','Answered']
    #dump DF into json
    df1= json.dumps(df.to_dict(orient='list'))
    mars_data['Mars_Facts']=df1


    hemisphere='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemisphere)

    hemis=[]

    links= browser.find_by_css("a.product-item h3")
    for i in range(len(links)):
    
    #find elements using splinter and beautiful soup
        browser.find_by_css("img.thumb")[i].click()
        time.sleep(5)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        title= browser.find_by_css('h2').text
        title= title.replace("Enhanced", "")
        hemis.append({"title": title, "link": image_url})
        browser.back()

    mars_data['hemisphere']=hemis

    browser.quit()
    return mars_data
