## Beautiful Soup Notes  
Basic syntax combo with requests module:  
```python
import requests, bs4
res = requests.get('https://nostarch.com') # dl the main page from that site
res.raise_for_status() # check for no errors
# Pass the text attribute of the response to bs4.BeautifulSoup(),
# and store it in a variable:
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup) # confirm a bs4 object
```  
You can also load an HTML file you saved locally by passing the file object
to bs4.BeautifulSoup(), along with a second argumnet specifying the parser to
use to analyze the HTML ('html.parser' is the basic one that comes with Python,
explore others):
```python
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
type(exampleSoup) # confrim it's a bs4 obejct
```
Once you have this bs4 object, you cna use its methods to locate specific parts of an 
HTML document. This is a much more reliable and effieicnt alternative to regexp. 
You can retrieve a web page element from a bs4 object by calling the select() method
and passing a string of a CSS selector for the element you are looking for.  
A selector tutorial can be found here: https://nostarch.com/automaatestuff2/ 
Here are some of the most common CSS selector patterns:

|selector passed | Will match... |
|----|----|
|soup.select('div') | All elements named <div> |
|soup.select('#author') | The element with an id attribute of author |
|soup.select('.notice') | All elements that use a CSS class attribute |
|soup.select('div span') | All elements named <span> that are within an element named <div> |
|soup.select('div > span') | All elements named <span> that are directly within an element named <div>, with no other element in between |
|soup.select('input[name]') | All elements named <input> that have an attribute with any value |
|soup.select('input[type="button"]') | All elements named <input> that have an attribute named type with value button |



