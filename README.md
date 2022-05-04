# web-scraping-challenge
## Target - Mission to Mars

Build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. <br/>

## Part  1: Scraping

Create scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.<br/>

Create a Jupyter Notebook file called [mission_to_mars.ipynb](https://github.com/Ash-Tao/web-scraping-challenge/blob/main/Missions_to_Mars/mission_to_mars.ipynb) to complete the below tasks: <br/>

#### 1. NASA Mars News

* Scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. <br/>

  >**Example:**<br/>
  >news_title = "NASA Mars Mission Connects With Bosnian and Herzegovinian Town"<br/>
  >news_p = "A letter from NASA was presented to the mayor of Jezero, Bosnia-Herzegovina, honoring the connection between the town and Jezero Crater, the Mars 2020 rover landing site."<br/>


#### 2. JPL Mars Space Images—Featured Image

* Visit the URL for the Featured Space Image site [here](https://spaceimages-mars.com).<br/>

* Use Splinter to navigate the site and find the image URL for the current Featured Mars Image.<br/>

  >**Example:**<br/>
  >featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'<br/>


#### 3. Mars Facts

* Visit the [Mars Facts webpage](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including diameter, mass, etc.<br/>

  >**Example:**<br/>
  >tables = pd.read_html(mars_facts_url)<br/>

#### 4. Mars Hemispheres

* Visit the [astrogeology site](https://marshemispheres.com/) to obtain high-resolution images for each hemisphere of Mars.
  >**Example:**<br/>
  >hemisphere_image_urls = [<br/>
  >    {"title": "Cerberus Hemisphere Enhanced", "img_url": "..."},<br/>
  >    {"title": "Schiaparelli Hemisphere Enhanced", "img_url": "..."},<br/>
  >    {"title": "Syrtis Major Hemisphere Enhanced", "img_url": "..."},<br/>
  >    {"title": "Valles Marineris Hemisphere Enhanced", "img_url": "..."},]<br/>


- - -

## Part 2: MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all the information that was scraped from the URLs above.<br/>

* Create a Flask app [app.py](https://github.com/Ash-Tao/web-scraping-challenge/blob/main/Missions_to_Mars/app.py)<br/>
  * Create a root route `/` that will query your Mongo database and pass the Mars data into an HTML template for displaying the data.<br/>
  * Create a route called `/scrape` that will import [scrape_mars.py](https://github.com/Ash-Tao/web-scraping-challenge/blob/main/Missions_to_Mars/scrape_mars.py) script and call `scrape` function. Store the return value in Mongo as a Python dictionary.<br/>

* Create a template HTML file called [index.html](https://github.com/Ash-Tao/web-scraping-challenge/blob/main/Missions_to_Mars/templates/index.html)<br/>
  * Display all the data in the appropriate HTML elements. <br/>

* Final product should look like:<br/>
  <img src="https://github.com/Ash-Tao/web-scraping-challenge/blob/main/Missions_to_Mars/Screenshots%20of%20your%20final%20application.png"><br/>
  
## Files
- [mission_to_mars.ipynb](https://github.com/Ash-Tao/web-scraping-challenge/blob/main/Missions_to_Mars/mission_to_mars.ipynb)<br/>
- [app.py](https://github.com/Ash-Tao/web-scraping-challenge/blob/main/Missions_to_Mars/app.py)<br/>
- [scrape_mars.py](https://github.com/Ash-Tao/web-scraping-challenge/blob/main/Missions_to_Mars/scrape_mars.py)<br/>
- [templates](https://github.com/Ash-Tao/web-scraping-challenge/tree/main/Missions_to_Mars/templates)<br/>
  - index.html<br/>
  - earth_mars_facts_table.html<br/>
  - mars_facts_table.html<br/>
- [Screenshots of your final application.png](https://github.com/Ash-Tao/web-scraping-challenge/blob/main/Missions_to_Mars/Screenshots%20of%20your%20final%20application.png)<br/>

