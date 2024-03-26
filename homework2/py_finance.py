import yfinance as yf
from datetime import datetime

def fetch_stock_info(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        current_datetime = datetime.now().strftime("%a %b %d %H:%M:%S %Z %Y")
        company_name = info.get('longName')
        current_price = info.get('regularMarketPrice')
        previous_close = info.get('previousClose')

        if current_price is not None and previous_close is not None:
            change = current_price - previous_close
            change_percent = (change / previous_close) * 100
            change_str = f"+{change:.2f}" if change > 0 else f"{change:.2f}"
            change_percent_str = f"+{change_percent:.2f}%" if change_percent > 0 else f"{change_percent:.2f}%"
        else:
            change_str = "N/A"
            change_percent_str = "N/A"

        print(current_datetime)
        print(f"{company_name} ({symbol})")
        print(f"{current_price if current_price is not None else 'N/A'} {change_str} ({change_percent_str})")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    symbol = input("Please enter a symbol:\n")
    fetch_stock_info(symbol)
