employee_dict = {"id" : 1, "name" : "name1", "salary" : 4235621}
print("This is Python", type(employee_dict))

print("\nNow Convert from Python to JSON")

import json
# Convert Python dict to JSON
json_object = json.dumps(employee_dict, indent=4)
print("Converted to JSON", type(json_object))
print(json_object)


