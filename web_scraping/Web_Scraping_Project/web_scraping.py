# https://www.youtube.com/watch?v=XVv6mJpFOb0&list=WL&index=3&t=1526s

# This builds on the basic_commentary version of the file by adding:
#   -Better formatting
#   -Having the program to set to run at specific times
#   -Apply filtrations to remove irrelevant jobs
#   -Put the results of the different job posts into a new blank file

from bs4 import BeautifulSoup
import requests
import time

print("Put some skills that you don't have")
unfamiliar_skills = input('>')
print(f'Filtering out {unfamiliar_skills}')
unfamiliar_skills_lst = unfamiliar_skills.lower().split()

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Java+%2C+Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span',class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_= 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if not bool(set(unfamiliar_skills_lst) & set(skills.lower().strip().split(','))):
                with open(f"./webscrape_posts/{index}.txt", "w") as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info} \n")
                print(f'File saved: {index}')
                

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
