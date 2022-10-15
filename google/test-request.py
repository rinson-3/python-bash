import requests

response=requests.get("https://www.google.com/")
len(response.text)