import rate_limiter
import requests

alpha_vantage_rate_limiter = rate_limiter.RateLimiter(max_calls=5, period=60)

for __ in range(10):
    response = alpha_vantage_rate_limiter(requests.get, 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=demo')
    print(response.json()['Meta Data']['3. Last Refreshed'])
