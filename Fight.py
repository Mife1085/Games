import random
import Items
player1 = {
"Player" : {
        "Name": "Mife",

        "Statistics": {
                "Lv" : 1,
                "Hp" : 10,
                "Gold" : 0,
                "Stats" : [4, 3, 1, 2, 0, 0] # Жиз, Сил, Лов, Вын, Инт, Удч
        },

        "Inventory" : [
                Items.id_list[0], Items.id_list[2], Items.id_list[5], Items.id_list[23] 

        ],

        "Info" : {}
        }
}
player1["Player"]["Statistics"]["Hp"] = player1["Player"]["Statistics"]["Stats"][0]*5 
player2 = {
"Player" : {
        "Name": "Enemy",

        "Statistics": {
                "Lv" : 1,
                "Hp" : 10,
                "Gold" : 0,
                "Stats" : [4, 2, 4, 0, 0, 0]
        },
        "Inventory" : [
                Items.id_list[0]
        ],

        "Info" : {}
        }
}

def Random_stat(player, lv): # Создание рандомных статов за очки прокачи с уровня
        stat_time = list(range(6))

        player["Player"]["Statistics"]["Lv"] = lv # разброс по уровню # random.randint(lv, lv+3)
        exp_point = player["Player"]["Statistics"]["Lv"] * 2 # очки прокачки (урв * очки прокачки за увр)
        i = 0
        while i != exp_point + 10:
                i = 0
                for stat_num in range(6):
                        stat_time[stat_num] = player["Player"]["Statistics"]["Stats"][stat_num] 
                for o in range(6):
                        stat_time[o] += random.randint(0, int(2+lv*2/6))
                        i += stat_time[o]
        player["Player"]["Statistics"]["Stats"] = stat_time
        player["Player"]["Statistics"]["Hp"] = player["Player"]["Statistics"]["Stats"][0]*5 # приведение статов хп в жизни 
       
Random_stat(player1, 50)
Random_stat(player2, 50)

def Fight(player1, player2):
        print(player1) #?
        def Enemy_move(PDamage, PDefens, EDefens):
                """Возможности противника"""
                PDamage = PDamage
                PDefens = PDefens
                EDefens = EDefens

                for item in player2["Player"]["Inventory"]:
                        if item.get("Equipment") == "Enable":
                                if player2["Player"]["Inventory"][item].get("Damage") != None:
                                        EDamage = player2["Player"]["Statistics"]["Stats"][1] + random.randint(int(player2["Player"]["Inventory"][item].get("Damage")[0]), int(player2["Player"]["Inventory"][item].get("Damage")[2]))
                                else:
                                        EDamage = player2["Player"]["Statistics"]["Stats"][1]

                Hit = (EDamage)

                Enemy_escape = (player1["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2])*10 if ((player1["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2])*10)>=0 else 0 #проверить
                if random.randint(0, 100) <= 100-Enemy_escape:
                        if PDefens > 0:
                                PDefens -= Hit
                                if PDefens <= 0:
                                        print(f"Вам нанесли {Hit} урона, сломав броню")
                        else:
                                player1["Player"]["Statistics"]["Hp"] -= Hit
                                print(f"Вам нанесли {Hit} урона")
                else:
                        print("Вы увернулся от атаки!") 
                
                return PDefens

        def Get_Damage_and_Defens(param):
                
                        for item in player1["Player"]["Inventory"]:
                                if player1["Player"]["Inventory"][item].get("Equipment") == "Enable":
                                                if param == "PDmg":
                                        if player1["Player"]["Inventory"][item].get("Damage", None) != None:
                                                return int((int(player1["Player"]["Inventory"][item].get("Damage")[0]) + int(player1["Player"]["Inventory"][item].get("Damage")[2]))/2)
                if param == "PDef":                                                
                        for item in player1["Player"]["Inventory"]:
                                if player1["Player"]["Inventory"][item].get("Equipment") == "Enable":
                                        if player1["Player"]["Inventory"][item].get("Защита") != None:
                                                return int(player1["Player"]["Inventory"][item].get("Защита")[0])

                if param == "EDmg":
                        for item in player2["Player"]["Inventory"]:
                                if player2["Player"]["Inventory"][item].get("Equipment") == "Enable":
                                        if player2["Player"]["Inventory"][item].get("Damage", None) != None:
                                                return int((int(player2["Player"]["Inventory"][item].get("Damage")[0]) + int(player2["Player"]["Inventory"][item].get("Damage")[2]))/2)
                if param == "EDef":                                                
                        for item in player2["Player"]["Inventory"]:
                                if player2["Player"]["Inventory"][item].get("Equipment") == "Enable":
                                        if player2["Player"]["Inventory"][item].get("Защита") != None:
                                                return int(player2["Player"]["Inventory"][item].get("Защита")[0]) 

        PDamage_const = Get_Damage_and_Defens("PDmg") + player1["Player"]["Statistics"]["Stats"][1]if Get_Damage_and_Defens("PDmg") != None else player1["Player"]["Statistics"]["Stats"][1]
        PDefens = Get_Damage_and_Defens("PDef") + player1["Player"]["Statistics"]["Stats"][4] if Get_Damage_and_Defens("PDef") != None else player1["Player"]["Statistics"]["Stats"][4]

        EDamage_const = Get_Damage_and_Defens("EDmg") + player2["Player"]["Statistics"]["Stats"][1] if Get_Damage_and_Defens("EDmg") != None else player2["Player"]["Statistics"]["Stats"][1]
        EDefens = Get_Damage_and_Defens("EDef") + player2["Player"]["Statistics"]["Stats"][4] if Get_Damage_and_Defens("EDef") != None else player2["Player"]["Statistics"]["Stats"][4]

        Player_Dice_num = random.randint(player1["Player"]["Statistics"]["Lv"], player1["Player"]["Statistics"]["Lv"]+player1["Player"]["Statistics"]["Stats"][2])
        Enemy_Dice_num = random.randint(player2["Player"]["Statistics"]["Lv"], player2["Player"]["Statistics"]["Lv"]+player2["Player"]["Statistics"]["Stats"][2])
        
        print(
f"""
{player1["Player"]["Name"]} Lv {player1["Player"]["Statistics"]["Lv"]} 
HP: {player1["Player"]["Statistics"]["Hp"]} | Зщт {PDefens} |  Урон {PDamage_const}| Увр: {(player1["Player"]["Statistics"]["Stats"][2] - player2["Player"]["Statistics"]["Stats"][2])*10 if ((player1["Player"]["Statistics"]["Stats"][2] - player2["Player"]["Statistics"]["Stats"][2])*10)>=0 else 0}% 

        |‾‾‾‾‾|        |‾‾‾‾‾|
        |  {Player_Dice_num}  |  -VS-  |  {Enemy_Dice_num}  |
        |_____|        |_____|

{player2["Player"]["Name"]} Lv {player2["Player"]["Statistics"]["Lv"]} 
HP: {player2["Player"]["Statistics"]["Hp"]} | Зщт {EDefens} |  Урон {EDamage_const} | Увр: {(player2["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2])*10 if ((player2["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2])*10)>=0 else 0}% 

""")    
        console = None
        while (console == "1" or console == "2") == False:
                console = input("Выберите\n1. Сражться | 2. Сбежать\n: ")

        Fight_or_Escape = True
        while Fight_or_Escape:
                
                
                if console == "1":
                        Fight_now = True
                        Frame = Player_Dice_num - Enemy_Dice_num

                        while Fight_now:
                                                                                        
                                print(
f"""
{player1["Player"]["Name"]} Lv {player1["Player"]["Statistics"]["Lv"]} 
HP: {player1["Player"]["Statistics"]["Hp"]} | Зщт {PDefens if PDefens > 0 else 0} |  Урон {PDamage_const}| Увр: {(player1["Player"]["Statistics"]["Stats"][2] - player2["Player"]["Statistics"]["Stats"][2])*10 if ((player1["Player"]["Statistics"]["Stats"][2] - player2["Player"]["Statistics"]["Stats"][2])*10)>=0 else 0}% 

        |‾‾‾‾‾|       
        |  {Frame} |
        |_____|

{player2["Player"]["Name"]} Lv {player2["Player"]["Statistics"]["Lv"]} 
HP: {player2["Player"]["Statistics"]["Hp"]} | Зщт {EDefens if EDefens > 0 else 0} |  Урон {EDamage_const} | Увр: {(player2["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2])*10 if ((player2["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2])*10)>=0 else 0}% 

1. Удар | 2. Движения | 3. Инвентарь | 4. Сбежать
""")
                                console = input(": ")
                                if console == "1":
                                # Идея фраймов в буфере поряда действий. 
                                # При +0 фраймов. действие игрока Удар -> нож (7 фреймов) и Действии противника Удар Кувалдой (10 ф.) 
                                # Число общих фреймов становиться -7. Игрок наносит удар и снова выбирает действие. Выбор падает на перекат в сторону (4).
                                # Игрок не успевает и получат урон и минус по общим фреймам
                                        for item in player1["Player"]["Inventory"]:
                                                if player1["Player"]["Inventory"][item].get("Equipment") == "Enable":
                                                        if player1["Player"]["Inventory"][item].get("Damage") != None:
                                                                PDamage = player1["Player"]["Statistics"]["Stats"][1] + random.randint(int(player1["Player"]["Inventory"][item].get("Damage")[0]), int(player1["Player"]["Inventory"][item].get("Damage")[2]))
                                        Hit = PDamage
                                        Enemy_escape = (player2["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2])*10 if ((player2["Player"]["Statistics"]["Stats"][2] - player1["Player"]["Statistics"]["Stats"][2])*10)>=0 else 0
                                        if random.randint(0, 100) <= 100-Enemy_escape:
                                                if EDefens > 0:
                                                        EDefens -= Hit
                                                        if EDefens <= 0:
                                                                print(f"Вы нанесли {Hit} урона Противнику, сломав его броню")
                                                else:
                                                        player2["Player"]["Statistics"]["Hp"] -= Hit
                                                        print(f"Вы нанесли {Hit} урона Противнику")
                                        else:
                                                print("Противник увернулся от атаки!") 
                                        
                                        PDefens = Enemy_move(PDamage, PDefens, EDefens)

                                elif console == "2":
                                        pass

                                elif console == "3":
                                        inv = player1["Player"]["Inventory"]
                                        objects = []
                                        for key in inv:
                                                objects.append(key)
                                        feature = []
                                        for key2 in objects:
                                                feature.append(inv[key2])
                                        print(objects, feature)
                                        print("Equipment: ")
                                        for key, itemue in zip(objects, feature):
                                                if itemue.get("Equipment") == "Enable":
                                                        print(f"""{key} | {itemue.get("Damage", "")} {itemue.get("Defense", "")}""")
                                                
                                        print("Else: ")
                                        for key, itemue in zip(objects, feature):
                                                if itemue.get("Equipment", "Disabled") == "Disabled":
                                                        print(f"""{key} | {itemue.get("Damage", "")} {itemue.get("Defense", "")}""")

                                elif console == "4":
                                        Fight_now = False
                                        console = "2"
                                        
                                else:
                                        pass # ciu()

                                if player1["Player"]["Statistics"]["Hp"] <= 0:
                                        print("Порожение")
                                        Fight_now = False
                                        Fight_or_Escape = False
                                if player2["Player"]["Statistics"]["Hp"] <= 0:
                                        print("Победа")
                                        Fight_now = False
                                        Fight_or_Escape = False





                elif console == "2":
                        escape = (player1["Player"]["Statistics"]["Stats"][2] - player2["Player"]["Statistics"]["Stats"][2])*10 if ((player1["Player"]["Statistics"]["Stats"][2] - player2["Player"]["Statistics"]["Stats"][2])*10)>=0 else 0
                        print(f"Шанс сбежать: {escape}%")
                        if random.randint(0, 100) >= 100-escape:
                                print("Вы избежали сражения")
                                Fight_or_Escape = False
                        else:   
                                print("Вы не смогли сбежать")
                                console = "1"
                                Fight_now = False
                                Enemy_move()
                else:   
                        pass # ciu()

Fight(player1, player2)
