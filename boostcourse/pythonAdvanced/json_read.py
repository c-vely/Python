import json

with open("json_ex.json", "r", encoding="utf8") as f:
    contents = f.read()
    json_data = json.loads(contents)

print(type(json_data))
print(json_data["employees"])

for employee in json_data["employees"]:
    print(employee)


for employee in json_data["employees"]:
    print(employee["lastName"])
