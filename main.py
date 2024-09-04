### Подземелья и ещё раз подземелья (По заказу Макса) ###

import os  # для работы с cmd(командной строкой)
import json  # для работы с json файлами для сохранения прогресса
import time  # для работы с временем(таймеры и тд)
import Inventory

import random  # для случайных событий и действий

# настройки экрана
# os.system("mode 55, 12")
os.system("chcp 1245")
cls = lambda: os.system("cls")


class Game():
	""" Мозг игры """

	def Start(self):
		with open("save.json", "r") as file:
			self.save = json.load(file)
		self.save = self.save["Player"]
		print(self.save["Name"])
		if self.save["Name"] == None:
			cls()
			name = input("Введите имя персонажа: ")
			self.job_time = True
			while self.job_time:
				print("1. Рыцарь | 2. Разбойник | 3. Маг")
				console = input("Ввыберите класс: ")

				if console == "1":
					cls()
					print("""
   ---Класс Рыцарь---
 #--Статы--#
Сила:         |3
Ловкость:     |1
Выносливость: |3
Интеллект:    |1
Удача:        |0

 #--Предметы--#
Ржавый меч: +2 урон
Ржавая броня: +1 зщт
Свиток Божественая помошь

|Рыцарь - непоколебим не перед чем и всегда остаётся верен в своего Бога|
""")
					Game.Selection_Class("Рыцарь", "", [3, 1, 3, 1, 0])

				elif console == "2":
					cls()
					print("""
   ---Класс Разбойник---
 #--Статы--#
rСила:        |2
Ловкость:     |3
Выносливость: |2
Интеллект:    |0
Удача:        |1

 #--Предметы--#
Ржавый Клинок: +1 урон
Дырявый Мешок: +1кг макс.вес
Подлый выпад: Вероятность увернуться и ударить

|Разбойник - подлый и незнающий пощяды, лучше с ним не шутить|
""")
					Game.Selection_Class("Разбойник", "", [2, 3, 2, 0, 1])

				elif console == "3":
					cls()
					print("""
   ---Класс Маг---
 #--Статы--#
Сила:         |1
Ловкость:     |1
Выносливость: |2
Интеллект:    |3
Удача:        |1

 #--Предметы--#
Надломаный Посох: +1 Инт.
Маленький Ловец душь: Собирает энергию поверженых врагов
Книга заклинаний

|Маг - никчёмный слабак, пока посох не начнёт свититься|
""")
					Game.Selection_Class("Маг", "", [1, 1, 2, 3, 1])
		else:
			self.Player = Game.Player(self.save["Name"], self.save["Statistics"]["Stat"]["Lv"],
									  self.save["Statistics"]["Stat"]["Hp"], self.save["Statistics"]["Stat"],
									  self.save["Inventory"], self.save["Info"])

	def Selection_Class(self, Player_Selection_Class, History_Selection_Class, Stat_Selection_Class):
		console = input("1. Подтвердить | 2. Вернуться к выбору\n=> ")

		if console == "1":
			self.job_time = False
			print(History_Selection_Class)

			self.save["Info"]["Class"] = Player_Selection_Class
			for stat, value in zip(self.save["Statistics"]["Stat"], Stat_Selection_Class):
				self.save["Statistics"]["Stat"][stat] = value
			print(self.save)

			self.Player = Game.Player(self.save["Name"], self.save["Statistics"]["Stat"]["Lv"],
									  self.save["Statistics"]["Stat"]["Hp"], self.save["Statistics"]["Stat"],
									  self.save["Inventory"], self.save["Info"])
		elif console == "2":
			cls()
		else:
			print("Команда не распознана")
			time.sleep(2)

# Создание сущностей
class Creature:
	def __init__(self, name, lv, hp, stats, inventory, info, dialogs):
		self.name = name
		self.lv = lv
		self.hp = hp
		self.stats = stats
		self.inventory = inventory
		self.info = info
		self.coins = 0
		self.limbs = {
			"Head": int(self.hp / 2),
			"Torso": int(self.hp),
			"Hands": int(self.hp / 4),
			"Foods": int(self.hp / 4),
		}
		self.dialogs = dialogs
		self.defens = self.Get_Damage_and_Defens()["Defens"]

	def take_damage(self, where, damage):
		if self.defens > 0:
			self.defens -= damage
			if self.defens <= 0:
				print(self.dialogs["take_damage"][0].format(damage))
			else:
				print(self.dialogs["take_damage"][1].format(damage))
		else:
			self.hp -= damage
			self.limbs[where] -= damage
			print(self.dialogs["take_damage"][2].format(damage))

		if self.hp <= 0:
			print(f"{self.name} повержен!")

	def push_damage(self):
		return self.Get_Damage_and_Defens()["Damage"]

	def is_alive(self):
		return self.hp > 0

	def Get_Damage_and_Defens(self):
		_result = {}
		if self.inventory == []:
			_result["Damage"] = self.stats["Power"] # Если инвентарь пуст код не работает
			_result["Defens"] = self.stats["Endurance"]
		for item in self.inventory:
			if item.get("Equipment") == "Enable":
				if item.get("Damage") is not None:
					parts = item.get("Damage").strip().split('-')
					Damage_list = [int(part) for part in parts]
					_result["Damage"] = self.stats["Power"] + random.randint(Damage_list[0], Damage_list[1])
					_result["Damage_const"] = self.stats["Power"] + int((Damage_list[0] + Damage_list[1])/2) # cp. знач. урона оружия | индексы отображают разброс Например 2-4 урона
				elif item.get("Defens") is not None:
					_result["Defens"] = self.stats["Endurance"] + int(item.get("Defens"))
		return _result


class Player(Creature):
	""" Игрок """

	def __init__(self, name, lv, hp, stats, inventory, info):
		dialogs = {
			"take_damage": [
				"Вас нанесли {} урона, сломав броню",
				"Вам нанесли {} урона, но броня взяла урон на себя",
				"Вам нанесли {} урона"
			]

		}
		super().__init__(name, lv, hp, stats, inventory, info, dialogs)

class Monster(Creature):
	""" Монстр """

	def __init__(self, name, lv, hp, stats, inventory, info):
		dialogs = {
			"take_damage": [
				"Вы нанесли {} урона " + name + ", сломав его броню",
				"Вы нанесли {} урона, но броня взяла урон на себя",
				"Вы нанесли {} урона " + name
			]

		}
		super().__init__(name, lv, hp, stats, inventory, info, dialogs)


# Пересоздание боевой системы
class Fight():
	pass

###  ###
print("""
=======================================================
___________---------------------------------___________
-_-_-_-_-_-|Подземелья и ещё раз подземелья|-_-_-_-_-_-
‾‾‾‾‾‾‾‾‾‾‾---------------------------------‾‾‾‾‾‾‾‾‾‾‾\n=======================================================
\n""")
if __name__ == "__main__":
	player = Player(
		name="Mife",
		lv="1",
		hp=10,
		stats={
				"Survive":      4,  # Жиз
				"Power":        3,  # Сил
				"Dexterity":    1,  # Лов
				"Endurance":    2,  # Вын
				"Intelligence": 0,  # Инт
				"Luck":         0  # Удч

		},
		inventory=[],
		# inventory=Inventory.Inventory,
		info="None"
	)
	print(player.take_damage(damage=2, where="Head"))
	print(player.limbs["Head"])

# Game = Game()
# job = True
# while job:
# ### Игровой цикл ###
# 	print("1. Играть\n2. Выход")
# 	console = input('=> ')
# 	if console == "1":
# 		Game.Start()
# 		job = False
# 	elif console == "2":
# 		quit()
# 	else:
# 		print("Команда не распознана")
#
