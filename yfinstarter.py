import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import yfinance as yf 
from datetime import datetime

# share = yf.Ticker('av.l')
share = yf.Ticker('f')

shareinfo = share.info

for key,value in shareinfo.items():
    if (key == "underlyingSymbol" or key == "longName"):
        print(key, ":", value)

print(share.recommendations)
print(share.splits)
