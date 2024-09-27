import os
WIDTH = os.get_terminal_size().columns
HEIGHT = os.get_terminal_size().lines
def getInputs():
    data = {
        "name": "",
        "categories": [],
        "values": []
    }
    data["name"] = input("Enter name of the graph: ")
    while True:
        try:
            category = input("Enter category: ")
            value = float(input("Enter value: "))
        except ValueError:
            print("Value must be a number")
            continue
        #print("this happened")
        data["categories"].append(category)
        data["values"].append(value)
        if input("Do you want to add more categories? (y/n): ") == "n":
            return data
def renderBarGraph(data):
    # data should be in dictionary format
    text = data["name"].center(WIDTH)
    print(text)
    
    max_value = max(data["values"])
    max_category_string_length = max([len(category) for category in data["categories"]])
    print("-" * WIDTH)
    for category, value in zip(data["categories"], data["values"]):
        bar = "*" * int((value / max_value) * (WIDTH - max_category_string_length - 2))
        string_buffer = " " * (max_category_string_length - len(category))
        print(f"{category}{string_buffer}| {bar}")
    

data = {
        "name": "test",
        "categories": ["apple","banana","cherry","date"],
        "values": [6,2,5,9]
}
renderBarGraph(getInputs())
#renderBarGraph(data)
