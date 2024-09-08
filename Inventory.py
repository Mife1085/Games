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
            self.inventory = player_inventory
        else:
            self.Load()

    def add_item(self, item_id):
        """Добавляет предмет в инвентарь, если есть место."""
        item = ItemsCollection.get_item_by_id(item_id)  # Получаем предмет по ID
        if len(self.inventory) < self.capacity:  # Проверяем, есть ли место в инвентаре
            self.inventory.append(item)  # Добавляем предмет в инвентарь
            print(f"Вы добавили '{item["Name"]}' в инвентарь.")
        else:
            print("Инвентарь полон! Не удалось добавить предмет.")

    def remove_item(self, item_id):
        """Удаляет предмет из инвентаря."""
        _item = self.inventory[item_id] # получение предмета по id
        if _item:  # Проверяем, есть ли предмет в инвентаре
            self.inventory.remove(_item)  # Удаляем предмет из инвентаря
            print(f"Вы удалили '{_item["Name"]}' из инвентаря.")
        else:
            print(f"Предмет '{_item}' не найден в инвентаре.")

    def Equipment(self, item_id):
        """Экипирует предмет, устанавливая его статус в 'Enable'."""
        _item = self.inventory[item_id] # получение предмета по id
        if _item:  # Проверяем, есть ли предметы в инвентаре
            _item["Equipment"] = "Enable"
        else:
            print("Предмет для удаления не найден")

    def show_inventory(self):
        """Отображает все предметы в инвентаре."""
        if self.inventory:
            print("-_-_-_-_-_-_-_-_-_-_-_Инвентарь_-_-_-_-_-_-_-_-_-_-_-")
            print("Оружие:")
            Weapon_item_id_list = []  # Список ID оружия
            Armor_item_id_list = []  # Список ID брони
            Enable_item_id_list = []  # Список ID экипированных предметов
            Other_item_id_list = []  # Список ID других предметов
            All_item = []
            # Перебираем предметы в инвентаре и классифицируем их
            for item in self.inventory:
                if item.get("Scale"):  # Проверяем, является ли предмет оружием
                    Weapon_item_id_list.append(item)
                    All_item.append(item)
                if item.get("Defens"):  # Проверяем, является ли предмет броней
                    Armor_item_id_list.append(item)
                    All_item.append(item)
                if item.get("Equipment") == "Enable":  # Проверяем, экипирован ли предмет
                    Enable_item_id_list.append(item)
                if item.get("Name"):  # Добавляем все предметы в список других
                    All_item.append(item)

            Other_item_id_list = [item for item in All_item if item not in Weapon_item_id_list + Armor_item_id_list + Enable_item_id_list]
            self.All_item_id_list = Weapon_item_id_list + Armor_item_id_list + Enable_item_id_list + Other_item_id_list


            text_name = []
            text_attribute = list(range(4))

            # Получение информации о
            print("Оружие:")
            attribute_list = []
            if Weapon_item_id_list:
                for item in Weapon_item_id_list:
                    text_name.append(item["Name"])
                    attribute_list.append(f'Урон: {item["Damage"]}')
                    attribute_list.append(f'Скорость: {item["Speed"]}')
                    attribute_list.append(f'Прирост: {item["Scale"]}')
                    attribute_list.append(f'Тип удара: {item["Type"]["Тип удара"]}')
                    attribute_list.append(f'Хват: {item["Type"]["Хват"]}')
                    attribute_list.append(f'Дистанция: {item["Type"]["Дистанция"]}')
                    attribute_list.append(f'Вес: {item["Type"]["Вес"]}')


                def set_attribute(self, name, attribute):
                    attribute_list.append(f'{name}: {item[attribute]}')


                text_attribute[0] = attribute_list

                        # print("-> " + text if self.choice_item == self.All_item_id_list.index(id) else text)
            else:
                text_attribute[0] = []
                print("Пусто")

            from pprint import pprint
            print(text_name)
            print(text_attribute)

            # Отображаем броню
            print("Броня:")
            attribute_list = []
            if Armor_item_id_list:
                for item in Armor_item_id_list:
                    text_name.append(item["Name"])
                    attribute_list.append(f'Защита: {item["Damage"]}')
                    if item.get("Speed"):
                        attribute_list.append(f'Скорость: {item["Speed"]}')
                    attribute_list.append(f'Вес: {item["Weight"]}')

                text_attribute[1] = attribute_list

            else:
                print("Пусто")
                text_attribute[1] = []

            # Отображаем другие предметы
            print("Прочее:")
            attribute_list = []
            if Other_item_id_list:
                for item in Other_item_id_list:
                    text_name.append(item["Name"])
                    # attribute_list.append(f'Описание: {item["Description"]}')
                    if item.get("Action"):
                        attribute_list.append(f'Использование: {item["Action"]}')

                text_attribute[2] = attribute_list
            else:
                print("Пусто")
                text_attribute[2] = []

            # Отображаем экипированные предметы
            print("Экипировано:")
            attribute_list = []
            if Enable_item_id_list:
                for item in Enable_item_id_list:
                    text_name.append(item["Name"])

                text_attribute[3] = attribute_list
            else:
                print("Пусто")
                text_attribute[3] = []

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

    def Save(self):
        with open("save.json", "w+", encoding='utf-8') as file:
            json.dump(self.inventory, fp=file, ensure_ascii=False, indent=4)

    def Load(self):
        """Загружает инвентарь из файла."""
        try:
            with open("save.json", "r+", encoding='utf-8') as file:
                self.inventory = json.load(fp=file)  # Загружаем инвентарь из JSON-файла
        except:
            self.inventory = []
    def id_map(self):
        for i in range(0, len(self.All_item_id_list) -1):
            print(self.All_item_id_list[i])

# Пример использования
if __name__ == "__main__":
    player_inventory = Inventory(player_inventory=[])
    # player_inventory.show_inventory()
    # player_inventory.Equipment(12)
    # player_inventory.Equipment(11)
    # player_inventory.Equipment(14)
    # player_inventory.Equipment(1)
    # player_inventory.show_inventory()
    # player_inventory.id_map()
    player_inventory.show_inventory()

########################################################################################################################
# Графика для show_inventory
# -> Деревянный Меч        | Урон: 3-4
# Железный Меч             | Скорость: 7f
# Броня:                   | Прирост: CE--
# Латный Щит               | Тип_удара: Режущий
# Титановый Шлем           | Хват: Одноручный
# Прочее:                  | Дистанция: Близко
# Пусто                    | Вес: Легкое
# Экипировано:             |
# Пусто                    |
