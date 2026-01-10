import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ticker symbols for pairs trading
t1="AAPL"
t2="MSFT"

start="2024-01-01"
lb=20
entry_z=2.0
stop_z=3.5

# data download
prices=yf.download([t1,t2],start=start)["Close"].dropna()
p1,p2=prices[t1],prices[t2]

# hedge ratio and spread calculation
hr=np.polyfit(p2,p1,1)[0]
spread=p1-hr*p2

# z-score calculation
mu=spread.rolling(lb).mean()
sigma=spread.rolling(lb).std()
z=(spread-mu)/sigma
z=z.shift(1).dropna()

# trading signals
sig=pd.Series(0,index=z.index)
sig[z>entry_z]=-1    # short spread
sig[z<-entry_z]=1    # long spread
sig[abs(z)>stop_z]=0 # emergency exit

# return calculation
r1=p1.pct_change()
r2=p2.pct_change()

str_ret=sig.shift(1)*(r1-hr*r2)
str_ret=str_ret.dropna()

eq_curve=(1+str_ret).cumprod()

# performance metrics
tdays=252
tot_ret=eq_curve.iloc[-1]-1
ann_vol=str_ret.std()*np.sqrt(tdays)
ann_ret=eq_curve.iloc[-1]**(tdays/len(eq_curve))-1
sharpe=ann_ret/ann_vol

print("Total Return:",round(tot_ret*100,2),"%")
print("Annualized Return:",round(ann_ret*100,2),"%")
print("Sharpe Ratio:",round(sharpe,2))

# visualization
plt.figure(figsize=(10,5))
plt.plot(eq_curve)
plt.title("Mean Reversion Pairs Trading Equity Curve")
plt.xlabel("Date")
plt.ylabel("Equity")
plt.show()
