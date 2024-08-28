import json

# Изначальный список предметов
Items = {
    "Weapons": {
        'Bow': [],
        'Sword': [],
        'Axe': [],
    },
    "Armor": {
        'Helmet': [],
        'Chestplate': [],
        'Boots': [],
    },
    "Accessories": {
        'Ring': [],
        'Amulet': [],
    },
    "Magic items": {
        'Potion': [],
        'Scroll': [],
    }
}

def add_item(category, item_type, item_attributes):
    """Добавляет новый предмет в указанную категорию и тип."""
    if category in Items and item_type in Items[category]:
        Items[category][item_type].append(item_attributes)
        print(f"Добавлен предмет: {item_attributes}")
    else:
        print("Категория или тип предмета не найдены.")

def display_items():
    """Выводит текущий список предметов."""
    print(json.dumps(Items, indent=4, ensure_ascii=False))

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить новый предмет")
        print("2. Показать все предметы")
        print("3. Выход")
        choice = input("Введите номер действия: ")

        if choice == '1':
            category = input("Введите категорию (Weapons, Armor, Accessories, Magic items): ")
            item_type = input("Введите тип предмета (например, Bow, Sword, Helmet): ")
            name = input("Введите имя предмета: ")
            damage = input("Введите урон (если применимо): ")
            defense = input("Введите защиту (если применимо): ")
            weight = input("Введите вес (если применимо): ")
            effect = input("Введите эффект (если применимо): ")
            item_attributes = {
                "Name": name,
                "Damage": damage if damage else None,
                "Defense": defense if defense else None,
                "Weight": weight if weight else None,
                "Effect": effect if effect else None,
                "Equipment": "Enable"  # или "Disable" в зависимости от логики игры
            }
            add_item(category, item_type, item_attributes)

        elif choice == '2':
            display_items()

        elif choice == '3':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()