"""Define functions for the main program"""

import os
import random
import urllib.request
from selenium import webdriver


def getimages(animal):
    # get the path of the chromedriver
    chrome_driver_path = "Gecko/chromedriver.exe"

    # create a new Chrome session
    driver = webdriver.Chrome(chrome_driver_path)
    driver.implicitly_wait(30)
    driver.maximize_window()

    # navigate to google
    driver.get("http://www.google.com")

    # get the search textbox
    search_field = driver.find_element_by_name("q")

    # enter search keyword and submit
    search_field.send_keys(animal)
    search_field.submit()

    # find the "Images" link and click
    driver.find_element_by_link_text('Images').click()

    # get the list of elements which are displayed after the search
    # currently on result page using find_elements_by_class_name method

    mylist = []
    images = driver.find_elements_by_tag_name('img')

    # cleaning of the list with filters
    mycleanlist = []
    for image in filter(None, images):
        mylist.append(image.get_attribute('src'))
    for i in filter(None, mylist):
        if i.startswith("https://"):
            mycleanlist.append(i)
    # run the downloader function for elements in the list
    for i in mycleanlist:
        downloader(i)

def downloader(image_url):
    # retrieve in myPath the files named by random integers
    file_name = random.randrange(1, 10000)
    myPath = "Downloads/"
    full_file_name = os.path.join(myPath, str(file_name) + '.jpg')
    urllib.request.urlretrieve(image_url, full_file_name)

