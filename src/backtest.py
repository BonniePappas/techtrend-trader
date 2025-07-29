import pandas as pd
import numpy as np 

# 十万本金进行模拟
def backtest(df, initial_cash=100000.0, fee=0.001, verbose=True):
    df = df.copy()
    df['position'] = 0
    df['cash'] = 0.0
    df['hold_value'] = 0.0
    df['total_value'] = initial_cash
    
    cash = initial_cash
    position = 0
    entry_price = 0
    
    for i in range(len(df)):
        signal = df.iloc[i]['signal']
        price = df.iloc[i]['close']
        
        # 开仓
        if signal == 'buy' and position == 0:
            entry_price = price * (1 + fee)
            position = int(cash/ entry_price)
            cash -= position * entry_price
        
        # 平仓
        elif signal == 'sell' and position > 0:
            exit_price = price * (1 - fee)
            cash += position * exit_price
            position = 0
            
        hold_value = position * price if position > 0 else 0
        total_value = cash + hold_value

        df.at[df.index[i], 'position'] = position
        df.at[df.index[i], 'cash'] = cash
        df.at[df.index[i], 'hold_value'] = hold_value
        df.at[df.index[i], 'total_value'] = total_value
    
    if verbose:
        print_summary(df)
        
    return df

def print_summary(df):
    # 计算总收益率和最大回撤
    total_return = (df['total_value'].iloc[-1] / df['total_value'].iloc[0]) - 1
    max_drawdown = (calculate_max_drawdown(df['total_value']))
    print(f'Total Return:{total_return*100:2f}%')
    print(f'Max Drawdown:{max_drawdown*100:2f}%')
    
def calculate_max_drawdown(series):
    roll_max = series.cummax()
    drawdown = (series - roll_max) / roll_max
    return drawdown.min()
