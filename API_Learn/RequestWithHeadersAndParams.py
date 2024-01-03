import requests

uri = "https://httpbin.org/get"
header ={"tasks":"love","priority":"low"}
params = {"option":"12","pname":"unknown","type":"tasks"}

response = requests.get(uri, headers=header, params=params)

print(response.text)
print(response.status_code)
