import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

bitcoin = pd.read_csv('BTC-CAD.csv', index_col='Date', parse_dates=True)
ethereum = pd.read_csv('ETH-CAD.csv', index_col='Date', parse_dates=True)

#For having DateTime Index
#index_col='Date'
#parse_dates=True

#2016-2021
#print(bitcoin.head())

#bitcoin['Close'].plot()
#plt.show()

#print(bitcoin.index)

#Study of only 2019
#bitcoin['2019-09']['Close'].plot()
#plt.show()

#Sept only
#bitcoin['2019-09']['Close'].plot()
#plt.show()

#2017-2019
#bitcoin.loc['2017':'Close'].plot()
#bitcoin['2019-09']['Close'].plot()
#plt.show()

#bitcoin.loc['2020':'2021','Close'].resample('M').plot()
#plt.show()

#By month and mean
#bitcoin.loc['2019','Close'].resample('M').mean().plot()
#plt.show()

#Mean by week
#bitcoin.loc['2019','Close'].resample('W').mean().plot()
#plt.show()

#bitcoin.loc['2019','Close'].resample('W').std().plot()
#plt.show()

#plt.figure(figsize=(12, 8))
#bitcoin.loc['2019':'2021','Close'].plot()
#bitcoin.loc['2019':'2021','Close'].resample('M').mean().plot(label='Average per month', lw=3, ls=':', alpha=0.8)
#bitcoin.loc['2019':'2021','Close'].resample('W').mean().plot(label='Average per week', lw=2, ls='--', alpha=0.8)
#plt.title('Bitcoin Price from 2019 to 2021')
#plt.legend()
#plt.savefig('Bitcoin2019-2021.png')
#plt.show()
#plt.savefig('Bitcoin2019-2021.png')

# =============================================================================
# m = bitcoin.loc['2019', 'Close'].resample('W').agg(['mean', 'std','min', 'max'])
# 
# plt.figure(figsize=(12,8))
# m['mean']['2019'].plot(label='moyenne par semaine')
# plt.fill_between(m.index, m['max'], m['min'], alpha=0.2, label='min-max par semaine')
# 
# plt.legend()
# plt.show()
# 
# =============================================================================

# bitcoin.loc['2019','Close'].rolling(window=7).mean()
# =============================================================================
# 
# plt.figure(figsize=(12, 8))
# bitcoin.loc['2019-09','Close'].plot()
# bitcoin.loc['2019-09','Close'].rolling(window=7, center=True).mean().plot(label='non centre', lw=3, ls=':', alpha=0.8)
# bitcoin.loc['2019-09','Close'].rolling(window=7, center=True).mean().plot(label='centre')
# bitcoin.loc['2019-09','Close'].ewm(alpha=0.6).mean().plot(label='centre')
# 
# plt.legend()
# plt.savefig('Bitcoin2019-2021.png')
# plt.show()
# =============================================================================


#ethereum['2019']['Close'].plot()

btc_eth = pd.merge(bitcoin, ethereum, on='Date', how='inner', suffixes=('_btc','_eth'))
#btc_eth[['Close_btc','Close_eth']].plot(subplots=True, figsize=(12,18))

btc_eth[['Close_btc','Close_eth']].corr()


