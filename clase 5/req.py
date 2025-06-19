import requests

pag = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(pag.json()["title"])