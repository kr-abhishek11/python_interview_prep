import requests

response = requests.get("https://www.google.com")
print(response.text)

# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title":"Kumar Abhishek",
#     "body":"Python developer",
#     "userId": 11,
# }
# headers = {
#     'Content-type':'application/json',
#     'charset':'UTF-8',
# }
# response = requests.post(url,headers=headers,json=data)