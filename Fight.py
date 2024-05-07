import random

import Items

player1 = {
    "Player": {
        "Name": "Mile",

        "Statistics": {
            "Lv": 1,
            "Hp": 10,
            "Gold": 0,
            "Stats": [4, 3, 1, 2, 0, 0]  # Жиз, Сил, Лов, Вын, Инт, Удч
        },

        "Inventory": [
            Items.id_list[0], Items.id_list[2], Items.id_list[5], Items.id_list[23]

        ],

        "Info": {}
    }
}
player1["Player"]["Statistics"]["Hp"] = player1["Player"]["Statistics"]["Stats"][0] * 5

player2 = {
    "Player": {
        "Name": "Enemy",

        "Statistics": {
            "Lv": 1,
            "Hp": 10,
            "Gold": 0,
            "Stats": [4, 2, 4, 0, 0, 0]
        },
        "Inventory": [
            Items.id_list[0]
        ],

        "Info": {}
    }
}


def Random_stat(player, lv):  # Создание случайных стат за очки прокачки с уровня
    stat_time = list(range(6))

    player["Player"]["Statistics"]["Lv"] = lv  # разброс по уровню # random.randint(lv, lv+3)
    exp_point = player["Player"]["Statistics"]["Lv"] * 2  # очки прокачки (урв * очки прокачки за увр)
    i = 0
    while i != exp_point + 10:
        i = 0
        for stat_num in range(6):
            stat_time[stat_num] = player["Player"]["Statistics"]["Stats"][stat_num]
        for o in range(6):
            stat_time[o] += random.randint(0, int(2 + lv * 2 / 6))
            i += stat_time[o]
    player["Player"]["Statistics"]["Stats"] = stat_time
    player["Player"]["Statistics"]["Hp"] = player["Player"]["Statistics"]["Stats"][
                                               0] * 5  # Из стат хп в очки жизней персонажа


Random_stat(player1, 50)
Random_stat(player2, 50)


def Fight(player1, player2):
    print(player1["Player"]["Statistics"]["Stats"][1], player2["Player"]["Statistics"]["Stats"][1])  # check

    # Функции
    def Get_Damage_and_Defens(param, player=player1):

        for item in player["Player"]["Inventory"]:
            if param[:6] == "Damage":
                result = player["Player"]["Statistics"]["Stats"][1]
                if item.get("Damage") != None:
                    if item.get("Equipment") == "Enable":
                        if param == "Damage_const":
                            result += int(
                                (int(item.get("Damage")[0]) + int(item.get("Damage")[2])) / 2)  # cp. знач. урона оружия
                        elif param == "Damage":
                            result += random.randint(int(item.get("Damage")[0]), int(item.get("Damage")[2]))
                    else:
                        player["Player"]["Inventory"].append(dict(Name="Кулаки", Damage="1-2", Speed="5f", Type=["Дробящий", "Двуручный", "Невесомое"], Equipment="Enable"))
                    return result

            elif param == "Speed":
                if item.get("Speed") != None:
                    if item.get("Equipment") == "Enable":
                        return int(item.get("Speed")[:1])
                    else:
                        return 5

            elif param == "Type":
                if item.get("Type") != None:
                    if item.get("Equipment") == "Enable":
                        return item.get("Type")
                    else:
                        return "Невесомое"

            elif param == "Defens":
                result = player["Player"]["Statistics"]["Stats"][4]
                if item.get("Equipment") == "Enable":
                    if item.get("Защита") != None:
                        result += int(item.get("Защита")[0])
                return result
        print("Get_Damage_and_Defens сработала вне if: вывод 0")
        return 0

    Defens = [Get_Damage_and_Defens("Defens", player1), Get_Damage_and_Defens("Defens", player2)]

    def Show_status(_Frame):
        text_title_player = f"""
{player1["Player"]["Name"]} Lv {player1["Player"]["Statistics"]["Lv"]} 
HP: {player1["Player"]["Statistics"]["Hp"]} | Зщт {Defens[0] if Defens[0] >= 0 else 0} |  Урон {PDamage_const}| Увр: {(player1["Player"]["Statistics"]["Stats"][2] - player2["Player"]["Statistics"]["Stats"][2]) * 5 if ((player1["Player"]["Statistics"]["Stats"][2] - player2["Player"]["Statistics"]["Stats"][2]) * 5) >= 0 else 0}%"""
        text_title_enemy = f"""
{player2["Player"]["Name"]} Lv {player2["Player"]["Statistics"]["Lv"]} 
HP: {player2["Player"]["Statistics"]["Hp"]} | Зщт {Defens[1] if Defens[1] >= 0 else 0 } |  Урон {EDamage_const} | Увр: {(player2["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2]) * 5 if ((player2["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2]) * 5) >= 0 else 0}% """

        print(f"""
{text_title_player}
{Get_Damage_and_Defens("Speed", player1)}
       |‾‾‾‾‾|       
       | {_Frame} |
       |_____|

{text_title_enemy}
{Get_Damage_and_Defens("Speed", player2)}
1. Удар | 2. Движения | 3. Инвентарь | 4. Сбежать
""")
        if player1["Player"]["Statistics"]["Hp"] <= 0:
            print("Поражение")
            quit()
        if player2["Player"]["Statistics"]["Hp"] <= 0:
            print("Победа")
            quit()


    def Hit(_player1, _player2, _Frame=0):
        """Для расчёта урона от _player1 -> _player2"""
        nonlocal Combo_Num

        Show_status(_Frame)

        _hit = Get_Damage_and_Defens("Damage", _player1)
        HitStun = 10
        BlockStun = 2  # BlockStun-Вын/2
        Parry = 15
        MassInFrame = {
            "Невесомое оружие/Попадание" : 1,
            "Невесомое оружие/Промах" : -3,
            "Невесомое оружие/Парирование" : -8,
            "Легкое оружие/Попадание" : 4,
            "Легкое оружие/Промах" : -7,
            "Легкое оружие/Парирование" : -13,
            "Тяжёлое оружие/Попадание" : 11,
            "Тяжёлое оружие/Промах" : -10,
            "Тяжёлое оружие/Парирование" : 20}
        words = []
        _player1_is = 5_000_000
        if _player1 == player1:
            words = [f"Вы нанесли {_hit} урона Противнику, сломав его броню",
                     f"Вы нанесли {_hit} урона, повредив броню",
                     f"Вы нанесли {_hit} урона Противнику",
                     "Противник увернулся от атаки!"]
            _player1_is = 1

        elif _player1 == player2:
            words = [f"Вам нанесли {_hit} урона, сломав броню",
                     f"Вам нанесли {_hit} урона, но броня взяла урон на себя",
                     f"Вам нанесли {_hit} урона",
                     "Вы увернулся от атаки!"]
            _player1_is = 0
            _Frame = _Frame * -1

        player1_attack_type = Get_Damage_and_Defens("Type", _player1)
        player1_attack_speed = Get_Damage_and_Defens("Speed", _player1)

        if player1_attack_speed + _Frame > Get_Damage_and_Defens("Speed", _player2):
            Chance_To_Dodge = ((_player2["Player"]["Statistics"]["Stats"][2] - _player1["Player"]["Statistics"]["Stats"][2]) * 5)
            Chance_To_Dodge = 0 if Chance_To_Dodge < 0 else Chance_To_Dodge
            if random.randint(0, 100) <= 100 - Chance_To_Dodge:

                # Подсчёт массы для увелечения стана
                _MassInFrame = 0
                if player1_attack_type == "Невесомое":
                    _MassInFrame = MassInFrame["Невесомое оружие/Попадание"]
                elif player1_attack_type == "Легкое":
                    _MassInFrame = MassInFrame["Легкое оружие/Попадание"]
                elif player1_attack_type == "Тяжёлое":
                    _MassInFrame = MassInFrame["Тяжёлое оружие/Попадание"]
                # Комбо увеличивается HitStun уменьшается
                Combo_Num += 1
                _Frame -= - player1_attack_speed
                _Frame += int(HitStun-(Combo_Num*5)) + _MassInFrame

                if Defens[_player1_is] > 0:
                    Defens[_player1_is] -= _hit
                    if Defens[_player1_is] <= 0:
                        print(words[0])
                        # точка интереса При поломке брони
                    else:
                        print(words[1])
                else:
                    _player2["Player"]["Statistics"]["Hp"] -= _hit
                    print(words[2])
            else:
                if player1_attack_type == "Невесомое":
                    _Frame += MassInFrame["Невесомое оружие/Промах"]       # -3f
                elif player1_attack_type == "Легкое":
                    _Frame += MassInFrame["Легкое оружие/Промах"]          # -7f
                elif player1_attack_type == "Тяжёлое":
                    _Frame += MassInFrame["Тяжёлое оружие/Промах"]         # -10f
                print(words[3])
        elif player1_attack_speed + Frame == Get_Damage_and_Defens("Speed", _player2):
            print("Клинч!!!")
            quit()
        else:
            print(f'Frame : {_Frame}   Huuuuuuuuuui ')
            Combo_Num = 0
            if _player1_is == 0:
                Player_Move(_Frame)
            else:
                Enemy_move(_Frame*(-1))
        if _player1_is == 1:
            Player_Move(_Frame)
        else:
            Enemy_move(_Frame*(-1))

    def Enemy_move(_Frame):
        """Возможности противника"""
        nonlocal Frame
        Frame = _Frame
        Hit(player2, player1, _Frame)


    # check
    print(player1["Player"]["Inventory"])
    for item in player1["Player"]["Inventory"]:
        print(item)
    print("End_________________________________________")

    # Проверка на наличия одетой экипировки
    Get_Damage_and_Defens("Damage_con1st", player1)
    Get_Damage_and_Defens("Damage_const", player2)

    PDamage_const = Get_Damage_and_Defens("Damage_const", player1)  # cp. знач. урона Игрока
    Defens[0] = Get_Damage_and_Defens("Defens", player1)

    EDamage_const = Get_Damage_and_Defens("Damage_const", player2)
    Defens[1] = Get_Damage_and_Defens("Defens", player2)

    Player_Dice_num = random.randint(player1["Player"]["Statistics"]["Lv"],
                                     player1["Player"]["Statistics"]["Lv"] + player1["Player"]["Statistics"]["Stats"][
                                         2])
    Enemy_Dice_num = random.randint(player2["Player"]["Statistics"]["Lv"],
                                    player2["Player"]["Statistics"]["Lv"] + player2["Player"]["Statistics"]["Stats"][2])
    text_title_player = f"""{player1["Player"]["Name"]} Lv {player1["Player"]["Statistics"]["Lv"]} 
HP: {player1["Player"]["Statistics"]["Hp"]} | Зщт {Defens[0]} |  Урон {PDamage_const}| Увр: {(player1["Player"]["Statistics"]["Stats"][2] - player2["Player"]["Statistics"]["Stats"][2]) * 5 if ((player1["Player"]["Statistics"]["Stats"][2] - player2["Player"]["Statistics"]["Stats"][2]) * 5) >= 0 else 0}%"""
    text_title_enemy = f""" {player2["Player"]["Name"]} Lv {player2["Player"]["Statistics"]["Lv"]} 
HP: {player2["Player"]["Statistics"]["Hp"]} | Зщт {Defens[1]} |  Урон {EDamage_const} | Увр: {(player2["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2]) * 5 if ((player2["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2]) * 5) >= 0 else 0}% """
    print(f"""
{text_title_player}

        |‾‾‾‾‾|        |‾‾‾‾‾|
        |  {Player_Dice_num}  |  -VS-  |  {Enemy_Dice_num}  |
        |_____|        |_____|
{text_title_enemy}""")
    # console временная переменная
    console = None
    while not (console == "1" or console == "2"):
        console = input("Выберите\n1. Сражaться | 2. Сбежать\n: ")

    Fight_or_Escape = True
    while Fight_or_Escape:

        if console == "1":
            Fight_now = True
            Frame = 5
            Combo_Num = 0
            # Frame = Player_Dice_num - Enemy_Dice_num

            while Fight_now:
                def Player_Move(Frame):
                    Show_status(Frame)

                    console = input(": ")
                    if console == "1":
                        # Идея фреймов в буфере порядка действий. При +0 фреймов. Действие игрока Удар -> нож (7 фреймов)
                        # и Действии противника Удар Кувалдой (10 ф.) Число общих фреймов становиться -7. Игрок наносит
                        # удар и снова выбирает действие. Выбор падает на перекат в сторону (4). Игрок не успевает и
                        # получат урон и минус по общим фреймам

                        return Hit(player1, player2, Frame)
                        # Enemy_move()

                    elif console == "2":
                        pass

                    elif console == "3":
                        pass

                    elif console == "4":
                        Fight_now = False
                        console = "2"

                    else:
                        pass  # ciu()

                Frame = Player_Move(Frame)



        elif console == "2":
            escape = (player1["Player"]["Statistics"]["Stats"][2] - player2["Player"]["Statistics"]["Stats"][
                2]) * 5 if ((player1["Player"]["Statistics"]["Stats"][2] - player2["Player"]["Statistics"]["Stats"][
                    2]) * 5) >= 0 else 0
            print(f"Шанс сбежать: {escape}%")
            if random.randint(0, 100) >= 100 - escape:
                print("Вы избежали сражения")
                Fight_or_Escape = False
            else:
                print("Вы не смогли сбежать")
                console = "1"
                Fight_now = False
                # Enemy_move(Frame)
        else:
            pass  # ciu()


Fight(player1, player2)
