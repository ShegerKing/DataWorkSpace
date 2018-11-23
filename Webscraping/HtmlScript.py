#Web scarping tools
import urllib.request
from bs4 import BeautifulSoup
import csv


urlpage = 'http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'

# request to access web page
page  = urllib.request.urlopen(urlpage)

# put the html file into a BeautifulSoup object.
soup = BeautifulSoup(page, 'html.parser')

# When doing a search go through the table first
table = soup.find('table', attrs={'class':'tableSorter'})
results = table.find_all('tr')

rows= []
rows.append(['Rank', 'Company Name', 'Description', 'Location', 'Year end', 'Annual sales rise over 3 years', 'Sales £000s', 'Staff', 'Comments'])

for results in results:
    data = results.find_all('td')
    if len(data) == 0:
        continue
    # write columns to variables
    rank = data[0].getText()
    company = data[1].getText()
    location = data[2].getText()
    yearend = data[3].getText()
    salesrise = data[4].getText()
    sales = data[5].getText()
    staff = data[6].getText()
    comments = data[7].getText()


    companyname = data[1].find('span', attrs={'class': 'company-name'}).getText()
    description = company.replace(companyname, '')

    sales = sales.strip('*').strip('†').replace(',', '')

    rows.append([rank, companyname, description, location, yearend, salesrise, sales, staff, comments])

print (rows)
