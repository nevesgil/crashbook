import requests

uri = "https://api.github.com/search/repositories?q=language:python&sort=stars"

headers = {"Accepted": "application/vnd.github.v3+json"}

r = requests.get(uri, headers=headers)

print(f"status code: {r.status_code}")

response_dict = r.json()

#

print(f"total items: {response_dict['total_count']}")
