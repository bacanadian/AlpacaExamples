import alpaca_trade_api as tradeapi

api = tradeapi.REST(
    key_id='PKKIL5SU92G0EPHC3XM4',
    secret_key='bKo7pQBjCFgGcn/0gOv7yLV0O2gGyR4eFVgWVsNj',
    base_url='https://paper-api.alpaca.markets'
)

# Get our position in AAPL.
aapl_position = api.get_position('AAPL')

# Get a list of all of our positions.
portfolio = api.list_positions()

# Print the quantity of shares for each position.
for position in portfolio:
    print("{} shares of {}".format(position.qty, position.symbol))