import yfinance as yf

def make_index(index, index_cw, index_per, holdings, time_range):
    for ticker in holdings:
        price = yf.download(ticker, start=time_range[0], end=time_range[1])['Adj Close'].iloc[-1]
        cap_weight = price * holdings.get(ticker, 0)
        index_cw[ticker] = cap_weight
        index["index"] = index.get("index", 0) + cap_weight

    for ticker in index_cw:
        index_per[ticker] = index_cw[ticker] * 100 / index["index"]

def run_monte_carlo(sim_length, portfolio):
    print(f"Running Monte Carlo for {sim_length} steps on portfolio: {portfolio.holdings}")

def past_data_sim(buy_sell, index):
    print("Simulating based on past buy/sell signals (placeholder)")

def monte_carlo_sim():
    print("Simulating future based on Monte Carlo (placeholder)")
