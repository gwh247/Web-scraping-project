import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from twilio.rest import Client 

client = Client('AC67496fdbf77fe68315ecee8ed6170cc8','4c48db820f0615aa6f606fe572d0f280')
TwilioNumber = "+13236895159"
myCellPhone = "+19037300797"
textmessage = client.messages.create(to=myCellPhone,from_= TwilioNumber,body= "Hi there")



webpage = 'https://www.cryptocurrencychart.com/top/25'
# name, symbol, current price, % change, price based on change 

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
r = Request(webpage, headers=headers)
webpage = urlopen(r).read()

soup = BeautifulSoup(webpage, 'html.parser')

table_rows = soup.findAll("tr",attrs={"class":'row'})

print("Top 5 crypto currencies")

for row in table_rows[0:5]:
     td = row.findAll("td")
     place = td[0].text
     name = td[1].text.replace('\n',' ')
     price = float(td[2].text.replace(",","").replace('$',""))
     change = float(td[4].text.replace("%",''))
     price_change = round((price*change),2)
     name_list = [place ,': ','Name:', name]
     print()
     print("".join(name_list))
     print(f"Current Price: ${price}")
     print(f"Change% in 24hr: {change}")
     print(f"Price based on change: ${price_change}")
     print()

     if name == " Etherium (ETH) ":
          if price <= 3000:
               textmessage = client.messages.create(to=myCellPhone,from_= TwilioNumber,body= "Etherium is under $3000")
     if name == " Bitcoin (BTC) ":
          if price <= 40000:
               textmessage = client.messages.create(to=myCellPhone,from_= TwilioNumber,body= "Bitcoin is under $40,000")



