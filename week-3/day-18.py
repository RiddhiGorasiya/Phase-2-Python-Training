import requests
response = requests.get("https://www.geeksforgeeks.org/")
print(response.status_code)

# # get method
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

# authentication using python requests
import requests
from requests.auth import HTTPBasicAuth
response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('username', 'password'))
print(response.status_code) 

# SSL Certificate Verification
import requests
response = requests.get('https://expired.badssl.com/', verify=False)
print(response.status_code)

# providing a custom certificate
import requests
response = requests.get('https://github.com/', verify='/path/to/certfile')
print(response.status_code)


# session objects
import requests
s = requests.Session()  
session = s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')
print(r.text)

# error handling with requests
import requests 
try:
    response = requests.get("https://www.example.com/", timeout=5)
    response.raise_for_status()  
except requests.exceptions.HTTPError as http_errh:
    print("HTTP Error:", http_errh)
except requests.exceptions.ConnectionError as conn_errc:
    print("Error Connecting:", conn_errc)
except requests.exceptions.Timeout as time_errt:
    print("Timeout Error:", time_errt)
except requests.exceptions.RequestException as req_err:
    print("Something went wrong:", req_err)