import requests

query = input("What type of news are you interested in today? ")
api = "dbe57b028aeb41e285a226a94865f7a7" 
url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api}"

print(f"Fetching: {url}")
r = requests.get(url)
data = r.json()

if data.get('status') == 'ok':
    articles = data['articles']
    for index, article in enumerate(articles):
        print(f"{index + 1}. {article['title']}")
        print(article["url"])
        print("-" * 40)
else:
    print("\nERROR:")
    print(f"Code: {data.get('code')}")
    print(f"Message: {data.get('message')}")