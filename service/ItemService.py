item_info = []

class Item:
    name = ""
    weight = ""

def inser_item(name,weight):
    item = Item()
    item.name = name
    item.weight = weight
    item_info.append(item)

def print_item():
    for item in item_info:
        print(item.name + " " + item.weight)
