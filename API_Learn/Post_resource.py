import requests
import json
import jsonpath

url = "https://reqres.in/api/users"
file_content = open('..\project_resources\jsonread.json', 'r')
json_request = json.loads(file_content.read())

response = requests.post(url,json_request)

print(response.status_code)

json_response = json.loads(response.text)
print(json_response)
print(jsonpath.jsonpath(json_response, "id"))

actual_name = jsonpath.jsonpath(json_response, "name")
assert actual_name[0] == "morpheus","{} is not matching".format(actual_name)


