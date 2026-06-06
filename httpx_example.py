import httpx

data = {"name": "Kirill", "age": 29}

r = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print(r.status_code)
print(r.json())