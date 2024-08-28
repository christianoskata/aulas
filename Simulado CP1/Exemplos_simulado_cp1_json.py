import requests

# API 1
url= "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()

# API 2
pais = "Brasil"
url = f"https://restcountries.com/v3.1/name/{pais}"
response = requests.get(url)
data = response.json()

# API 3
url = "https://api.coingecko.com/api/v3/coins/list"
response = requests.get(url)
data = response.json()

nome_cripto = "bitcoin"
url = f"https://api.coingecko.com/api/v3/coins/{nome_cripto}"
response = requests.get(url)
data = response.json()