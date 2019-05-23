import alpaca_trade_api as tradeapi
import datetime

api = tradeapi.REST(
    key_id='PKKIL5SU92G0EPHC3XM4',
    secret_key='bKo7pQBjCFgGcn/0gOv7yLV0O2gGyR4eFVgWVsNj',
    base_url='https://paper-api.alpaca.markets'
)

# Check if the market is open now.
clock = api.get_clock()
print('The market is {}'.format('open.' if clock.is_open else 'closed.'))

# Check when the market was open on Dec. 1, 2018
date = '2018-12-01'
calendar = api.get_calendar(start=date, end=date)[0]
print('The market opened at {} and closed at {} on {}.'.format(
    calendar.open,
    calendar.close,
    date
))