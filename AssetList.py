import alpaca_trade_api as tradeapi

api = tradeapi.REST(
    key_id='PKKIL5SU92G0EPHC3XM4',
    secret_key='bKo7pQBjCFgGcn/0gOv7yLV0O2gGyR4eFVgWVsNj',
    base_url='https://paper-api.alpaca.markets'
)

# Get a list of all active assets.
active_assets = api.list_assets(status='active')

# Filter the assets down to just those on NASDAQ.
nasdaq_assets = [a for a in active_assets if a.exchange == 'NASDAQ']
for i in nasdaq_assets:
    print(i)