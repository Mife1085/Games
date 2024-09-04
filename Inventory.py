import json
import Items

# Создаем экземпляр коллекции предметов и загружаем данные
ItemsCollection = Items.ItemsCollection()
ItemsCollection.Load()

class Inventory:
    def __init__(self, player_inventory=[], capacity=10):
        # Инициализация инвентаря
        self.capacity = capacity  # Максимальное количество предметов в инвентаре
        self.choice_item = 0  # Индекс выбранного предмета
        self.All_item_id_list = []  # Список всех ID предметов в инвентаре

        # Если передан инвентарь игрока, используем его, иначе загружаем из источника
        if player_inventory:
            self.items = player_inventory
        else:
            self.Load()

    def add_item(self, item_id):
        """Добавляет предмет в инвентарь, если есть место."""
        item = ItemsCollection.get_item_by_id(item_id)  # Получаем предмет по ID
        if len(self.items) < self.capacity:  # Проверяем, есть ли место в инвентаре
            self.items.append(item)  # Добавляем предмет в инвентарь
            print(f"Вы добавили '{item}' в инвентарь.")
        else:
            print("Инвентарь полон! Не удалось добавить предмет.")

    def remove_item(self, item_id):
        """Удаляет предмет из инвентаря."""
        item = ItemsCollection.get_item_by_id(item_id)  # Получаем предмет по ID
        if item in self.items:  # Проверяем, есть ли предмет в инвентаре
            self.items.remove(item)  # Удаляем предмет из инвентаря
            print(f"Вы удалили '{item}' из инвентаря.")
        else:
            print(f"Предмет '{item}' не найден в инвентаре.")

    def Equipment(self, item_id):
        """Экипирует предмет, устанавливая его статус в 'Enable'."""
        if self.items:  # Проверяем, есть ли предметы в инвентаре
            self.items[self.items.index(ItemsCollection.get_item_by_id(str(item_id)))]["Equipment"] = "Enable"

    def show_inventory(self):
        """Отображает все предметы в инвентаре."""
        if self.items:
            print("-_-_-_-_-_-_-_-_-_-_-_Инвентарь_-_-_-_-_-_-_-_-_-_-_-")
            print("Оружие:")
            Weapon_item_id_list = []  # Список ID оружия
            Armor_item_id_list = []  # Список ID брони
            Enable_item_id_list = []  # Список ID экипированных предметов
            Other_item_id_list = []  # Список ID других предметов

            # Перебираем предметы в инвентаре и классифицируем их
            for item in self.items:
                if item.get("Scale"):  # Проверяем, является ли предмет оружием
                    Weapon_item_id_list.append(item.get("ID"))
                if item.get("Defens"):  # Проверяем, является ли предмет броней
                    Armor_item_id_list.append(item.get("ID"))
                if item.get("Equipment") == "Enable":  # Проверяем, экипирован ли предмет
                    Enable_item_id_list.append(item.get("ID"))
                if item.get("Name"):  # Добавляем все предметы в список других
                    Other_item_id_list.append(item.get("ID"))

            # Отображаем оружие
            if Weapon_item_id_list:
                for id in Weapon_item_id_list:
                    item = ItemsCollection.get_item_by_id(str(id))  # Получаем предмет по ID
                    text = f"""{item["Name"]} (Урон: {item["Damage"]}, Скорость: {item["Speed"]}, Прирост: {item["Scale"]}, Особенности: {item["Type"]})"""
                    print("-> " + text if self.choice_item == self.All_item_id_list.index(id) else text)
            else:
                print("Пусто")

            # Отображаем броню
            print("Броня:")
            if Armor_item_id_list:
                for id in Armor_item_id_list:
                    item = ItemsCollection.get_item_by_id(str(id))
                    if item.get("Speed"):
                        print(f"""{item["Name"]} (Защита: {item["Defens"]}, Скорость: {item["Speed"]}, Вес: {item["Weight"]})""")
                    else:
                        print(f"""{item["Name"]} (Защита: {item["Defens"]}, Вес: {item["Weight"]})""")
            else:
                print("Пусто")

            # Отображаем другие предметы
            print("Прочее:")
            if Other_item_id_list:
                for id in Other_item_id_list:
                    item = ItemsCollection.get_item_by_id(str(id))
                    print(item["Name"])
            else:
                print("Пусто")

            # Отображаем экипированные предметы
            print("Экипировано:")
            if Enable_item_id_list:
                for id in Enable_item_id_list:
                    print(ItemsCollection.get_item_by_id(str(id))["Name"])
            else:
                print("Пусто")

            print("____________________________________________")
        else:
            print("Ваш инвентарь пуст.")

    def Up(self):
        """Перемещает выбор предмета вверх."""
        self.choice_item -= 1 if self.choice_item >= 0 else 0  # Уменьшаем индекс выбранного предмета
        self.show_inventory()  # Обновляем отображение инвентаря
        return self.All_item_id_list[self.choice_item]  # Возвращаем выбранный предмет

    def Down(self):
        """Перемещает выбор предмета вниз."""
        self.choice_item += 1  # Увеличиваем индекс выбранного предмета
        self.show_inventory()  # Обновляем отображение инвентаря
        return self.All_item_id_list[self.choice_item]  # Возвращаем выбранный предмет

    def Load(self):
        """Загружает инвентарь из файла."""
        with open("save.json", "r") as file:
            self.items = json.load(file)["Player"]["Inventory"]  # Загружаем инвентарь из JSON-файла

# Пример использования
if __name__ == "__main__":
    player_inventory = Inventory()
