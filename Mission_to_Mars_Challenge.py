
# import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager 
import pandas as pd


#set your executable path in the next cell, then set up the URL https://redplanetscience.com/ for scraping.
#Creating the instance of a Splinter browser, means- prepping automated browser and specifying Chrome as the browser
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Visit the mars nasa news site

url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


#set up the HTML parser:
html = browser.html
news_soup = soup(html,"html.parser")

slide_elem = news_soup.select_one("div.list_text")


#assign the title and summary text to variables
slide_elem.find('div', class_='content_title')


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images 

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)




#creating the new variable to hold the scraping results 
full_image_elem = browser.find_by_tag("button")[1]

#splinter will click the image to view the full size 
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')



#BeautifulSoup to look inside the <img /> tag for an image with a class of fancybox-image.
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel



#the variable img_url holds the f string 
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


#collection of mars facts 

df = pd.read_html("https://galaxyfacts-mars.com")[0]

#assigning the column to the dataFrame
df.columns = ["description","Mars","Earth"]
df.set_index("description",inplace= True)
df


#convert the dataFrame into HTML -ready code using .to_html()
df.to_html()

browser.quit()


# Mission_to_Mars_Challenge_starter_code

# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


slide_elem.find('div', class_='content_title')


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


df.to_html()


# ## D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# ### Hemispheres


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# 1. use your browser to visit the Mars Hemispheres website to view the hemisphere images.
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)



# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    
    #create a empty dictionary
    hemispheres = {}
    
    browser.find_by_css("a.product-item h3")[i].click()                                     
    element = browser.find_by_text("Sample").first
    img_url= element["href"]
    title = browser.find_by_css("h2.title").text
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)
    browser.back()


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# 5. Quit the browser
browser.quit()





