from src.fetch_data import get_fut_daily, list_futures
from src.visualize import plot_candlestick, plot_equity_and_return
from src.trend import generate_signals
from src.backtest import backtest
from src.indicators import add_indicators
import pandas as pd

def main():
    # 1.获取数据
    df = get_fut_daily("AO2507.SHF", save_path="data/AO2507.csv")
    
    # 2.添加技术指标
    df = add_indicators(df)
    
    # 3.可视化原始数据
    plot_candlestick(df)
    
    # 4.生成信号并回测
    df_with_signals = generate_signals(df)
    backtest_result = backtest(df_with_signals)
    
    # 5.保存和可视化结果
    backtest_result.to_csv("data/backtest_result.csv", index=False)
    plot_equity_and_return(backtest_result)
    
if __name__ == "__main__":
    main()