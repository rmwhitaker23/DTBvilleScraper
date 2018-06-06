from bs4 import BeautifulSoup
import requests
import re

page = requests.get("https://events.downtownbentonville.org/")
page.status_code
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

# Open text file for raw data output
output = open('bentonvilleEvents.txt', 'w')
# Write table headers to top of output file to be used when importing data
output.write("Title| Time| Venue\n")

# Find number of instances of times on list
numTimes = len(soup.find_all(class_="timely-title-text"))

for y in range(numTimes-2):
  print(y+1)
  #Get title, time, venue, and category of event y
  title = soup.find_all(class_="timely-title-text")[y].get_text()
  time = soup.find_all(class_="timely-start-time")[y].get_text()
  venue = soup.find_all(class_="timely-venue")[y].get_text()
  # remove tabs, new lines, and a dash from time
  time = time.replace('\t', '')
  time = time.replace('\n', '')
  time = time.replace('-', '')
  venue = venue.replace('\t', '')
  venue = venue.replace('\n', '')
  venue = venue.replace('-', '')  
  # Print event info with new line to separate them
  # Don't need this, but nice to see when developing
  print(title.strip())
  print(time.strip())
  print(venue.strip())
  print("\n")
  # Output to text file using .encode('utf-8') because otherwise ascii error will occur
  output.write(title.encode('utf-8') + "| ")
  output.write(time.encode('utf-8') + "| ")
  output.write(venue.encode('utf-8') + "\n")



#For testing on first event in calendar
''' x=28
title = soup.find_all(class_="timely-title-text")[x].get_text()
time = soup.find_all(class_="timely-start-time")[x].get_text()
time = time.replace('\t', '')
time = time.replace('\n', '')
time = time.replace('-', '')
venue = soup.find_all(class_="timely-venue")[x].get_text()
print(title.strip())
print(time.strip())
print(venue.strip())
print("\n") '''

''' # find number of days
numChildren = len(soup.find_all('h2'))
print numChildren '''

# Close the output file
output.close()