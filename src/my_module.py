import pandas as pd
import os

def load_yfinance_data(folder_path):
    combined_df = pd.DataFrame()
    for file in os.listdir(folder_path):
        if file.endswith('.csv'):
            df = pd.read_csv(os.path.join(folder_path, file))
            df['Ticker'] = file.split('_')[0]  # Add ticker symbol from filename
            combined_df = pd.concat([combined_df, df], ignore_index=True)
    return combined_df

def load_news_data(folder_path):
            df = pd.read_csv(os.path.join(folder_path))
            return df