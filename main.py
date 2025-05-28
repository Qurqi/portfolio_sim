import pandas as pd
from portfolio import portfolio
from stats import drawdown_analysis

# Example Usage
if __name__ == "__main__":
    holdings = {'AAPL': 10, 'MSFT': 5}
    buy_sell_signals = pd.DataFrame()

    pf = portfolio(holdings, buy_sell_signals)
    pf.add_stocks('GOOG', 7)

    portfolio.make_index(pf.index, pf.index_cw, pf.index_per, pf.holdings, ['2024-01-01', '2024-01-03'])

    print("Holdings:", pf.holdings)
    print("Index:", pf.index)
    print("Cap Weights:", pf.index_cw)
    print("Index %:", pf.index_per)
