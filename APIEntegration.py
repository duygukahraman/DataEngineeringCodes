import requests
import pandas as pd

url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=apikey"  #Make sure to change ******* to your API key.
response = requests.get(url)
#print(response.text)
data = response.json()
dataf = pd.DataFrame(data, columns=['Rates'])

dataf.to_csv("exchange_rates_1.csv")
