import tushare as ts
import pandas as pd

def get_fut_daily(ts_code:str,save_path="D:\MyDesktop\techtrend-trader\data"):
    pro = ts.pro_api("7d3dbc65aa7da7f14128249745011c42a8c6ba1dd1c60f57313e91f7")
    df = pro.fut_daily(ts_code=ts_code)
    if save_path:
        df.to_csv(save_path, index=False)
    return df

def list_futures(exchange:str="SHFE"):
    pro = ts.pro_api("7d3dbc65aa7da7f14128249745011c42a8c6ba1dd1c60f57313e91f7")
    fut_list = pro.fut_basic(exchange=exchange)
    return fut_list[['ts_code','name']]
    pass
    