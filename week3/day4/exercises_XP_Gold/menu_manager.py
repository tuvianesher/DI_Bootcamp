import json

class MenuManager:
    def __init__(self):
        self.load_menu_from_file()

    def load_menu_from_file(self):
        with open("restaurant_menu.json") as file:
            self.menu = json.load(file)

    def add_item(self, name, price):
        new_item = {"name": name, "price": price}
        self.menu["items"].append(new_item)

    def remove_item(self, name):
        for item in self.menu["items"]:
            if item["name"] == name:
                self.menu["items"].remove(item)
                return True
        return False

    def save_to_file(self):
        with open("restaurant_menu.json", "w") as file:
            json.dump(self.menu, file, indent=4)
