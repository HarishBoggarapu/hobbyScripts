# About:
#     Get the list of technology stacks and reponsibilties required for a particular job
#   Top 10 job sites:
#     (Indeed, CareerBuilder, Dice, Glassdoor, Google for Jobs, Idealist, LinkedIn, Monster, US.jobs)

import requests
from bs4 import BeautifulSoup
import re
# get info from Indeed site

payload = {'q': 'python developer',
           'I': '',
           'start': 40}
joblist = requests.get('https://www.indeed.com/jobs', params=payload).text
soup = BeautifulSoup(joblist, 'lxml')
searchCount = soup.find('div', id='searchCount').text.strip()
print("*********** {} ************\n".format(searchCount))
jobprofiles = soup.find('td', id='resultsCol')
alljobs = soup.find_all('div', class_='jobsearch-SerpJobCard unifiedRow row result')

# viewJob = requests.get('https://www.indeed.com/viewjob?jk=397863d5023e215d&from=serp&vjs=3')

for job in alljobs:
    try:
        indLink = alljobs[0].find('div', class_='title').a.get('href')
        viewPaylod = {
            'jk': alljobs[0].get('data-jk'),
            'from': 'serp',
            'vjs': indLink.split('=')[-1].strip()
        }
        viewJob = requests.get('https://www.indeed.com/viewjob', params=viewPaylod)
        jobtitle = job.find('div', class_='title').text.strip()
        joblocation = job.find('div', class_='location').text.strip()
        jobsummary = job.find('div', class_='summary').text.strip()
        print(jobtitle)
        print(joblocation)
        print(jobsummary)
    except:
        ()
