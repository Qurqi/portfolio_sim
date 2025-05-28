
def drawdown_analysis(stats,index):
    '''
    Performs Drawdown Analysis to evaluate peak-to-trough declines in the portfolio.
    :param stats: Dictionary, containing the portfolio's maximum drawdown and corresponding recovery period, to be updated
    :param index: dict with Dataframe containing the index value at each time period.
    :return: updated 'stats' dict
    '''
    ## add statistics to stats dictionary if not present
    if 'dd_max' not in stats.keys():
      stats.update({'dd_max': 0})
    if 'dd_rec' not in stats.keys():
      stats.update({'dd_rec': 0})
    ## store index[0] as intial base value
    peak = index.get(index[0]) #store index value 0
    i_peak = 0
    
    for i in range(1,len(index)):
      
      ## Check for recovery time and calculate drawdown if so. Check all Positive slope line points 
      #  to see if they are greater than the peak as this is where the recovery happens.
      # 
      #   is (in[i-1] < in[i]) and (in[i+1] > in[i])? 
      #     is index.get(index[i]) > peak?
      #     
      #       if so, i - i_peak = dd_rec
      #   
      #       Compute Drawdown
      #   
      #       Find minumum index value between i_peak and i
      #       create sub data frame with index values between i_peak and i
      #       find min value in sub data frame
      #       set trough = min value
      #   
      #       dd = (peak - trough)*100/peak
      #   
      #       is dd > dd_max?
      #         if so, store this value as dd_max
      ##
      if (index.get(index[i-1]) < index.get(index[i])) and (index.get(index[i+1]) > index.get(index[i])):
        if index.get(index[i]) > peak:
          trough = min(index.get(index[i_peak:i]))
          dd = (peak - trough)*100/peak
          if dd > stats.get('dd_max'):
            dd_rec = i - i_peak
            stats.update({'dd_max' : dd})
            stats.update({'dd_rec' : dd_rec})
          
      ## Find local max. Find all points with negative concavity and check their relative heights
      #  
      #  is (in[i-1] < in[i]) and (in[i+1] < in[i])?
      #    is index.get(index[i]) > peak?
      #       if so, store this value as a peak and store i value(i_peak)
      #       set peak = index.get(index[i])
      ##
      if (index.get(index[i-1]) < index.get(index[i])) and (index.get(index[i+1]) < index.get(index[i])):
        if index.get(index[i]) > peak:
          peak = index.get(index[i])
          i_peak = i

def win_loss_ratio(self, buy_sell):
    '''
    Calculates the Win/Loss Ratio, comparing the number of winning trades to losing trades.
    :return : float: Win/Loss ratio value.
    '''

    pass
  
def calculate_PnL(stats,index,buy_sell):
      '''
      Profit & Loss (P&L): Track realized if we were to follow what this model predicts.

      :param index: Dataframe containing the index value at each time period.
      :param buy_sell: Dataframe containing the buy/sell signals at each time period.
      :return: float: Positive/Negative value if profit/loss was made at the end of this period
      '''

      pass
