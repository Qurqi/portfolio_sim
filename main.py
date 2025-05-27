import pandas as pd
from portfolio import Portfolio
from simulation import make_index
from stats import drawdown_analysis

# Example Usage
if __name__ == "__main__":
    holdings = {'AAPL': 10, 'MSFT': 5}
    index = {'index': 0}
    buy_sell_signals = pd.DataFrame()

    pf = Portfolio(holdings, index, buy_sell_signals)
    pf.add_stocks('GOOG', 7)

    make_index(pf.index, pf.index_cw, pf.index_per, pf.holdings, ['2022-01-01', '2022-12-31'])

    print("Holdings:", pf.holdings)
    print("Index:", pf.index)
    print("Cap Weights:", pf.index_cw)
    print("Index %:", pf.index_per)
