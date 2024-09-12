
# Оружие: сабля, Секира,
import json
class ItemsCollection(object):
    
    def __init__(self):
        self.Items = {
            "Weapons": {
                "Swords": [], # Мечи
                "Sabers": [], # Сабли
                "Maces": [],  # Булавы
                "Spears": [], # Копья
                "Axes": [],   # Топоры
                "Knifes": [], # Ножи
                "Rapier": [], # Рапиры
                "Bow": []     # Луки
            },

            "Armor": {
                "Shields": [],      # Щиты
                "Helmet": [],       # Шлем
                "Breastplates": [], # Нагрудники
                "Gloves": [],       # Перчатки
                "Boots": [],        # Ботинки
            },

            "Magic": {
                "Sticks": [],  # Палочки
                "Scrolls": [], # Свитки
                "Leaves": []   # Листья
            },

            "Accessories": {
                "Rings": [],  # Кольца
                "Amulets": [] # Амулеты
            }}

    def CreateNewItem(self, type_name, Name, Damage=None, Speed=None, Scale=None, Type=None, Defens=None, word_ending=None):
        """Функция для создания предметов
        Пример использования: self.CreateNewItem(type_name={"Вид": "Weapons", "Подвид": "Сабля"}, Name="Сабля", Damage="2-4", Speed="6f", Scale="CB--", Type=["Режущий", "Одноручный", "Легкое"])"""
        if type_name["Вид"] in self.Items: # Проверка на правильный вид предмета

            if type_name["Вид"] == "Weapons":

                word_ending = word_ending # Для правильного русского окончания

                # Создания списка имён Матерьял + Название оружия
                Name_list = []
                materials = ["Деревянн", "Железн", "Бронзов", "Стальн", "Титанов"]
                for material in materials:
                    Name_list.append(material + word_ending + " " + Name)

                Name_list[3] = "Стальной " + Name

                # Создание списка растущего урона на каждый уровень оружия
                Damage_list = [f"{str(int(Damage[0]))}-{str(int(Damage[2]))}"]
                for Damage_scale in range(1, len(materials[1:])+1):
                    Damage_list.append(f"{str(int(Damage[0])*2*Damage_scale)}-{str(int(Damage[2])*2*Damage_scale)}")

                Speed = Speed

                Type = Type

                Scale = Scale

                # Добавления в self. Items
                self.Items[ type_name["Вид"] ][ type_name["Подвид"] ] = []
                for i in range(len(materials)):
                    self.Items[ type_name["Вид"] ][ type_name["Подвид" ]].append({"Name": Name_list[i], "Damage": Damage_list[i], "Speed": Speed, "Scale": Scale, "Type": Type, "Equipment": "Disable"})

            elif type_name["Вид"] == "Armor":

                word_ending = word_ending # Для правильного русского окончания

                # Создания списка имён Матерьял + Название оружия
                Name_list = []
                materials = ["Кожан", "Кольчужн", "Латн", "Стальн", "Титанов"]
                for material in materials:
                    Name_list.append(material + word_ending + " " + Name)

                Name_list[3] = "Стальной " + Name

                Weight_list = ["Легкие", "Легкие", "Средние", "Средние", "Тяжёлые"]

                Defens_bonus = range(1, 6)

                Defens = Defens


                self.Items[ type_name["Вид"] ][ type_name["Подвид"] ] = []
                for i in range(len(materials)):
                    self.Items[ type_name["Вид"] ][ type_name["Подвид" ]].append({"Name": Name_list[i], "Defens": Defens*Defens_bonus[i], "Weight": Weight_list[i], "Equipment": "Disable"})


        else:
            print("Неправильно указан раздел")
            exit()

    # Функция для добавления ID к предметам и создания id-карты
    @staticmethod
    def add_id_to_items(items):
        global_id = 1  # Начинаем с 1
        id_mapping = {}  # Словарь для хранения ID и предметов

        for category, subcategories in items.items():
            for subcategory, item_list in subcategories.items():
                for item in item_list:
                    item["ID"] = global_id  # Присваиваем глобальный ID
                    id_mapping[global_id] = item  # Сохраняем предмет в словаре по ID
                    global_id += 1  # Увеличиваем глобальный ID на 1

        return id_mapping  # Возвращаем словарь ID и предметов

    def init(self):
        # Создание оружия

        self.CreateNewItem(type_name={"Вид": "Weapons", "Подвид": "Swords"}, Name="Меч", Damage="3-4", Speed="7f", Scale="CE--", Type={"Тип удара": "Режущий", "Хват": "Одноручный", "Дистанция": "Близко", "Вес": "Легкое"}, word_ending="ый")
        self.CreateNewItem(type_name={"Вид": "Weapons", "Подвид": "Sabers"}, Name="Сабля", Damage="2-4", Speed="6f", Scale="DC--", Type={"Тип удара": "Режущий", "Хват": "Одноручный", "Дистанция": "Близко", "Вес": "Легкое"}, word_ending="ая")
        self.CreateNewItem(type_name={"Вид": "Weapons", "Подвид": "Maces"}, Name="Булова", Damage="3-4", Speed="8f", Scale="B---", Type={"Тип удара": "Дробящий", "Хват": "Одноручный", "Дистанция": "Близко", "Вес": "Тяжёлое"}, word_ending="ая")
        self.CreateNewItem(type_name={"Вид": "Weapons", "Подвид": "Spears"}, Name="Копьё", Damage="4-7", Speed="10f", Scale="DD--", Type={"Тип удара": "Колющий", "Хват": "Двуручный", "Дистанция": "Средняя", "Вес": "Тяжёлое"}, word_ending="ое")
        self.CreateNewItem(type_name={"Вид": "Weapons", "Подвид": "Axes"}, Name="Топор", Damage="3-5", Speed="6f", Scale="C---", Type={"Тип удара": "Режущий", "Хват": "Одноручный", "Дистанция": "Близко", "Вес": "Легкое"}, word_ending="ый")
        self.CreateNewItem(type_name={"Вид": "Weapons", "Подвид": "Knifes"}, Name="Кинжал", Damage="1-3", Speed="4f", Scale="EB--", Type={"Тип удара": "Режущий/Колющий", "Хват": "Одноручный", "Дистанция": "Близко", "Вес": "Невесомое"}, word_ending="ый")
        self.CreateNewItem(type_name={"Вид": "Weapons", "Подвид": "Rapier"}, Name="Рапира", Damage="3-5", Speed="6f", Scale="-B--", Type={"Тип удара": "Колющий", "Хват": "Одноручный", "Дистанция": "Близко", "Вес": "Легкое"}, word_ending="ая")
        self.CreateNewItem(type_name={"Вид": "Weapons", "Подвид": "Bow"}, Name="Лук", Damage="6-8", Speed="14f", Scale="ED--", Type={"Тип удара": "Колющий", "Хват": "Двуручный", "Дистанция": "Дальняя", "Вес": "Легкое"}, word_ending="ый")

        # Создание брони
        self.CreateNewItem(type_name={"Вид": "Armor", "Подвид": "Shields"}, Name="Щит", Defens=5, Speed="5f", word_ending="ый")
        self.CreateNewItem(type_name={"Вид": "Armor", "Подвид": "Helmet"}, Name="Шлем", Defens=5, word_ending="ый")
        self.CreateNewItem(type_name={"Вид": "Armor", "Подвид": "Breastplates"}, Name="Нагрудник", Defens=7, word_ending="ый")
        self.CreateNewItem(type_name={"Вид": "Armor", "Подвид": "Gloves"}, Name="Перчатка", Defens=2, word_ending="ая")
        self.CreateNewItem(type_name={"Вид": "Armor", "Подвид": "Boots"}, Name="Ботинок", Defens=4, word_ending="ый")

        self.Items["ID_Map"] = self.add_id_to_items(self.Items)

    def get_item_by_id(self, ID_Item):
        return self.Items["ID_Map"][str(ID_Item)]


    def Save(self, items):
        with open("config.json", "w", encoding='utf-8') as file:
            json.dump(items, fp=file, ensure_ascii=False, indent=4)

    def Load(self):
        with open("config.json", "r", encoding='utf-8') as file:
            self.Items = json.load(file)
            return self.Items

if __name__ == "__main__":
    Items = ItemsCollection()
    # Items.Load()
    Items.init()
    Items.Save(Items.Items)


    # Inv = [Items.get_item_by_id(1), Items.get_item_by_id(2), Items.get_item_by_id(43), Items.get_item_by_id(50)]
    # print(json.dumps(Inv, indent=2))

# Items_GPT = {
#     "Accessories": {
#         "Ring": [
#             dict(
#                 Name="Кольцо Силы", Effect="+2 к Силе", Type="Ring", Equipment="Enable"
#             ),
#             dict(
#                 Name="Кольцо Удачи",
#                 Effect="+5% шанс критического удара",
#                 Type="Ring",
#                 Equipment="Enable",
#             ),
#         ],
#         "Amulet": [
#             dict(
#                 Name="Амулет Защиты",
#                 Effect="+3 к Защите",
#                 Type="Amulet",
#                 Equipment="Enable",
#             ),
#         ],
#     },
#     "Magic items": {
#         "Potion": [
#             dict(
#                 Name="Зелье Здоровья",
#                 Effect="Восстанавливает 50 HP",
#                 Type="Consumable",
#                 Equipment="Disable",
#             ),
#             dict(
#                 Name="Зелье Маны",
#                 Effect="Восстанавливает 30 MP",
#                 Type="Consumable",
#                 Equipment="Disable",
#             ),
#         ],
#         "Scroll": [
#             dict(
#                 Name="Свиток Огненного Шара",
#                 Effect="Наносит 20 урона огнем",
#                 Type="One-time",
#                 Equipment="Disable",
#             ),
#             dict(
#                 Name="Свиток Лечения",
#                 Effect="Восстанавливает 40 HP",
#                 Type="One-time",
#                 Equipment="Disable",
#             ),
#         ],
#     },
# }
#
# Items_GPT2 = {
#     "Accessories": {
#         'Ring': [
#             dict(Name="Кольцо Силы", Effect="+2 к Силе", Type="Ring", Equipment="Enable"),
#             dict(Name="Кольцо Удачи", Effect="+5% шанс критического удара", Type="Ring", Equipment="Enable"),
#             dict(Name="Кольцо Защиты", Effect="+3 к Защите", Type="Ring", Equipment="Enable"),
#             dict(Name="Кольцо Мудрости", Effect="+2 к Интеллекту", Type="Ring", Equipment="Enable"),
#         ],
#         'Amulet': [
#             dict(Name="Амулет Защиты", Effect="+3 к Защите", Type="Amulet", Equipment="Enable"),
#             dict(Name="Амулет Силы", Effect="+2 к Силе", Type="Amulet", Equipment="Enable"),
#             dict(Name="Амулет Здоровья", Effect="+50 HP", Type="Amulet", Equipment="Enable"),
#             dict(Name="Амулет Удачи", Effect="+5% шанс критического удара", Type="Amulet", Equipment="Enable"),
#         ],
#     },
#     "Magic items": {
#         'Potion': [
#             dict(Name="Зелье Здоровья", Effect="Восстанавливает 50 HP", Type="Consumable", Equipment="Disable"),
#             dict(Name="Зелье Маны", Effect="Восстанавливает 30 MP", Type="Consumable", Equipment="Disable"),
#             dict(Name="Зелье Силы", Effect="Увеличивает силу на 5 на 10 минут", Type="Consumable", Equipment="Disable"),
#             dict(Name="Зелье Защиты", Effect="Увеличивает защиту на 5 на 10 минут", Type="Consumable", Equipment="Disable"),
#         ],
#         'Scroll': [
#             dict(Name="Свиток Огненного Шара", Effect="Наносит 20 урона огнем", Type="One-time", Equipment="Disable"),
#             dict(Name="Свиток Лечения", Effect="Восстанавливает 30 HP", Type="One-time", Equipment="Disable"),
#             dict(Name="Свиток Защиты", Effect="Увеличивает защиту на 5 на 5 минут", Type="One-time", Equipment="Disable"),
#             dict(Name="Свиток Молнии", Effect="Наносит 25 урона молнией", Type="One-time", Equipment="Disable"),
#         ],
#     }
# }
#
#######################################################################################################################