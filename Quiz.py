from tkinter import *
from data import data

class Quiz:
	# Генерация приложения
	def __init__(self, parent):
		print("Старт работы")
		self.count = 0
		self.score = 0
		self.questions = data
		frame = Frame(parent)		
		stratBtn = Button(frame, text = "Начать опрос", command = lambda: self.startBtnFunc(parent, frame))
		stratBtn.pack(pady = [70, 0])

		aboutBtn = Button(frame, text = "О разработчиках", command = lambda: self.aboutBtnFunc(parent, frame))
		aboutBtn.pack(pady = [10, 10])

		frame.pack(anchor = CENTER)

	# Обратока кнопки "Старт"
	def startBtnFunc(self, parent, frame):
		print("Начало")
		#print(self.count)
		#Очищаем всё
		for widget in frame.winfo_children():
		    widget.destroy()
		    frame.pack_forget()

		frame = Frame(parent)
		frame.pack(anchor = CENTER)
		label = Label(frame, text = self.questions[self.count]['title'])
		label.pack(pady=[30, 10])

		self.var = IntVar()
		self.var.set(None)

		for i in range(0, 4):
			rbtn = Radiobutton(frame, text = self.questions[self.count]['answers'][i]['title'], variable = self.var, value = int(self.questions[self.count]['answers'][i]['value']))
			rbtn.pack(pady=[5,5])

		if (self.count + 1) < len(self.questions):
			continueBtn = Button(frame, text="Далее", command = lambda: self.setScore(parent, frame))
		else:
			continueBtn = Button(frame, text="Ответить и закончить", command = lambda: self.setScore(parent, frame))

		continueBtn.pack()
		self.count += 1

	# Обратока кнопки "О разработчиках"
	def aboutBtnFunc(self, parent, frame):
		print("О разработчиках")
		#Очищаем всё
		for widget in frame.winfo_children():
		    widget.destroy()
		    frame.pack_forget()

		#Создаём новый фрейм
		frame = Frame(parent)
		label1 = Label(frame, text = "Разработал: Новоселов А.В. ПИ-23")
		label1.pack(pady = [70, 0])

		stratBtn = Button(frame, text = "Начать опрос", command = lambda: self.startBtnFunc(parent, frame))
		stratBtn.pack(pady = [10, 0])

		frame.pack(anchor = CENTER)

	#Последний экран
	def endWindow(self, parent, frame):
		print("Заканчиваем тестирование")
		#Очищаем всё
		for widget in frame.winfo_children():
		    widget.destroy()
		    frame.pack_forget()

		frame = Frame(parent)
		label0 = Label(frame, text = "Вы завершили тест")
		label0.pack(pady=[70,10])
		label1 = Label(frame, text = f"Вcего вопросов было: {self.count}" )
		label1.pack(pady=[0,10])
		label2 = Label(frame, text = f"Правильных ответов: {self.score}")
		label2.pack(pady=[0, 10])
		frame.pack(anchor = CENTER)

	# Считаем очки
	def setScore(self, parent, frame):
		if self.var.get() == 0:
			self.score+=1

		if (self.count) < len(self.questions):
			self.startBtnFunc(parent, frame)
		else:
			self.endWindow(parent, frame)
		#self.score += self.var.get()