from src.data_reader import DataReader
from src.kpi_calculator import KPICalculator
import pathlib
import matplotlib.pyplot as plt

BASE_FOLDER  = pathlib.Path().resolve()  # Path for default output.

def main():
    # Select the folder
    csv_path = BASE_FOLDER.joinpath('data/btc_price_sample/BTC-2017min.csv')
    
    # Initialize DataReader and read data into a DataFrame
    reader = DataReader(csv_path)
    df = reader.read_csv()
    
    # Initialize KPICalculator with a custom time interval
    kpi_calculator = KPICalculator(df['open'], time_interval=14)
    
    # Calculate KPIs
    moving_avg = kpi_calculator.calc_ma(df)
    print()
    
    # You can now further analyze these KPIs or save them, etc.

if __name__ == '__main__':
    main()