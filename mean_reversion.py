
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#ticker symbols for pairs trading
T1 = "AAPL"
T2 = "MSFT"

START_DATE = "2024-01-01"
LOOKBACK = 20
ENTRY_Z = 2.0
STOP_Z = 3.5

#data download
prices = yf.download([T1, T2], start=START_DATE)["Close"].dropna()
s1, s2 = prices[T1], prices[T2]

#hedge ratio and spread calculation

hedge_ratio = np.polyfit(s2, s1, 1)[0]
spread = s1 - hedge_ratio * s2

#z-score calculation

mu = spread.rolling(LOOKBACK).mean()
sigma = spread.rolling(LOOKBACK).std()
z_score = ((spread - mu) / sigma).shift(1)
z_score = z_score.dropna()

#reading signals

signals = pd.Series(0, index=z_score.index)
signals[z_score > ENTRY_Z] = -1     # short spread
signals[z_score < -ENTRY_Z] = 1     # long spread
signals[abs(z_score) > STOP_Z] = 0  # emergency exit

#return calculation

ret1 = s1.pct_change()
ret2 = s2.pct_change()

strategy_returns = signals.shift(1) * (ret1 - hedge_ratio * ret2)
strategy_returns = strategy_returns.dropna()

equity_curve = (1 + strategy_returns).cumprod()


#performance metrics

trading_days = 252
total_return = equity_curve.iloc[-1] - 1
annual_vol = strategy_returns.std() * np.sqrt(trading_days)
annual_return = equity_curve.iloc[-1] ** (trading_days / len(equity_curve)) - 1
sharpe = annual_return / annual_vol

print("Total Return:", round(total_return * 100, 2), "%")
print("Annualized Return:", round(annual_return * 100, 2), "%")
print("Sharpe Ratio:", round(sharpe, 2))

#visualization

plt.figure(figsize=(10, 5))
plt.plot(equity_curve)
plt.title("Mean Reversion Pairs Trading Equity Curve")
plt.xlabel("Date")
plt.ylabel("Equity")
plt.show()
