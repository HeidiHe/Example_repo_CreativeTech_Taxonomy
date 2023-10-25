import json
 
# Opening JSON file
f = open('test_data.json')
data = json.load(f)
processedData = None

class EachLayer():
    # The class "constructor" - It's actually an initializer 
    def __init__(self, name, children):
        self.name = name
        self.children = children

    def __repr__(self):
        return f"<name:{self.name} children:{self.children}>"

# a recursive function that formats data into D3's hierachy
def format_data(curData):
    for eachKey in curData.keys():
        print(eachKey)
        # if curData has children
        if curData.get(eachKey):
            return EachLayer(eachKey, format_data(curData.get(eachKey)))
        else:
            finalData =  EachLayer(eachKey, "none")
            return finalData


processedData = format_data(data)
# print(repr(processedData))
print(processedData.__dict__)
# write nested class to json in python: https://www.geeksforgeeks.org/serialize-and-deserialize-complex-json-in-python/ 
final_data = json.dumps(processedData.__dict__, default=lambda o: o.__dict__, indent=4)
print(final_data)


# write to json
with open("processed_data.json", "w") as outfile:
    outfile.write(final_data)