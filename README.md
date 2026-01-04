# Mean Reversion Pairs Trading (AAPL / MSFT)

This project executes a straightforward **mean reversion–based pairs trading strategy** utilizing historical price data from AAPL and MSFT.

The aim of this project is **educational and research-focused**: to comprehend the mechanics, assumptions, and limitations associated with statistical arbitrage strategies.

---

## Strategy Overview

- Two correlated stocks: **AAPL** and **MSFT**
- Hedge ratio determined through linear regression
- Spread standardized via a rolling **Z-score**
- Trades initiated when Z-score surpasses ±2
- Construction of a market-neutral position
- Clear avoidance of look-ahead bias

---

## Core Concepts Used

- Normalization of hedge ratio
- Rolling mean and standard deviation calculations
- Signal generation based on Z-score
- Hypothesis of mean reversion
- Returns that are market-neutral

---

## How It Works

1. Acquire historical closing prices
2. Estimate the hedge ratio to adjust for differences in price scale
3. Calculate the spread between the two assets
4. Standardize the spread using a rolling Z-score
5. Create long/short signals based on Z-score thresholds
6. Calculate market-neutral returns and the equity curve

---

## Performance Metrics

The script provides reports on:
- Total return
- Annualized return
- Sharpe ratio
- Visualization of the equity curve

---

## Limitations

- Absence of transaction costs or slippage
- Static hedge ratio
- Lack of formal cointegration testing
- Performance of the strategy is dependent on market regimes

This implementation is **not designed for live trading**.

---

## Possible Improvements

- Conducting cointegration tests (ADF / Johansen)
- Implementing dynamic hedge ratios
- Modeling transaction costs
- Performing walk-forward validation
- Sizing positions based on risk

---

## Disclaimer

This project is intended for **educational and research purposes only**.
It should not be interpreted as financial advice.
