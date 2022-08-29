#!/bin/python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'http://xkcd.com' # starting url

# Next line ensures that the 'xkcd' folder exists, and exist_ok = True
# prevents the function from throwing an error if the folder 
# already exists.  
os.makedirs('xkcd', exist_ok=True)  
    
while not url.endswith('#'): # confirmed this by going to comic #1
    # Download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status() # standard practice - will do nothing if everything is okay
    # get our soup object, get down to business.
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image. 
    # This here is where the scraping of the web happens. 
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else: 
        comicUrl = 'https:' + comicElem[0].get('src')
        # Download the image
        print(f'Downloading image {comicUrl}')
        res = requests.get(comicUrl)
        res.raise_for_status()
    
    # Save the image to ./xkcd
    # imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    
    #os.path.basename() returns the last part of a URL, which we use here as a filename
    # when saving them image.
    #os.path.join() joins the filenme to the path of the working dir. 
    
        with open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') as imageFile:
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)

    # Get the Prev button url
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')


