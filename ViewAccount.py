import alpaca_trade_api as tradeapi

APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'
APCA_API_KEY_ID = 'PKP9WFN2NAA58WW9RIYJ'
APCA_API_SECRET_KEY = 'mi5ivAnq8DwD5GQp37jGxvKEO6ncHjCzgH7yzgHB'

api = tradeapi.REST(
    base_url=APCA_API_BASE_URL,
    key_id=APCA_API_KEY_ID,
    secret_key=APCA_API_SECRET_KEY
)

# Get our account information.
account = api.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))