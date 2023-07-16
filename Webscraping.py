from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
import pandas as pd

html_data = requests.get('https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks').text
soup = BeautifulSoup(html_data,'html5lib')
data=pd.DataFrame(columns=["Name", "Market Cap(US$ Billion)"])

rows = soup.find_all('tbody')[2].find_all('tr')
for row in rows:
    cells =row.find_all('td')
    if (cells != []):
        name = cells[1].text.strip()
        marketcap = cells[2].text.strip() #strip method Leading means at the beginning of the string, trailing means at the end.
        #You can specify which character(s) to remove, if not, any whitespaces will be removed.
        data = data.append({"Name":name, "Market Cap(US$ Billion)":marketcap}, ignore_index=True)    
         
#data.to_json("bank_market_cap.json")
data.to_csv("bank_market_cap2.csv")