import alpaca_trade_api as tradeapi

api = tradeapi.REST(
    key_id='PKKIL5SU92G0EPHC3XM4',
    secret_key='bKo7pQBjCFgGcn/0gOv7yLV0O2gGyR4eFVgWVsNj',
    base_url='https://paper-api.alpaca.markets'
)

# Submit a market order and assign it a Client Order ID.
###
api.submit_order(
    symbol='AAPL',
    qty=1,
    side='buy',
    type='market',
    time_in_force='gtc',
    client_order_id='my_first_order'
)

# Get our order using its Client Order ID.
my_order = api.get_order_by_client_order_id('my_first_order')
print('Got order #{}'.format(my_order.id))