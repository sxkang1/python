import requests
# pillow
response = requests.get('http://www.baidu.com/')
print(response.text)