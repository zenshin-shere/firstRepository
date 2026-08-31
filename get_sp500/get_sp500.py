import yfinance as yf
import matplotlib.pyplot as plt

# S&P500のティッカーシンボルを設定 (^GSPC)
ticker = "^GSPC"

# 過去1年分の日足データを取得
# period: '1d', '5d', '1mo', '1y', 'max' など
# interval: '1m' (1分足), '1d' (日足), '1wk' (週足) など
df = yf.download(ticker, period="1y", interval="1d")

# データの先頭を表示
print(df.head())

# 終値 (Close) の推移をプロット
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Close'], label='S&P 500')
plt.title('S&P 500 Price History (1 Year)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.legend()
plt.show()