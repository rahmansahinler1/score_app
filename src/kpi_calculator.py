import pandas as pd
import numpy as np

class KPICalculator:
    
    def __init__(self, df: pd.DataFrame, time_interval: int = 0):
        self.df = df
        self.time_interval = time_interval
    
    def calc_ma(self, df):
        """
        Calculate the moving average of the dataframe.

        Args:
            df (pd.DataFrame): The dataframe to calculate the moving average.
        """
        window = self.time_interval
        return self.df.rolling(window).mean()