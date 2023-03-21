import requests

# Set the API endpoint and parameters
endpoint = "https://api.coindesk.com/v1/bpi/currentprice.json"
params = {"currency": "USD"}

# Make a request to the API
response = requests.get(endpoint, params=params)
data = response.json()

# Extract the current price of BTC
current_price = data["bpi"]["USD"]["rate_float"]

# Print the current price to the console
print(f"Current price: ${current_price:.2f}")
