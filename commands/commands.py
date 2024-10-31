import yfinance as yf 
import pandas as pd 
import matplotlib.pyplot as plt

def get_stock_data(symbol):
    if symbol is None or symbol.strip() == "":
        return None

    stock = yf.Ticker(symbol)
    data = stock.history(period='5d')

    return data if not data.empty else None
    
def plot_comparison(data1, data2, symbol1, symbol2):

    plt.figure(figsize=(4, 4))
    plt.plot(data1.index, data1['Close'], marker='o', label=symbol1)
    plt.plot(data2.index, data2['Close'], marker='o', label=symbol2)
    plt.title(f'Comparacao de Precos - {symbol1} e {symbol2}')
    plt.xlabel('Data')
    plt.ylabel('Preco (R$)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.legend()
    plt.tight_layout()

    plot_path = f'static/plot_{symbol1}_{symbol2}.png'
    plt.savefig(plot_path)
    plt.close()
    return plot_path

def get_stock_list():

    tickers = ['PETR3.SA', 'VALE3.SA', 'ITUB4.SA', 'BBAS3.SA', 'B3SA3.SA', 
               'AMBP3.SA', 'WEGE3.SA', 'LREN3.SA', 'MGLU3.SA']
    
    stock_data = {}
    
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        stock_info = stock.info
        stock_data[ticker] = {
            'name': stock_info.get('longName', 'N/A'),
            'price': stock_info.get('currentPrice', 'N/A'),
            'market_cap': stock_info.get('marketCap', 'N/A')
        }
    
    return stock_data