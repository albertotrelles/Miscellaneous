from bs4 import BeautifulSoup
import requests

url="https://coinmarketcap.com/"
request = requests.get(url).text
page = BeautifulSoup(request, "html.parser")

#table and its contents (a table of 100 cryptocurrencies)
table = page.find("tbody")
coins = table.contents 


#####Loop for first 10 coins       (the ticker was in a <p> tag)
tickers = []
prices = []

for coin in coins[0:10]:

    i = 1
    for child in coin.contents[2:4]:
        
        if i == 1:
            a = child.find_all("p", class_ = "sc-e225a64a-0 dfeAJi coin-item-symbol") 
            ticker = a[0].string                                                                
            #print(ticker)
            tickers.append(ticker)

        elif i ==2:
            b = child.find_all("span")
            price = b[0].string
            #print(price)
            prices.append(price)
        i = i+1


#####Loop for last 90 coins      (the ticker was in a <span> tag with class "crypto-symbol")
for coin in coins[10::]:
    
    i = 1
    for child in coin.contents[2:4]:

        if i == 1:
            a = child.find_all("span", class_ = "crypto-symbol")
            ticker = a[0].string
            #print(ticker)
            tickers.append(ticker)

        elif i == 2:
            b = child.find_all("span")
            #price = b[0].string                  #this doesn't work this time. I transform b into a string and get the text 
            #print(price)                         #this prints "None"
            r1 = str(b)
            r2 = r1[16::]
            r3 = r2[0: (len(r2) - 8) ]
            price = "$" + r3
            #print(price)
            prices.append(price)

        i = i+1


#####Making the Database
import pandas as pd

dataframe = pd.DataFrame( list(zip(tickers, prices)) )
dataframe.to_csv("Dataframe.csv")