import pandas as pd

class DataReader:
    def __init__(self, path: str):
        self.path = path
    
    def read_csv(self):
        """
        Read csv file from the path.
        """
        return pd.read_csv(self.path)
    