import json
import Items
ItemsCollection = Items.ItemsCollection()
ItemsCollection.Load()

class Inventory:

    def __init__(self, capacity=10):
        self.capacity = capacity  # Максимальное количество предметов в инвентаре
        with open("save.json", "r") as file:
            self.items = json.load(file)["Player"]["Inventory"] # Список для хранения предметов

    def add_item(self, item):
        """Добавляет предмет в инвентарь, если есть место."""
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"Вы добавили '{item}' в инвентарь.")
        else:
            print("Инвентарь полон! Не удалось добавить предмет.")

    def remove_item(self, item):
        """Удаляет предмет из инвентаря."""
        if item in self.items:
            self.items.remove(item)
            print(f"Вы удалили '{item}' из инвентаря.")
        else:
            print(f"Предмет '{item}' не найден в инвентаре.")

    def Equipment(self, item_id):
        if self.items:
            self.items[ self.items.index( ItemsCollection.get_item_by_id( str(item_id) ) ) ]["Equipment"] = "Enable"

    def show_inventory(self):
        """Отображает все предметы в инвентаре."""
        if self.items:
            print("Ваш инвентарь:")

            Weapon_item_id_list = []
            Armor_item_id_list = []
            Other_item_id_list = []
            Enable_item_id_list = []
            for item in self.items:
                if item.get("Scale"):
                    Weapon_item_id_list.append(item.get("ID"))
                if item.get("Defens"):
                    Armor_item_id_list.append(item.get("ID"))
                # if item.get(pass):
                #     Other_item_id_list.append(item.get("ID"))
                if item.get("Equipment") == "Enable":
                    Enable_item_id_list.append(item.get("ID"))

            print("-_-_-_-_-_-_-_-_-_-_-_Инвентарь_-_-_-_-_-_-_-_-_-_-_-")
            print("Оружие:")
            for id in Weapon_item_id_list:
                print(ItemsCollection.get_item_by_id(str(id)))
            print("Броня:")
            for id in Armor_item_id_list:
                print(ItemsCollection.get_item_by_id(str(id)))
            print("Прочее:")
            # for id in Enable_item_id_list:
            #     print(ItemsCollection.get_item_by_id(str(id)))
            print("____________________________________________")
            print("Экипировано:")
            for id in Enable_item_id_list:
                print(ItemsCollection.get_item_by_id(str(id)))
        else:
            print("Ваш инвентарь пуст.")

# Пример использования
if __name__ == "__main__":
    player_inventory = Inventory()
    player_inventory.Equipment(1)
    # # Добавление предметов
    # player_inventory.add_item("Меч")
    # player_inventory.add_item("Щит")
    # player_inventory.add_item("Зелье здоровья")

    # Отображение инвентаря
    player_inventory.show_inventory()

    # Удаление предмета
    # player_inventory.remove_item("Щит")

