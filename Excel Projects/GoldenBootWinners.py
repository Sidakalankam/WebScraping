from bs4 import BeautifulSoup
import requests
import openpyxl

excel = openpyxl.Workbook()


sheet = excel.active
sheet.title = 'Premier League Golden Boot Winners'
print(excel.sheetnames)
sheet.append(['Year Won','Player Name','Club','Goals'])




page = requests.get("https://www.premierleague.com/news/1206108")

print(page.status_code)

soup = BeautifulSoup(page.text, "html.parser")

winners = soup.find("tbody").find_all('tr')

for winner in winners:
    th_tags = winner.find_all('th')
    td_tags = winner.find_all('td')

    if th_tags:  # Check if th_tags list is not empty
        year = th_tags[0].text





    if td_tags:  # Check if td_tags list is not empty
        name = td_tags[0].text
        club = td_tags[1].text
        tally = td_tags[2].text
    else:
        print("Data not found")
        continue

    print(year, name, club, tally)
    sheet.append([year, name, club, tally])

excel.save('Premier League Golder Boot Winners')






    





