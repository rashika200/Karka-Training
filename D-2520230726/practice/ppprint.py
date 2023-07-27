from urllib import request
s=request.urlopen("https://jsonplaceholder.typicode.com/users")
json_s=s.read()
import json
users=json.loads(json_s)
# print(users)
for user in users:
    print(user)