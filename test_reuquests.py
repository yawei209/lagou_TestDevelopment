
import requests

# r = requests.get("http://www.baidu.com") #使用get请求
# print(r.status_code)
# print(r.encoding)


r = requests.post("http://httpbin.org/post", data={'key':'value'})
print(r.text)