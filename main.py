import pandas as pd
from portfolio import portfolio
from stats import drawdown_analysis

# Example Usage
if __name__ == "__main__":
    holdings = {'AAPL':7, 'MSFT':6, 'AMZN':2}

    buy_sell_signals = pd.DataFrame()

    pf = portfolio(holdings, buy_sell_signals)
    pf.make_index(['2020-01-01', '2023-01-01'])
    drawdown_analysis(pf)


