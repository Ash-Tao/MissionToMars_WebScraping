from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
import time
import pymongo

def scrape_info():
    # set up mongo
    # Use PyMongo to establish Mongo connection
    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client.mars_db
    collection = db.images


    # check if database exists if it does, delete it 
    dblist = client.list_database_names()
    if 'mars_db' in dblist:
        db.drop_collection('images')

    # Setup splinter
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # 1. NASA Mars News
    news_url = "https://redplanetscience.com/"
    browser.visit(news_url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    slide_elem = soup.select_one('div.list_text')
    news_title = slide_elem.find('div', class_="content_title").text.strip()
    news_p = soup.find('div', class_='article_teaser_body').text.strip()


    # 2. JPL Mars Space Images—Featured Image
    image_url = "https://spaceimages-mars.com/"
    browser.visit(image_url)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    featured_image_title = soup.find('h1', class_="media_feature_title").text.strip()
    featured_image_url = image_url + soup.find('img', class_='headerimage fade-in')['src']



    # 3. Mars Facts
    mars_facts_url = "https://galaxyfacts-mars.com/"
    tables = pd.read_html(mars_facts_url)

    tables[0]
    earth_mars_facts_table = tables[0].loc[1:,:].set_index([0])
    earth_mars_facts_table.index.name=None
    earth_mars_facts_table.columns = ['Mars','Earh']

    html_table = earth_mars_facts_table.to_html(index=True, header=True, classes="table table-striped")

    # 4. Mars Hemispheres
    hemi_url = 'https://marshemispheres.com'
    #parse the landing page, isolate the image links in the item div
    browser.visit(hemi_url)
    hemi_html = browser.html
    soup = BeautifulSoup(hemi_html, "html.parser")
    # hemi_links = hemi_soup.find("div", class_='collapsible results')
    # collect all items in collapsible resultes container
    hemi_links = soup.find_all('div', class_='item')

    # print(hemi_links)

    hemisphere_image_urls = []
        # loop through each hemisphere data
    for hemi_link in hemi_links:

        img_name = hemi_link.find('h3').text
        artical_url = hemi_url +"/"+ hemi_link.a['href']

        browser.visit(artical_url)        
        hemi_html = browser.html
        hemi_soup = BeautifulSoup(hemi_html, 'html.parser')        

        hemi_img_url = hemi_url+"/"+hemi_soup.find('img', class_='wide-image')['src']

        hemisphere_image_url = {
            'title': img_name,
            'img_url': hemi_img_url
        }
        hemisphere_image_urls.append(hemisphere_image_url)



    mission_to_mars ={
        'news_title' : news_title,
        'summary': news_p,
        'featured_image_title': featured_image_title,
        'featured_image': featured_image_url,
        'fact_table': html_table,
        'hemisphere_images': hemisphere_image_urls
        }
    # collection.insert_one(mission_to_mars)

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mission_to_mars
