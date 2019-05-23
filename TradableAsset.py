import alpaca_trade_api as tradeapi

APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'
APCA_API_KEY_ID = 'PKP9WFN2NAA58WW9RIYJ'
APCA_API_SECRET_KEY = 'mi5ivAnq8DwD5GQp37jGxvKEO6ncHjCzgH7yzgHB'

api = tradeapi.REST(
    base_url=APCA_API_BASE_URL,
    key_id=APCA_API_KEY_ID,
    secret_key=APCA_API_SECRET_KEY
)

# Check if AAPL is tradable on the Alpaca platform.

asset = "AAPL"
try:
    aapl_asset = api.get_asset(asset)
    if aapl_asset.tradable:
        print("We can trade " + asset)
    else:
        print("We cannot trade " + asset)
except:
    print("Error finding " + asset)