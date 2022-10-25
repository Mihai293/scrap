from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.anaf.ro/restante/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup)
table = soup.find('table')
# print(table)
head = []
col = []
for x in table.find_all('th'):
    title = x.text
    head.append(title)
# print(head)
df = pd.DataFrame(columns=head)
for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    print(data)
    row_data = [td.text.strip() for td in data]
    length = len(df)
    print(row_data)
    # df.loc[length] = row_data
# for i in head('Codul de identificare fiscală'):
#     coloana = i.text
#     col.append(coloana)
# print(col)