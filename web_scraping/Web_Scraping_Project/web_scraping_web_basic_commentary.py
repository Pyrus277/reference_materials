# https://www.youtube.com/watch?v=XVv6mJpFOb0&list=WL&index=3&t=1526s
# Start to 48:27

from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Java+%2C+Python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')

# We then use Inspect and find that our search results are in here:
# <ul class="new-joblist">
# And under this are each individual find, each containing the content
# we want to scrape:
#    <li class="clearfix job-bx wht-shd-bx"></li>
# And to access these elements we go:
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    # ^ .find(), vs find_all(), will just find the first match.
    # Using .find(), we find the nugget we want is in the H3 tag
    # Now, we don't want all the h3 tags, just those within "jobs"
    # so we go:
for job in jobs:
    # Unlike for what company_name and skills bring up (below), this is inside a span tag
    #   within another span tag. So what do?
    published_date = job.find('span', class_='sim-posted').span.text
    # print(published_date)
    # With .span.text at the end we get what we need. We don't want to print this
    # though, just use it as a filter criteria:

    if 'few' in published_date:
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            #.replace(' ','') gets rid of the whitespace that would otherwise be in that output.
        skills = job.find('span', class_='srp-skills').text.replace(' ','')
        # print(company_name)
        # print(skills)
        # We also just want to pick out postings that were "Posted few days ago."
        # So we do more poking around and discover that tag exists within class='sim-posted'




        print(f'''
        Company Name: {company_name}
        Required Skills: {skills}
        ''')

        print('')

# One thing though-- like with so many sites that return results, the results are
# paginated. So how can we access the finds on page 2, and 3 and so on??

