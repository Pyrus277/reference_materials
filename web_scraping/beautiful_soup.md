## Beautiful Soup Notes 
### From the book *Automate the boring stuff* by Al Sweigart   
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
Once you have this bs4 object, you can use its methods to locate specific parts of an 
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

**Instead of writing the selector yourself, you can right click the element in your
browser and select "Inspect Element". When the developer's console opens, right-click
the element's HTML and select "Copy > CSS Selector" to copy the selector string to the
clipboard and paste it into your source code.**  
    
The select() method will return *a list of Tag objects*, which is how BS represents an
HTML element, one Tag object for every match in the object HTML. You can put the str() function on them to show the HTML they represent.  
 
Here's Beautiful Soup in action given the following HTML text. 
In the Python code, note teh .getText() and .attrs methods.
 
```html
 <!-- This is the example.html file. -->

<html>
    <head>
        The Website Title
    </head>
<body>
    <p>Download my <strong>Python</strong> book from 
    <a href="https://inventwithpython.com">my website</a>.</p>
    <p class="slogan"></p>Learn Python the easy way!</p>
    <p>By <span id="author">Al Sweigart</span></p>
</body>
</html>
 ```
 ```python
 import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
print(type(elems))
# <class 'bs4.element.ResultSet'>
len(elems)
# 1
type(elems[0])
# <class 'bs4.element.Tag'>
str(elems[0])
# <span id="author">Al Sweigart</span>'
elems[0].getText()
# 'Al Sweigart
elems[0].attrs
# {'id': 'author'}
```
Example of getting data from an element's attributes:
```python
import bs4
soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanElem = soup.select('span')[0]
str(spanElem)
# <span id="author">Al Sweigart</span>'
spanElem.get('id') # Here's where it happens
# 'author'
spanElem.get('some_nonexistent_addr') == None
# True
spanElem.attrs
# {'id':'author'}
```
