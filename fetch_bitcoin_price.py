__author__ = "Kevin Selm"
__version__ = "0.1.0"

import requests, threading

from config import BITCOIN_URL

def getPrice():
  """
  Fetch the price of bitcoin and return
  """
  data = ""
  
  try:
    res = requests.get(BITCOIN_URL)
    data = res.json()
  except (requests.Timeout, requests.ConnectionError, requests.HTTPError) as err:
    print("Error making the request")
    print(err)
  finally:
    return data['bpi']['USD']['rate']



def repeatFetch():
  """
  Run getPrice() every 20 seconds using threading.Timer 
  """
  print(getPrice())
  # oldPrice = getPrice()
  # newPrice = getPrice()
  t = threading.Timer(30, repeatFetch).start()

repeatFetch()


# print(getPrice)
# print('The price of bitcoin: $',getPrice())
