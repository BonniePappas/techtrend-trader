import pandas as pd

def generate_signals(df:pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # 初始化signal列
    df = generate_ma_signals(df)
    df = apply_indicator_filters(df)
    df.to_csv('data/signals.csv', index=False)
    
    return df

def apply_indicator_filters(df):
    for i in range(1,len(df)):
        if df.at[i,'signal'] == 'buy' and df.at[i,'RSI'] >70:
            df.at[i,'signal'] = 'hold'
        elif df.at[i,'signal'] == 'sell' and df.at[i,'RSI'] <30:
            df.at[i,'signal'] = 'hold'
            
    return df

def generate_ma_signals(df:pd.DataFrame) -> pd.DataFrame:
    df['signal'] = 'hold'
    buy_signal = (df['MA5'] > df['MA20']) & (df['MA5'].shift(1) <= df['MA20'].shift(1))
    sell_signal = (df['MA5'] < df['MA20']) & (df['MA5'].shift(1) >= df ['MA20'].shift(1))
    
    # 分别赋值
    df.loc[buy_signal,'signal'] = 'buy'
    df.loc[sell_signal,'signal'] = 'sell'
    
    return df