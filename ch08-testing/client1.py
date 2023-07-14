import requests

response = requests.get('http://localhost:8080/events')
events = response.json()
for e in events:
    print(e)

payload= {"title": "New events", "image": "new_event.png", "description": "This is a new event", "tags": ["new_event"], "location": "Bangsar"}

res = requests.post('http://localhost:8080/events/create', json=payload)
print(res.text)