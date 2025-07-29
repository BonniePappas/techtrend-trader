import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio
from plotly.subplots import make_subplots

pio.renderers.default = 'browser'

def prepare_date_column(df):
    df = df.copy()
    df['trade_date'] = pd.to_datetime(df['trade_date'], format='%Y%m%d')
    df = df.sort_values(by='trade_date')
    return df

def plot_candlestick(df:pd.DataFrame,ma_windows=[5,20]):
    df = prepare_date_column(df)
    
    #构建k线图    
    fig = go.Figure()
    
    fig.add_trace(go.Candlestick(
        x=df['trade_date'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
        name='Candlestick'
    ))
    
    #叠加均线图
    for window in ma_windows:
        fig.add_trace(go.Scatter(
            x=df['trade_date'],
            y=df[f'MA{window}'],
            mode='lines',
            name=f'MA{window}'
        ))
    
    # 美化图表
    fig.update_layout(
        title='Candlestick Chart',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis_rangeslider_visible=False,
        template='plotly_white'
    )    
    
    fig.show()
    
    # return df
    
def plot_equity_and_return(df):
    df = prepare_date_column(df)
    
    df['scaled_equity'] = df['total_value']/df['total_value'].iloc[0]
    
    df['daily_return'] = df['total_value'].pct_change()
    df = df.dropna(subset=['total_value','daily_return'])
    
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
    
    #资金曲线（上图）
    fig.add_trace(go.Scatter(
        x=df['trade_date'],
        y=df['scaled_equity'],
        line=dict(color='blue'),
        name='Equity Curve'
    ), row=1,col=1)
    
    #日收益率（下图）
    fig.add_trace(go.Scatter(
        x=df['trade_date'],
        y=df['daily_return'],
        line=dict(color='orange'),
        name='Daily Return'
    ), row=2, col=1)
    
    fig.update_layout(height=600, title_text='Separate Views')
    fig.show()