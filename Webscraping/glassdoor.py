from bs4 import BeautifulSoup
from requests import get

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) '
            'AppleWebKit/537.36 (KHTML, like Gecko)'
            ' Chrome/41.0.2228.0 Safari/537.36'})
sapo = "https://www.glassdoor.com/Job/us-data-science-summer-intern-jobs-SRCH_IL.0,2_IN1_KO3,29.htm"


response = get(sapo, headers=headers)


html = BeautifulSoup(response.text, 'html.parser')

hover = html.find_all('li', class_='jl')
Jobs = []
print(len(hover))
for item in range(len(hover)):
    job = hover[item]

    title = job.find('div',class_ = 'flexbox jobTitle').find('a').getText()
    location = job.find('div', class_ = 'flexbox empLoc').find('span').getText()
    Jobs.append([title, location])

print(Jobs)

