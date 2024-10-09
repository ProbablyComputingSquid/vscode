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
    title = data["name"].center(WIDTH)    
    max_value = max(data["values"]) # max value in the values list
    max_category_string_length = max([len(category) for category in data["categories"]]) + 1 # max length of the categories to align properly
    # 1 is for the space
    print(title)
    print("-" * WIDTH)
    # print the bars and categories
    for category, value in zip(data["categories"], data["values"]):
        bar = "*" * int((value / max_value) * (WIDTH - max_category_string_length - 2))
        string_buffer = " " * (max_category_string_length - len(category))
        if value == max_value:
            print(f"{category}{string_buffer}| {bar.replace('***', '', 1)} {str(value)}")
        else:
            print(f"{category}{string_buffer}| {bar}{"" if value == max_value else " " + str(value)}")
    

data = {
        "name": "favorite fruits graph",
        "categories": ["apple","banana","cherry","date", "eggs and rasins"],
        "values": [9,2,5,3,1]
}
renderBarGraph(data)
# actual user input
print("example graph: ")
renderBarGraph(getInputs())
# fake data for testing LOL

