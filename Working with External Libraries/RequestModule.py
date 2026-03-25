import requests

r = requests.get(
    "https://www.python.org/",
    headers={"User-Agent": "Mozilla/5.0"})

print(r.text)



