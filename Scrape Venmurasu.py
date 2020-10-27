from bs4 import BeautifulSoup
import requests
import os
import numpy as np
import time

# Change the novel name, number in series, total chaptes in the below lines 
# in small letters
novel = 'mutharkanal'
number = 1
chapters = 50

# Creating folders for novels downloads 
# Create a folder named 'Venmurasu' in desktop and change the username in the below
novel_folder = 'C:/Users/*****/Desktop/Venmurasu/Volume_{number}_{novel}'.format(novel = novel, number = number)
novel_images_folder = 'C:/Users/*****/Desktop/Venmurasu/Volume_{number}_{novel}/{novel}_images'.format(novel = novel, number = number)

os.mkdir(novel_folder)
os.mkdir(novel_images_folder)

# Scrapping the novel pages
url_list = []
page_number = np.arange(1,chapters+1)
images_url_list = []

os.chdir(novel_folder)
for x in page_number:
    webpage = ('https://venmurasu.in/{novel}/chapter-'+ str(x)).format(novel = novel)
    url_list.append(webpage)

for x in url_list:
    URL = x
    page = requests.get(URL)
    time.sleep(10)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_='content')
    
    # Append only text to the existing text file
    filename = '{novel}.txt'.format(novel = novel)
    t = open(filename,'a', encoding="utf-8")
    t.write(results.text)
    t.close()
    
    # Append the scrapped html page to the html file
    filename = '{novel}.html'.format(novel = novel)
    ti = open(filename,'a', encoding="utf-8")
    ti.write(str(results))
    ti.close()
    
    # Get Image URL's in the page
    image_tags = soup.findAll('img')
    for image_tag in image_tags:
        images_url_list.append(image_tag.get('src'))

# Save the images URL's in a text file
# Remove obviously repeating URL's
os.chdir(novel_images_folder)
images_url_list = [i for i in images_url_list if i != 'https://d33wubrfki0l68.cloudfront.net/38c7ea039030006145dd4e91c105db9e5460186b/a8b47/venmurasu.jpg']

filename_2 = '{novel}_images_urls.txt'.format(novel = novel)
i = open(filename_2,'a', encoding="utf-8")
i.write(str(images_url_list))
i.close()