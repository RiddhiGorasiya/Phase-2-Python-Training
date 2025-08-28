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