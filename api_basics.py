import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.text)
data = response.json()
print(data)
print(type(data))
if response.status_code == 200:
    print(data["title"])
else:
    print("Request failed") 
