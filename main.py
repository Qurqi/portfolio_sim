import pandas as pd
from portfolio import portfolio
from stats import drawdown_analysis

# Example Usage
if __name__ == "__main__":

    holdings = {'AAPL':7, 'MSFT':6, 'AMZN':2}
    # create buy sell signals
    signals = pd.DataFrame(columns=['Date', 'Action', 'Quantity', 'Price', 'Ticker'])
    signals = pd.DataFrame({
        'Date': ['2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05'],
        'Action': ['buy', 'sell', 'buy', 'sell'],
        'Quantity': [10, 5, 15, 10],
        'Price': [150, 155, 160, 165],
        'Ticker': ['AAPL', 'AAPL', 'MSFT', 'MSFT']
    })
    pf = portfolio(time_range=['2020-01-01', '2023-01-01'])
    pf.update_portfolio(holdings)
    pf.plot_index()
    pf.apply_signals(signals)
    pf.plot_index()

    
   


