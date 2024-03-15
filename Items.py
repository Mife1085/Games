Items = {'Weapons': {
    'Swords': [
        dict(Name="Деревянный Меч", Damage="2-4", Speed="8f", Type="Режущий/Одноручный", Equipment="Disable"),
        dict(Name="Бронзовый Меч", Damage="1-3", Speed="17f", Type="Режущий/Одноручный", Equipment="Disable"),
        dict(Name="Железный Меч", Damage="2-4", Speed="6f", Type="Режущий/Одноручный", Equipment="Disable"),
        dict(Name="Стальной Меч", Damage="3-5", Speed="22f", Type="Режущий/Одноручный", Equipment="Disable"),
        dict(Name="Титановый Меч", Damage="4-6", Speed="8f", Type="Режущий/Одноручный", Equipment="Disable")],
    'Maces': [
        dict(Name="Деревянная Дубина", Damage="1-5", Speed="10f", Type="Дробящий/Одноручная", Equipment="Disable"),
        dict(Name="Бронзовая Дубина", Damage="1-3", Speed="21f", Type="Дробящий/Одноручная", Equipment="Disable"),
        dict(Name="Железная Дубина", Damage="2-4", Speed="33f", Type="Дробящий/Одноручная", Equipment="Disable"),
        dict(Name="Стальная Дубина", Damage="3-5", Speed="8f", Type="Дробящий/Одноручная", Equipment="Disable"),
        dict(Name="Титановая Дубина", Damage="4-6", Speed="16f", Type="Дробящий/Одноручная", Equipment="Disable")],
    'Spears': [
        dict(Name="Деревянное Копьё", Damage="3-7", Speed="14f", Type="Колучиший/Двуручный", Equipment="Disable"),
        dict(Name="Бронзовое Копьё", Damage="1-3", Speed="38f", Type="Колучиший/Двуручный", Equipment="Disable"),
        dict(Name="Железное Копьё", Damage="2-4", Speed="23f", Type="Колучиший/Двуручный", Equipment="Disable"),
        dict(Name="Стальное Копьё", Damage="3-5", Speed="18f", Type="Колучиший/Двуручный", Equipment="Disable"),
        dict(Name="Титановое Копьё", Damage="4-6", Speed="28f", Type="Колучиший/Двуручный", Equipment="Disable")],
    'Axes': [
        dict(Name="Деревянный Топор", Damage="2-3", Speed="7f", Type="Режущий/Одноручный", Equipment="Disable"),
        dict(Name="Бронзовый Топор", Damage="1-3", Speed="15f", Type="Режущий/Одноручный", Equipment="Disable"),
        dict(Name="Железный Топор", Damage="2-4", Speed="5f", Type="Режущий/Одноручный", Equipment="Disable"),
        dict(Name="Стальной Топор", Damage="3-5", Speed="39f", Type="Режущий/Одноручный", Equipment="Disable"),
        dict(Name="Титановый Топор", Damage="4-6", Speed="21f", Type="Режущий/Одноручный", Equipment="Disable")],
    'Knifes': [
        dict(Name="Деревянный Нож", Damage="1-2", Speed="4f", Type="Колучиший/Одноручный", Equipment="Disable"),
        dict(Name="Бронзовый Нож", Damage="1-3", Speed="6f", Type="Колучиший/Одноручный", Equipment="Disable"),
        dict(Name="Железный Нож", Damage="2-4", Speed="11f", Type="Колучиший/Одноручный", Equipment="Disable"),
        dict(Name="Стальной Нож", Damage="3-5", Speed="15f", Type="Колучиший/Одноручный", Equipment="Disable"),
        dict(Name="Титановый Нож", Damage="4-6", Speed="22f", Type="Колучиший/Одноручный", Equipment="Disable")],
    'Rapier': [
        dict(Name="Деревянная Рапира", Damage="1-4", Speed="7f", Type="Колучиший/Одноручная", Equipment="Disable"),
        dict(Name="Бронзовая Рапира", Damage="1-3", Speed="37f", Type="Колучиший/Одноручная", Equipment="Disable"),
        dict(Name="Железная Рапира", Damage="2-4", Speed="9f", Type="Колучиший/Одноручная", Equipment="Disable"),
        dict(Name="Стальная Рапира", Damage="3-5", Speed="34f", Type="Колучиший/Одноручная", Equipment="Disable"),
        dict(Name="Титановая Рапира", Damage="4-6", Speed="6f", Type="Колучиший/Одноручная", Equipment="Disable")],
    'Bow': [
        dict(Name="Деревянный Лук", Damage="7-9", Speed="18f", Type="Дальний бой/Двуручный", Equipment="Disable"),
        dict(Name="Бронзовый Лук", Damage="1-3", Speed="12f", Type="Дальний бой/Двуручный", Equipment="Disable"),
        dict(Name="Железный Лук", Damage="2-4", Speed="15f", Type="Дальний бой/Двуручный", Equipment="Disable"),
        dict(Name="Стальной Лук", Damage="3-5", Speed="12f", Type="Дальний бой/Двуручный", Equipment="Disable"),
        dict(Name="Титановый Лук", Damage="4-6", Speed="21f", Type="Дальний бой/Двуручный", Equipment="Disable")]},
    'Armor': {
        "Shields": [],
        "Helmet": [],
        "Breastplates": [],
        "Gloves": [],
        "Boots": [],

    }, 'Magic': {
        "Sticks": [],
        "Scrolls": [],
        "Leaves": []
    }, 'Accessories': {
        "Rings": [],
        "Amulets": []
    }}

# import random
# Materials = ["Деревянный", "Бронзов", "Железный", "Стальной", "Титановый"]
# for item in Items["Weapons"]:
#     i = 0
#     while i < len(Materials):
#         Items["Weapons"][item].append({
#         "Name" : f"{Materials[i]} {item}", "Damage" : f"{i}-{i+2}", "Speed" : f"{random.randint(5, 40)}f",
#         "Type" : "Колучиший"})
#         i += 1
# print(Items["Weapons"])
id_list = []
for category in Items:
    for Item_type in Items[category]:
        for Item in Items[category][Item_type]:
            id_list.append(Item)
