from bs4 import BeautifulSoup

with open('example2.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    # here's where it get interesting:
    course_cards = soup.find_all('div', class_='card')
    #^ .find_all method here will get you all the div tags that
    # also have the class='card' tag as a LIST. Note the underscore after 
    # class-- class is a python keyword, and the underscore lets it
    # pass to bs4 as a specified bit of text.    
    # print(course_cards)
    for course in course_cards:
    # Now this is also very useful:
        course_name = course.h5.text  
        course_price = course.a.text   
        # this will specifically get the h5 parts out of your
        # list of bs4 (div, class='card') objects.
        # print(course_price)

        print(f"{course_name} costs {course_price.split()[-1]}")
        # and you can dig deeper:
    #    
    #    print(f"hello {}  ")