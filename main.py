### Подземелья и ещё раз подземелья (По заказу Макса) ###

import os # для работы с cmd(командной строкой)
import json # для работы с json файлами для сохранения прогресса
import time # для работы с временем(таймеры и тд)
import random # для случайных событий и действий

# настройки экрана
# os.system("mode 55, 12")
os.system("chcp 1245")
cls = lambda: os.system("cls")

class Game():
	""" Мозг игры """

	def Start(self):
		self.save = open("save.json")
		self.save = json.load(self.save)
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
					Game.Selection_Class("Рыцарь", "", [3,1,3,1,0])

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
					Game.Selection_Class("Разбойник", "", [2,3,2,0,1])

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
					Game.Selection_Class("Маг", "", [1,1,2,3,1])
		else:
			self.Player = Game.Player(self.save["Name"], self.save["Statistics"]["Stat"]["Lv"], self.save["Statistics"]["Stat"]["Hp"], self.save["Statistics"]["Stat"], self.save["Inventory"], self.save["Info"])




	def Selection_Class(self, Player_Selection_Class, History_Selection_Class, Stat_Selection_Class):
		console = input("1. Подтвердить | 2. Вернуться к выбору\n=> ")

		if console == "1":
			self.job_time = False
			print(History_Selection_Class)

			self.save["Info"]["Class"] = Player_Selection_Class
			for stat, value in zip(self.save["Statistics"]["Stat"], Stat_Selection_Class):
				self.save["Statistics"]["Stat"][stat] = value
			print(self.save)

			self.Player = Game.Player(self.save["Name"], self.save["Statistics"]["Stat"]["Lv"], self.save["Statistics"]["Stat"]["Hp"], self.save["Statistics"]["Stat"], self.save["Inventory"], self.save["Info"])
		elif console == "2":
			cls()
		else:
			print("Команда не распознана")
			time.sleep(2)

class Player():
	""" Игрок """
	def __init__(self, name, lv, hp, stat, inventari, info):
		self.name = save["Name"]
		self.lv = lv
		self.hp = hp
		self.stat = stat
		self.inventory = inventory
		self.info = info

###  ###
print("""
=======================================================
___________---------------------------------___________
-_-_-_-_-_-|Подземелья и ещё раз подземелья|-_-_-_-_-_-
‾‾‾‾‾‾‾‾‾‾‾---------------------------------‾‾‾‾‾‾‾‾‾‾‾\n=======================================================
\n""")

Game = Game()
job = True
while job:
### Игровой цикл ###
	print("1. Играть\n2. Выход")
	console = input('=> ')
	if console == "1":
		Game.Start()
		job = False
	elif console == "2":
		quit()
	else:
		print("Команда не распознана")

