Items = {
    "Weapons": {
        "Swords": [],
        "Maces": [],
        "Spears": [],
        "Axes": [],
        "Knifes": [],
        "Rapier": [],
        "Bow": []
    },

    "Armor": {
        "Shields": [],
        "Helmet": [],
        "Breastplates": [],
        "Gloves": [],
        "Boots": [],
    },

    "Magic": {
        "Sticks": [],
        "Scrolls": [],
        "Leaves": []
    },

    "Accessories": {
        "Rings": [],
        "Amulets": []
    }}
# Оружие: сабля, Секира,

def CreateNewItem(type_name, Name, Damage=None, Speed=None, Scale=None, Type=None, word_ending=None):
    """Функция для создания предметов
    Пример использования: CreateNewItem(type_name={"Вид": "Weapons", "Подвид": "Сабля"}, Name="Сабля", Damage="2-4", Speed="6f", Scale="CB--", Type=["Режущий", "Одноручный", "Легкое"])"""
    if type_name["Вид"] in Items: # Проверка на правильный вид предмета

        if type_name["Вид"] == "Weapons":

            word_ending = word_ending # Для правильного русского окончания

            # Создания списка имён Матерьял + Название оружия
            Name_list = []
            materials = ["Деревянн", "Железн", "Бронзов", "Стальн", "Титанов"]
            for material in materials:
                Name_list.append(material + word_ending + " " + Name)

            # Создание списка растущего урона на каждый уровень оружия
            Damage_list = [f"{str(int(Damage[0]))}-{str(int(Damage[2]))}"]
            for Damage_scale in materials[1:]:
                Damage_list.append(f"{str(int(Damage[0])*2)}-{str(int(Damage[2])*2)}")

            Speed = Speed

            Type = Type

            Scale = Scale

            # Добавления в Items
            Items[ type_name["Вид"] ][ type_name["Подвид"] ] = []
            for i in range(len(materials)):
                Items[ type_name["Вид"] ][ type_name["Подвид" ]].append({"Name": Name_list[i], "Damage": Damage_list[i], "Speed": Speed, "Scale": Scale, "Type": Type, "Equipment": "Disable"})

        elif type_name["Вид"] == "Armors":
            pass
    else:
        print("Неправильно указан раздел")
        exit()




# Функция для добавления ID к предметам и создания id-карты
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

def init_Items():
    CreateNewItem(type_name={"Вид": "Weapons", "Подвид": "Сабли"}, Name="Сабля", Damage="2-4", Speed="6f", Scale="CB--", Type=["Режущий", "Одноручный", "Легкое"], word_ending="ая")

    Items["ID_Map"] = add_id_to_items(Items)

def get_Items(ID_Item):
    return Items["ID_Map"][ID_Item]

import json
def Save_Items(items):
    with open("config.json", "w") as file:
        json.dump(items, file, indent=2)

def Load_Items(items):
    with open("config.json", "r") as file:
        return json.load(file)

if __name__ == "__main__":
    pass

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
# ########################################################################################################################