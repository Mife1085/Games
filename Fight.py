import random
import Inventory
import Items
ItemsCollection = Items.ItemsCollection()
ItemsCollection.Load()

player1 = {
	"Player": {
		"Name": "Mife",
		"Statistics": {
			"Lv": 1,
			"Hp": 10,
			"Gold": 0,
			"Stats": {
				"Survive":      4,  # Жиз
				"Power":        3,  # Сил
				"Dexterity":    1,  # Лов
				"Endurance":    2,  # Вын
				"Intelligence": 0,  # Инт
				"Luck":         0  # Удч

		}
		},

		"Inventory": [
			ItemsCollection.get_item_by_id(7)		],

		"Info": {}
	}
}
player1["Player"]["Statistics"]["Hp"] = player1["Player"]["Statistics"]["Stats"]["Survive"] * 5

player2 = {
	"Player": {
		"Name": "Enemy",

		"Statistics": {
			"Lv": 1,
			"Hp": 10,
			"Gold": 0,
			"Stats": {
				"Survive":      10,  # Жиз
				"Power":        0,  # Сил
				"Dexterity":    0,  # Лов
				"Endurance":    0,  # Вын
				"Intelligence": 0,  # Инт
				"Luck":         0  # Удч
			}
		},
		"Inventory": [
			# ItemsCollection.id_list[0]
			ItemsCollection.get_item_by_id(40)
		],

		"Info": {}
	}
}

player1["Player"]["Inventory"][0]["Equipment"] = "Enable"
player2["Player"]["Inventory"][0]["Equipment"] = "Enable"

class Time_class():
	"""docstring for Time_class"""
	def __init__(self, p1, p2):
		player1 = p1
		player2 = p2

	def Get_Damage_and_Defens(self, param):
		print("Starting Get_Damage_and_Defens")

		result = 0
		if  player1["Player"]["Inventory"] == []:
			result = player1["Player"]["Statistics"]["Stats"]["Power"] # Если инвентарь пуст код не работает
		if player2["Player"]["Inventory"] == []:
			result = player1["Player"]["Statistics"]["Stats"]["Power"] # Этот кусок кода просто костыль


		for item in player1["Player"]["Inventory"]:
			if item.get("Equipment") == "Enable":

				if item.get("Damage") is not None:
					parts = item.get("Damage").strip().split('-')
					Damage_list = [int(part) for part in parts]
					if param == "PDamage_const":
						result = player1["Player"]["Statistics"]["Stats"]["Power"] + int((Damage_list[0] + Damage_list[1])/2) # cp. знач. урона оружия | индексы отображают разброс Например 2-4 урона
					elif param == "PDamage":
						result = player1["Player"]["Statistics"]["Stats"]["Power"] + random.randint(Damage_list[0], Damage_list[1])

				elif param == "PDefens":
					if item.get("Защита") is not None:
						result = int(item.get("Защита")[0])

			else:
				if param == "PDamage":
					result = player1["Player"]["Statistics"]["Stats"]["Power"]

		for item in player2["Player"]["Inventory"]:
			if item.get("Equipment") == "Enable":
				if item.get("Damage") is not None:
					parts = item.get("Damage").strip().split('-')
					Damage_list = [int(part) for part in parts]
					if param == "EDamage_const":
						result = player2["Player"]["Statistics"]["Stats"]["Power"] + int((Damage_list[0] + Damage_list[1])/2) # cp. знач. урона оружия | индексы отображают разброс Например 2-4 урона
					elif param == "EDamage":
						result = player2["Player"]["Statistics"]["Stats"]["Power"] + random.randint(Damage_list[0], Damage_list[1])

				elif param == "EDefens":
					if item.get("Защита") is not None:
						result = int(item.get("Защита")[0])

		return result

	def Enemy_move(self,  PDefens, EDefens):
		print("Starting Enemy_move")
		"""Возможности противника"""
		self.PDefens = PDefens
		self.EDefens = EDefens

		Hit = self.Get_Damage_and_Defens("EDamage")

		Enemy_escape = 0 if ((player1["Player"]["Statistics"]["Stats"]["Dexterity"] -
		                      player1["Player"]["Statistics"]["Stats"]["Dexterity"]) * 10) < 0 else (player1["Player"]["Statistics"]["Stats"]["Dexterity"] - player1["Player"]["Statistics"]["Stats"]["Dexterity"]) * 10  #проверить
		if random.randint(0, 100) <= 100-Enemy_escape:
			if self.PDefens > 0:
				self.PDefens -= Hit
				if self.PDefens <= 0:
					print(f"Вам нанесли {Hit} урона, сломав броню")
				else:
					print(f"Вам нанесли {Hit} урона, но броня взяла урон на себя")
			else:
				player1["Player"]["Statistics"]["Hp"] -= Hit
				print(f"Вам нанесли {Hit} урона")
		else:
			print("Вы увернулся от атаки!")

		return self.PDefens

		print(player1["Player"]["Inventory"])
		for item in player1["Player"]["Inventory"]:
			print(item)
		print("End_________________________________________")

	def Random_stat(self, player, lv): # Создание рандомных статов за очки прокачки с уровня
		print("Starting Random_stat")
		stat_time = list(range(6))

		player["Player"]["Statistics"]["Lv"] = lv # разброс по уровню # random.randint(lv, lv+3)
		exp_point = player["Player"]["Statistics"]["Lv"] * 2 # очки прокачки (урв * очки прокачки за увр)
		i = 0
		while i != exp_point + 10:
			i = 0
			stat_time = player["Player"]["Statistics"]["Stats"].values()
			stat_time = list(stat_time)
			for o in range(6):
				stat_time[o] += random.randint(0, int(2+lv*2/6))
				i += stat_time[o]
		for stat_name, stat_num in zip(player["Player"]["Statistics"]["Stats"], stat_time):
			player["Player"]["Statistics"]["Stats"][stat_name] = stat_num
		player["Player"]["Statistics"]["Hp"] = player["Player"]["Statistics"]["Stats"]["Survive"]*5 # приведение статов хп в жизни



	def Fight(self, player1, player2):
		print("Starting Fight")
		self.Random_stat(player1, 10)
		self.Random_stat(player2, 10)

		PDamage_const = self.Get_Damage_and_Defens("PDamage_const") # cp. знач. урона Игрока
		self.PDefens = self.Get_Damage_and_Defens("PDefens") + player1["Player"]["Statistics"]["Stats"]["Endurance"]

		EDamage_const = self.Get_Damage_and_Defens("EDamage_const")
		self.EDefens = self.Get_Damage_and_Defens("EDef") + player2["Player"]["Statistics"]["Stats"]["Endurance"]

		Player_Dice_num = random.randint(player1["Player"]["Statistics"]["Lv"], player1["Player"]["Statistics"]["Lv"]+player1["Player"]["Statistics"]["Stats"]["Dexterity"])
		Enemy_Dice_num = random.randint(player2["Player"]["Statistics"]["Lv"], player2["Player"]["Statistics"]["Lv"]+player2["Player"]["Statistics"]["Stats"]["Dexterity"])

		print(
	f"""1
	{player1["Player"]["Name"]} Lv {player1["Player"]["Statistics"]["Lv"]} 
	HP: {player1["Player"]["Statistics"]["Hp"]} | Зщт {self.PDefens} |  Урон {PDamage_const}| Увр: {(player1["Player"]["Statistics"]["Stats"]["Dexterity"] - player2["Player"]["Statistics"]["Stats"]["Dexterity"])*10 if ((player1["Player"]["Statistics"]["Stats"]["Dexterity"] - player2["Player"]["Statistics"]["Stats"]["Dexterity"])*10)>=0 else 0}% 

		|‾‾‾‾‾|        |‾‾‾‾‾|
		|  {Player_Dice_num}  |  -VS-  |  {Enemy_Dice_num}  |
		|_____|        |_____|

	{player2["Player"]["Name"]} Lv {player2["Player"]["Statistics"]["Lv"]} 
	HP: {player2["Player"]["Statistics"]["Hp"]} | Зщт {self.EDefens} |  Урон {EDamage_const} | Увр: {(player2["Player"]["Statistics"]["Stats"]["Dexterity"] - player1["Player"]["Statistics"]["Stats"]["Dexterity"])*10 if ((player2["Player"]["Statistics"]["Stats"]["Dexterity"] - player1["Player"]["Statistics"]["Stats"]["Dexterity"])*10)>=0 else 0}% 

	""")
		# console времяная переменная
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
	HP: {player1["Player"]["Statistics"]["Hp"]} | Зщт {self.PDefens if self.PDefens > 0 else 0} |  Урон {PDamage_const}| Увр: {(player1["Player"]["Statistics"]["Stats"]["Dexterity"] - player2["Player"]["Statistics"]["Stats"]["Dexterity"])*10 if ((player1["Player"]["Statistics"]["Stats"]["Dexterity"] - player2["Player"]["Statistics"]["Stats"]["Dexterity"])*10)>=0 else 0}% 

		|‾‾‾‾‾|       
		|  {Frame} |
		|_____|

	{player2["Player"]["Name"]} Lv {player2["Player"]["Statistics"]["Lv"]} 
	HP: {player2["Player"]["Statistics"]["Hp"]} | Зщт {self.EDefens if self.EDefens > 0 else 0} |  Урон {EDamage_const} | Увр: {(player2["Player"]["Statistics"]["Stats"]["Dexterity"] - player1["Player"]["Statistics"]["Stats"]["Dexterity"])*10 if ((player2["Player"]["Statistics"]["Stats"]["Dexterity"] - player1["Player"]["Statistics"]["Stats"]["Dexterity"])*10)>=0 else 0}% 

	1. Удар | 2. Движения | 3. Инвентарь | 4. Сбежать
	""")
					console = input(": ")
					if console == "1":
					# Идея фраймов в буфере поряда действий.
					# При +0 фраймов. Действие игрока Удар -> нож (7 фреймов) и Действии противника Удар Кувалдой (10 ф.)
					# Число общих фреймов становиться -7. Игрок наносит удар и снова выбирает действие. Выбор падает на перекат в сторону (4).
					# Игрок не успевает и получат урон и минус по общим фреймам
						Hit =  self.Get_Damage_and_Defens("PDamage")
						Enemy_escape = (player2["Player"]["Statistics"]["Stats"]["Dexterity"] - player1["Player"]["Statistics"]["Stats"]["Dexterity"])*10 if ((player2["Player"]["Statistics"]["Stats"]["Dexterity"] - player1["Player"]["Statistics"]["Stats"]["Dexterity"])*10)>=0 else 0
						if random.randint(0, 100) <= 100-Enemy_escape:
							if self.EDefens > 0:
								self.EDefens -= Hit
								if self.EDefens <= 0:
									print(f"Вы нанесли {Hit} урона Противнику, сломав его броню")
							else:
								player2["Player"]["Statistics"]["Hp"] -= Hit
								print(f"Вы нанесли {Hit} урона Противнику")
						else:
							print("Противник увернулся от атаки!")

						self.PDefens = self.Enemy_move(self.PDefens, self.EDefens)

					elif console == "2":
						pass

					elif console == "3":
						inv = Inventory("save.json")
						inv
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
				escape = (player1["Player"]["Statistics"]["Stats"]["Dexterity"] - player2["Player"]["Statistics"]["Stats"]["Dexterity"])*10 if ((player1["Player"]["Statistics"]["Stats"]["Dexterity"] - player2["Player"]["Statistics"]["Stats"]["Dexterity"])*10)>=0 else 0
				print(f"Шанс сбежать: {escape}%")
				if random.randint(0, 100) >= 100-escape:
					print("Вы избежали сражения")
					Fight_or_Escape = False
				else:   
					print("Вы не смогли сбежать")
					console = "1"
					Fight_now = False
					self.Enemy_move()
			else:   
				pass # ciu()
Game = Time_class(player1, player2)
Game.Fight(player1, player2)
