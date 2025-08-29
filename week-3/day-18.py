import requests
response = requests.get("https://www.geeksforgeeks.org/")
print(response.status_code)

# get method
import requests
response = requests.get("https://github.com/RiddhiGorasiya/Phase-2-Python-Training.git")
print(response.status_code)
print(response.text)
# with open("demo.py", "w") as f: #add requests to file
#     f.write(response.text)
# print(response.content) #bytes of data

# post method
import requests
r = requests.post("https://httpbin.org/post", data = {'key':'value'})
print(r.text) 
print(r.json())

# put method
import requests
r = requests.put("https://httpbin.org/put", data = {'a': 1, 'b': 2})
print("Stsatus code:", r.status_code)
print("Response Body:", r.content.decode())

# delete method
import requests 
r = requests.delete("https://httpbin.org//delete", data = {'key': 'value'})
print(r) 
print(r.json())

# head method
import requests
r = requests.head("https://httpbin.org/get", data = {'key': 'value'})
print(r)
print(r.headers)
print(r.content)

# patch method
import requests
r = requests.patch("https://httpbin.org/patch", data = {'key': 'value'}) 
print(r)
print(r.content) 

# response object
import requests
response = requests.get('https://api.github.com/')
print(response.url)
print(response.status_code)  

