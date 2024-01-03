import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"


response = requests.get(url)  #will fetch response of the data
print("-------------Content---------------")
print(response.content) #will get you full body
print("-------------text---------------")
response_data = response.text #will get you full body which can be used for handling it
print(response_data)
print("--------------header----------------------")
print(response.headers) #will get you the header
print("--------------header-get----------------------")
print(response.headers.get("Date")) #fetch respective data from the header
print("--------------statusCode----------------------")
print(response.status_code) #gives you the status code
print("--------------elapsed time----------------------")
print(response.elapsed) #gives you the elapsed time
print("--------------json values----------------------")
json_response_data = json.loads(response_data) #json.loads will convert it to json
print("------------simple Json----------------------")
perpage = jsonpath.jsonpath(json_response_data,"per_page") # fetch respective details from the json via jsonpath
print(perpage)
print("------------Complex Json----------------------")
support_url = jsonpath.jsonpath(json_response_data,"support.url")# fetch respective details from the complex json via jsonpath
print(support_url[0])
print("------------Complex Json without jsonpath----------------------")
data = json_response_data["data"]
first_name = jsonpath.jsonpath(json_response_data, "data[0].first_name[]")
print("first name from first data is: {}".format(first_name[0]))

print("count is: {}" .format(data[0]))
print(data[0])
for x in data:
    print(x["first_name"])


