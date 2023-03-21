import pandas as pd
from datetime import datetime, timedelta

def load_data():
    # Load Bitcoin price data
    df = pd.read_csv('btc_price_data.csv', index_col=0, parse_dates=True)

    # Resample to hourly data
    df = df.resample('H').ffill()

    # Interpolate missing data
    df.interpolate(inplace=True)

    # Add market dynamics data
    news = pd.read_csv('news_data.csv', index_col=0, parse_dates=True)
    social = pd.read_csv('social_data.csv', index_col=0, parse_dates=True)
    df = pd.concat([df, news, social], axis=1)

    # Scale data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(df.values)

    return scaled_data, scaler

def create_sequences(data, seq_length):
    x = []
    y = []
    for i in range(len(data)-seq_length-1):
        seq = data[i:(i+seq_length), :]
        label = data[i+seq_length, :]
        x.append(seq)
        y.append(label)
    return np.array(x), np.array(y)
