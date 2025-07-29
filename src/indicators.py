import pandas as pd
import numpy as np
from ta.trend import MACD
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands

def add_indicators(df, window=14,ma_windows=[5,20]):
    # 移动平均线（MA）
    df['MA5'] = df['close'].rolling(window=5).mean()
    df['MA20'] = df['close'].rolling(window=20).mean()
    
    # 均线类
    for window in ma_windows:
        df[f'MA{window}'] = df['close'].rolling(window=window).mean()
    
    # RSI（相对强弱指数）
    df['RSI'] = RSIIndicator(df['close'], window=window).rsi()
    
    # MACD（移动平均收敛/发散指标）
    macd = MACD(df['close'])
    df['MACD'] = macd.macd_signal()
    
    # 布林带(Bollinger Bands)
    bb = BollingerBands(df['close'],window=20)
    df['BB_Upper'] = bb.bollinger_hband()
    df['BB_Lower'] = bb.bollinger_lband()
    
    return df