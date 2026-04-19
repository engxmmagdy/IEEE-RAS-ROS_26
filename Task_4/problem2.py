

import json
data = {"orange":5, "apple":4, "tomato":3}

def save_inventory(data):
    with open("items.json","w") as file:
        json.dump(data,file)



def read_inventory():
    try:
        with open("items.json","r") as file:
            read = json.load(file)
        return read
    except json.JSONDecodeError:
        return {}

save_inventory({"data":6})
print(read_inventory())


