import alpaca_trade_api as tradeapi

api = tradeapi.REST(
    key_id='PKKIL5SU92G0EPHC3XM4',
    secret_key='bKo7pQBjCFgGcn/0gOv7yLV0O2gGyR4eFVgWVsNj',
    base_url='https://paper-api.alpaca.markets'
)

# Get the last 100 of our closed orders
closed_orders = api.list_orders(
    status='closed',
    limit=100
)

# Get only the closed orders for a particular stock
closed_aapl_orders = [o for o in closed_orders if o.symbol == 'AAPL']
print(closed_aapl_orders)