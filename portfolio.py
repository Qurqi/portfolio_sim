def __init__(self):
...
  pass

def add_stocks(tickers):
  """ 
  :Adds the quantity of a given ticker specified by the input dictionary
  
  """
  pass

def mk_index(stocks):
  """
  creates an index from the stock dictionary
  :
  """
  pass

def monte_sim():
  """
  Runs monte carlo sim for a given window into the future for given portfolio. 
  Returns dataframe with averaged outcome
  :param time: integer number of given time units to simulate. Defaults to 500.
  :param unit: string specifying unit of time for simulation. Options are {Monthly, Weekly, Daily, Hourly, Minutely}
               Defaults to daily if none specified.
  :param portfolio: portfolio object to simulate
  return monte_sim
  """
