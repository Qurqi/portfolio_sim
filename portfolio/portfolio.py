from typing import Dict
import pandas as pd
import yfinance as yf
import numpy as np
from datetime import datetime
from portfolio.stats import drawdown_analysis, win_loss_ratio, calculate_PnL
import time
import pickle 

class portfolio:

    def __init__(self,holdings: Dict = None,time_range: list = None):
        ##
        #  Initializes a portfolio object with the following attributes:
        #
        #  :param holdings: Dataframe storing the amount of a ticker held at each time instance. The ticker name is the column name, the date is the index, amount is the entry
        #  :param buy_sell: DataFrame containing B/S signals for each stock in the portfolio retrieved from the BackTesting Framework. 
        #                   Signals are formatted  as such: {'Date': [date],'Action': [signal],'Quantity': [quantity],'Price': [current_pred],'Ticker' : [ticker]}. NOTE: if sell, quantity is already negative.
        #  :param data: Dataframe containing a cap weighted index in the first column, and the closing price data for each stock held in the remaining columns. 'index' initialized to zero
        #  :param stats: DataFrame containing portfolio statistics such as maximum drawdown(dd_max), the corresponding recovery period(dd_rec), PnL, and Win Loss Ratio of each stock in the portfolio. Stat names are the indexes and ticker names are the column names
        #  :param date_range: date range of all holdings data
        ## 
        
        # check to see that time range is the right format (YYYY-MM-DD, YYYY-MM-DD)
        if time_range is None:
            exception = ValueError("time_range must be provided as a list containing the start and end dates in the format [YYYY-MM-DD, YYYY-MM-DD]")
            raise exception
        else:
            self.date_range = pd.date_range(start=time_range[0], end=time_range[1]) ## create date range for the portfolio based on the time_range input
        self.data = pd.DataFrame(0,columns = ['index'],index = self.date_range) # df of stock data. the first row contains an index of all stocks held. Index initialized to Zero
        self.station = pd.DataFrame(0,columns = ['index'], index = self.date_range)
        self.stats = pd.DataFrame() # append stats as we add them. ticker names are columns and indexes are corresponding stat.    

        if holdings is None: # Require user to input stocks and amounts
            self.holdings = pd.DataFrame(index=self.date_range)  # Initialize holdings DataFrame with zeros
        else: # intialize holdings DataFrame with amounts for each stock in columns, indexed over the given date range. 
            self.holdings = pd.DataFrame(index=self.date_range)  # Initialize holdings DataFrame with zeros
            self.update_portfolio(holdings)  # Initialize holdings DataFrame with the provided holdings dictionary

    def apply_signals(self,BS_signals: pd.DataFrame):
        '''
        Applies buy/sell signals to the portfolio's holdings DataFrame. 
        :param BS_signals: DataFrame containing B/S signals for each stock in the portfolio retrieved from the BackTesting Framework. 
                           Signals are formatted  as such: {'Date': [date],'Action': [signal],'Quantity': [quantity],'Price': [current_pred],'Ticker' : [ticker]}
        '''
        # Make a DF with tickers as columns, indexed over the date range of the portfolio
        # Fill in the df with signals.
        signals = self.convert_signals(BS_signals)  # Convert the buy/sell signals DataFrame into a signals DataFrame with tickers as columns, indexed over the date range of the portfolio
        print("Signals", signals)
        print("Holdings before applying signals", self.holdings)
        # add the signals to the holdings DataFrame, indexed over the date range of the portfolio
        self.holdings = self.holdings.add(signals, fill_value=0)
        print("Holdings after applying signals", self.holdings)
        # update index value with the new holdings DataFrame
        self.update_index()

    def convert_signals(self,BS_signals: pd.DataFrame):
        '''
        converts the buy_sell_signals DataFrame into a df of signals.
        
        '''
        # Make a signal Dataframe with tickers as columns, indexed over the date range of the portfolio
        signals = pd.DataFrame(0, columns = self.holdings.columns,index=self.date_range)  # Initialize signals DataFrame with zeros

        # at index date,ticker, if the action is buy or sell, add the quantity to the signals DataFrame
        for i in range(BS_signals.shape[0]):
            date = BS_signals.at[i, 'Date']
            ticker = BS_signals.at[i, 'Ticker']
            action = BS_signals.at[i, 'Action']
            quantity = BS_signals.at[i, 'Quantity']
            if action == 'buy' or action == 'sell': ## update quantity at date and all future dates
                # create a column vector of length date, self.date_range[-1] with the quantity to be added
                quantity_vector = pd.Series(quantity, index=self.date_range[self.date_range.get_loc(date):])
                #replace the quantity at the date and all future dates with the quantity vector
                signals[ticker] = signals[ticker].add(quantity_vector, fill_value=0)
            elif action == 'hold':
                pass
        return signals  # Return the signals DataFrame with the buy/sell signals applied
        
    def get_data(self,ticker: str):
        '''
        Initializes the portfolio's holdings data Dataframe from yfinance 
        :param ticker: ticker symbol to be added to the portfolio's data DataFrame
        '''
        ## Pull price data for each ticker and store in the data DataFrame
        price = yf.download(ticker, start= self.date_range[0], end=self.date_range[-1]) ## retrieve price data  
        tick_data = (price['Close'][ticker]).rename(ticker)  # Get the closing prices for the ticker
        self.data = pd.concat([self.data, tick_data], axis=1, join = 'inner')  # Insert the stock price into the DataFrame. Not that the inner merge will filter out non-trading days in date_range

    def update_data(self):
        '''
        Adjust data DataFrame to remove any ticker data for tickers that are no longer in the holdings DataFrame, and add any which are new.
        '''

        for ticker in list(self.data.columns): #for the data in the data frame, check if the ticker is in the updated holdings DataFrame. if not, remove data for that ticker
            if ticker not in list(self.holdings.columns) and ticker != 'index':  # If the ticker is not in the holdings DataFrame, remove it from the data DataFrame
                self.data.drop(ticker, axis=1, inplace=True)  # Remove the ticker data from the data DataFrame
        for ticker in list(self.holdings.columns): #for the holdings DataFrame, check if the ticker is in the data DataFrame. if not, add data for that ticker
            if ticker not in list(self.data.columns):  # If the ticker is not in the data DataFrame, add it
                self.get_data(ticker)  # Get the data for the ticker and add it to the data DataFrame

    def update_portfolio(self, update: Dict = None, BS_signals: pd.DataFrame = None):
        '''
        Updates the portfolio with a dictionary of ticker:amount pairs, where amount is the number of stocks the portolio shoud hold
        
        :param update: Dictionary containing ticker:amount pairs to update the portfolio holdings
        '''
        if update == None and BS_signals is None: # User must do one action
            exception = ValueError("You must provide either a dictionary of holding:amount pairs defining your portfolio's holdings or a DataFrame of buy/sell signals to update the portfolio")
            raise exception
        elif update is not None and BS_signals is not None: # User can do both actions in the order: Initialize holdings and then apply signals.
            self.update_holdings(update)
            self.update_index()
            self.update_stats()
            self.apply_signals(BS_signals)  
        elif update is None and BS_signals is not None:
            self.apply_signals(BS_signals)  # If BS_signals is provided, apply the signals to the portfolio
        elif update is not None and BS_signals is None:
            self.update_holdings(update)
            self.update_index()
            self.update_stats()

    def update_holdings(self, update: Dict): 
        '''   
        Updates the holdings dictionary with ticker:amount pairs in update dictionary 

        '''
        # update the holdings DataFrame with new ticker:amount pairs
        # remove any tickers that are not in the update dictionary, adjust amounts for existing tickers, and add new tickers from the update dictionary
        for ticker in list(self.holdings.columns): # if ticker is a current holding, check if it is in the update dictionary
            if ticker not in list(update.keys()): # if the ticker is not in the update dictionary, remove it from the holdings DataFrame
                self.holdings.drop(ticker, axis=1, inplace=True)
            if ticker in list(update.keys()): # if the ticker is in the update dictionary, update the amount held for that ticker
                self.holdings[ticker] = update[ticker]  # Update the amount held for the ticker

        for ticker in list(update.keys()): # if ticker is not a current holding, add it to the holdings DataFrame
            if ticker not in list(self.holdings.columns): 
                # make a dataframe column with the ticker name and the amount held, indexed over the date range
                new_ticker_data = pd.Series(update[ticker], index=self.date_range, name=ticker)  # Create a new Series for the ticker
                self.holdings = pd.concat([self.holdings, new_ticker_data], axis=1)  # Add the new ticker to the holdings DataFrame

    def update_index(self):
        '''
        Updates the index value

        '''  
        # update data with updated ticker data
        self.update_data()  # Get the latest data for the tickers in the holdings

        # given new holdings, update the index value by recalculating the capitalization weighted index
        #clear index column
        self.data['index'] = 0
        # recalculate index with new weights for holdings
        for ticker in list(self.holdings.columns):
            price = self.data[ticker]
            cap_weight = price.mul(self.holdings[ticker])
            self.data['index'] = self.data['index'].add(cap_weight)

    def plot_index(self):
        '''
        Plots the index value over time

        '''
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 5))
        plt.plot(self.data.index, self.data['index'], label='Portfolio Index')
        plt.title('Portfolio Index Over Time')
        plt.xlabel('Date')
        plt.ylabel('Index Value')
        plt.legend()
        plt.show()

    def update_stats(self):
        '''
        Updates the stats dictionary with new statistics 

        '''
        if self.stats.empty:  # If the stats DataFrame is empty, initialize it with the correct columns
            cols = ['index'] + list(self.holdings.columns)
            self.stats = pd.DataFrame(columns=cols)
            self.stats.fillna(0, inplace=True)
        
        drawdown_analysis(self)  # Perform drawdown analysis to update the stats DataFrame
        win_loss_ratio(self)  # Calculate the win/loss ratio and update the stats DataFrame
        
        pass

    def save_to_file(self, filename: str):
        """
        Saves the current portfolio instance to a local file using pickle.
        :param filename: Path to the file to save the portfolio.
        """
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_from_file(filename: str):
        """
        Loads a portfolio instance from a local file.
        :param filename: Path to the file containing the saved portfolio.
        :return: portfolio instance
        """
        with open(filename, 'rb') as f:
            return pickle.load(f)
