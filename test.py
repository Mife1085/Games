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
        if not self.inventory:
            print("Инвентарь пуст.")
            return

        categorized_items = {
            "Оружие": [],
            "Броня": [],
            "Экипированные": [],
            "Прочие": []
        }

        # Классификация предметов
        for item in self.inventory:
            if item.get("Scale"):
                categorized_items["Оружие"].append(item)
            elif item.get("Defens"):
                categorized_items["Броня"].append(item)
            if item.get("Equipment") == "Enable":
                categorized_items["Экипированные"].append(item)

        categorized_items["Прочие"] = [
            item for item in self.inventory if item not in
            categorized_items["Оружие"] + categorized_items["Броня"] + categorized_items["Экипированные"]
        ]

        # Функция для создания словаря свойств предметов
        def create_item_properties_dict(item_list):
            properties_dict = {}
            for item in item_list:
                item_name = item.get("Name", "Без названия")
                attributes = [
                    f"Урон: {item.get('Damage')}",
                    f"Скорость: {item.get('Speed')}",
                    f"Прирост: {item.get('Scale')}",
                    f"Защита: {item.get('Defens')}",
                    f"Вес: {item.get('Weight')}"
                ]

                # Добавляем свойства из Type, если они существуют
                if "Type" in item:
                    for key, value in item["Type"].items():
                        attributes.append(f"{key}: {value}")

                # Фильтруем пустые свойства
                properties_dict[item_name] = [attr for attr in attributes if attr.split(": ")[1] != 'None']
            return properties_dict

        # Функция для отображения предметов

#
#
#


        # Выводим информацию о классах предметов
        print("""
|*                                 *|
|*         ___Инвентарь___         *|
|*                                 *|
""")
        title_category_list = list(categorized_items.keys())
        items_category_list = list(categorized_items.values())
        num_main = 0
        for num_main in range(len(title_category_list)):
            print(title_category_list[num_main]) # Оружие

            text_title_items = []
            how_many_items = len(items_category_list[num_main]) # Кол-во в списке предметов в категории Оружие
            # Создания списка с названиями предметов
            [text_title_items.append(
                f'{items_category_list[num_main][number]["Name"]} {" "*(25-len(items_category_list[num_main][number]["Name"]))}| ')
                for number in range(how_many_items)]

            name_attribute_items = [
                ["Урон", "Скорость", "Прирост"],
                ["Защита", "Вес"],
                [],
                []
            ]
            value_attribute_items = []

            attributes = list(items_category_list[num_main][0].values())


            for item_attribute_index in range(1, len(name_attribute_items)+1):
                value_attribute_items.append(f"{attributes[item_attribute_index]}")

            if num_main == 0:
                for key, value in attributes[4].items():
                    name_attribute_items[0].append(key)
                    value_attribute_items.append(value)
                value_attribute_items.pop(3)

            for name in text_title_items:
                print(name)

            # print(title + ":")
            # if items:
            #
            #     print(f" ->{items['Name']}" if items['Name'] == list(items[])[self.choice_item] else f"{items['Name']}")
            #     for prop in properties:
            #         print(f"             {prop}")
            #     print()  # Отделяем предметы пустой строкой
            # else:
            #     print("Пусто")
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

# Реализация
#print("_—"*19)
#print("_—"*5 + "Инвентарь" + "_—"*5)
#print("_—"*19)
#
#
#
# for num1, num2 in zip(range(len(text_name)), range(len(text_attribute))):
#    space = 10
#    space -= len(text_name[num1])
#    if choice_item == text_name[num1]:
#       space -= 2
#       print("->" + text_name[num1] + ":" + " "*space + "| " + text_attribute[num1][num2])
#
#    print(text_name[num1] + ":" + " "*space + "| " + text_attribute[num1][num2])
#
