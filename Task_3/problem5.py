
import json

try:
    with open("config.json") as file:
        print("System Ready")
        

except FileNotFoundError:
    with open("config.json","w") as file:
        json.dump({"volume": 50, "sleepTimer": 2},file)


        


