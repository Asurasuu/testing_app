from tkinter import *
from data import data


class Quiz:
    # Генерация приложения
    def __init__(self, parent):
        print("Старт работы")
        self.count = 0
        self.score = 0
        self.questions = data  # Получаем вопросы с ответами с отдельного файла
        self.pp = parent

        self.var = IntVar()  # переопределять при нажатии на вопрос
        self.var.set(None)

        self.answers = {}

        frame = Frame(parent, bg='white')

        label1 = Label(frame, text="Тема теста: Основы SQL", bg='white', fg='black', font='bold')
        label1.pack(pady=[70, 0])

        stratBtn = Button(frame, text="Начать опрос", bg='white', fg='black', command=lambda: self.startBtnFunc(self.count, parent, frame, 0))
        stratBtn.pack(pady=[70, 0])

        aboutBtn = Button(frame, text="О разработчиках", bg='white', fg='black', command=lambda: self.aboutBtnFunc(parent, frame))

        aboutBtn.pack(pady=[10, 10])
        frame.pack(anchor=CENTER)

    # Обратока кнопки "Старт"
    def startBtnFunc(self, cc, parent, frame, back):
        self.count = cc

        try:
            self.answers[back] = self.var.get()
        except:
            self.var.set(None)

        try:
            self.var.set(self.answers[self.count])
        except:
            self.var.set(None)

        #print(self.answers)

        # Очищаем всё
        for widget in frame.winfo_children():
            widget.destroy()
            frame.pack_forget()

        frame = Frame(parent, bg='white')
        frame.pack(anchor=CENTER)
        label = Label(frame, text=self.questions[self.count]['title'], bg='white', fg='black')
        label.pack(pady=[30, 10])

        for i in range(0, 4):
            rbtn = Radiobutton(frame, text=self.questions[self.count]['answers'][i]['title'], variable=self.var,
                               value=int(self.questions[self.count]['answers'][i]['value']), bg='white', fg='black')
            rbtn.pack(pady=[5, 5])

        if (self.count == len(self.questions)-1): # and (len(self.questions) == len(self.answers) - 2):
            print('Показываем кнопку')
            try:
                self.answers[self.count] = self.var.get()
            except:
                print('Что-то отвалилось, но это уже не наши проблемы!')

            Button(frame, text='Закончить и посчитать ответы', bg='white', fg='black', command= lambda: self.endWindow(parent, frame)).pack(pady=10)

        panelW = PanedWindow(frame, orient=HORIZONTAL, bg='white')
        panelW.pack(anchor=CENTER, pady=30)

        for i in range(0, len(self.questions)):

            color = 'white'

            if i in self.answers:
                color = 'yellow'

            if i == self.count:
                color = 'green'

            Button(panelW, text=i+1, bg=color, fg='black', command= lambda e = i, back = self.count: self.startBtnFunc(e, parent, frame, back) ).grid(row = 0, column = i)

    # Обратока кнопки "О разработчиках"
    def aboutBtnFunc(self, parent, frame):
        print("О разработчиках")

        #Очищаем всё
        for widget in frame.winfo_children():
            widget.destroy()
            frame.pack_forget()

        #Создаём новый фрейм
        frame = Frame(parent, background="white")

        label1 = Label(frame, text="Разработал: Новоселов А.В. ПИ-33", bg='white', fg='black')
        label1.pack(pady=[70, 0])

        startBtn = Button(frame, text="Начать опрос", bg='white', fg='black',
                          command=lambda: self.startBtnFunc(self.count, parent, frame, 0))

        startBtn.pack(pady=[10, 0])

        frame.pack(anchor=CENTER)

    #Последний экран
    def endWindow(self, parent, frame):
        print("Заканчиваем тестирование")
        #Очищаем всё
        for widget in frame.winfo_children():
            widget.destroy()
            frame.pack_forget()

        for i in self.answers:
            if i == 0:
                self.score += 1

        frame = Frame(parent, bg='white')
        label0 = Label(frame, bg='white', fg='black', text="Вы завершили тест")
        label0.pack(pady=[70, 10])
        label1 = Label(frame, bg='white', fg='black', text=f"Вcего вопросов было: {len(self.questions)}")
        label1.pack(pady=[0, 10])
        label2 = Label(frame, bg='white', fg='black', text=f"Правильных ответов: {self.score}")
        label2.pack(pady=[0, 10])
        frame.pack(anchor=CENTER)