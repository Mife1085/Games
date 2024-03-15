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
    print(player1["Player"]["Statistics"]["Stats"][1], player2["Player"]["Statistics"]["Stats"][1])  # ?

    def Enemy_move(PDefens, EDefens):
        """Возможности противника"""

        Hit = Get_Damage_and_Defens("Damage", player2)

        Hero_escape = (player1["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2]) * 5 if ((player1["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2]) * 5) >= 0 else 0  # проверить
        if random.randint(0, 100) <= 100 - Hero_escape:
            if PDefens > 0:
                PDefens -= Hit
                if PDefens <= 0:
                    print(f"Вам нанесли {Hit} урона, сломав броню")
                else:
                    print(f"Вам нанесли {Hit} урона, но броня взяла урон на себя")
            else:
                player1["Player"]["Statistics"]["Hp"] -= Hit
                print(f"Вам нанесли {Hit} урона")
        else:
            print("Вы увернулся от атаки!")

        return PDefens

    # check
    print(player1["Player"]["Inventory"])
    for item in player1["Player"]["Inventory"]:
        print(item)
    print("End_________________________________________")

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
                    return result

            elif param == "Defens":
                result = player["Player"]["Statistics"]["Stats"][4]
                if item.get("Equipment") == "Enable":
                    if item.get("Защита") != None:
                         result += int(item.get("Защита")[0])
                return  result
        print("Get_Damage_and_Defens сработала вне if: вывод 0")
        return 0

    PDamage_const = Get_Damage_and_Defens("Damage_const", player1)  # cp. знач. урона Игрока
    PDefens = Get_Damage_and_Defens("Defens", player1)

    EDamage_const = Get_Damage_and_Defens("Damage_const", player2)
    EDefens = Get_Damage_and_Defens("Defens", player2)

    Player_Dice_num = random.randint(player1["Player"]["Statistics"]["Lv"],
                                     player1["Player"]["Statistics"]["Lv"] + player1["Player"]["Statistics"]["Stats"][
                                         2])
    Enemy_Dice_num = random.randint(player2["Player"]["Statistics"]["Lv"],
                                    player2["Player"]["Statistics"]["Lv"] + player2["Player"]["Statistics"]["Stats"][2])

    print(
        f"""
{player1["Player"]["Name"]} Lv {player1["Player"]["Statistics"]["Lv"]} 
HP: {player1["Player"]["Statistics"]["Hp"]} | Зщт {PDefens} |  Урон {PDamage_const}| Увр: {(player1["Player"]["Statistics"]["Stats"][2] - player2["Player"]["Statistics"]["Stats"][2]) * 5 if ((player1["Player"]["Statistics"]["Stats"][2] - player2["Player"]["Statistics"]["Stats"][2]) * 5) >= 0 else 0}% 

		|‾‾‾‾‾|        |‾‾‾‾‾|
		|  {Player_Dice_num}  |  -VS-  |  {Enemy_Dice_num}  |
		|_____|        |_____|

{player2["Player"]["Name"]} Lv {player2["Player"]["Statistics"]["Lv"]} 
HP: {player2["Player"]["Statistics"]["Hp"]} | Зщт {EDefens} |  Урон {EDamage_const} | Увр: {(player2["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2]) * 5 if ((player2["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2]) * 5) >= 0 else 0}% 

""")
    # console временная переменная
    console = None
    while not (console == "1" or console == "2"):
        console = input("Выберите\n1. Сражaться | 2. Сбежать\n: ")

    Fight_or_Escape = True
    while Fight_or_Escape:

        if console == "1":
            Fight_now = True
            Frame = Player_Dice_num - Enemy_Dice_num

            while Fight_now:

                print(
                    f"""
{player1["Player"]["Name"]} Lv {player1["Player"]["Statistics"]["Lv"]} 
HP: {player1["Player"]["Statistics"]["Hp"]} | Зщт {PDefens if PDefens > 0 else 0} |  Урон {PDamage_const}| Увр: {(player1["Player"]["Statistics"]["Stats"][2] - player2["Player"]["Statistics"]["Stats"][2]) * 5 if ((player1["Player"]["Statistics"]["Stats"][2] - player2["Player"]["Statistics"]["Stats"][2]) * 5) >= 0 else 0}% 

		|‾‾‾‾‾|       
		|  {Frame} |
		|_____|

{player2["Player"]["Name"]} Lv {player2["Player"]["Statistics"]["Lv"]} 
HP: {player2["Player"]["Statistics"]["Hp"]} | Зщт {EDefens if EDefens > 0 else 0} |  Урон {EDamage_const} | Увр: {(player2["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2]) * 5 if ((player2["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2]) * 5) >= 0 else 0}% 

1. Удар | 2. Движения | 3. Инвентарь | 4. Сбежать
""")
                console = input(": ")
                if console == "1":
                    # Идея фреймов в буфере порядка действий. При +0 фреймов. Действие игрока Удар -> нож (7 фреймов)
                    # и Действии противника Удар Кувалдой (10 ф.) Число общих фреймов становиться -7. Игрок наносит
                    # удар и снова выбирает действие. Выбор падает на перекат в сторону (4). Игрок не успевает и
                    # получат урон и минус по общим фреймам
                    Hit = Get_Damage_and_Defens("Damage", player1)
                    Enemy_escape = 0 if ((player2["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2]) * 5) < 0 else (player2["Player"]["Statistics"]["Stats"][2] -player1["Player"]["Statistics"]["Stats"][2]) * 5
                    if random.randint(0, 100) <= 100 - Enemy_escape:
                        if EDefens > 0:
                            EDefens -= Hit
                            if EDefens <= 0:
                                print(f"Вы нанесли {Hit} урона Противнику, сломав его броню")
                            else:
                                print(f"Вам нанесли {Hit} урона, но броня взяла урон на себя")
                        else:
                            player2["Player"]["Statistics"]["Hp"] -= Hit
                            print(f"Вы нанесли {Hit} урона Противнику")
                    else:
                        print("Противник увернулся от атаки!")

                    PDefens = Enemy_move(PDefens, EDefens)

                elif console == "2":
                    pass

                elif console == "3":
                    pass

                elif console == "4":
                    Fight_now = False
                    console = "2"

                else:
                    pass  # ciu()

                if player1["Player"]["Statistics"]["Hp"] <= 0:
                    print("Поражение")
                    Fight_now = False
                    Fight_or_Escape = False
                if player2["Player"]["Statistics"]["Hp"] <= 0:
                    print("Победа")
                    Fight_now = False
                    Fight_or_Escape = False





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
                Enemy_move(PDefens, EDefens)
        else:
            pass  # ciu()


Fight(player1, player2)
