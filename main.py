from Quiz import Quiz 
from tkinter import *

# Запуск приложения

window = Tk()
# Поменять название!
window.title("Опрос на темы: Базы данных. Основы SQL") # Тема: Основы SQL
window.geometry('800x400')

obj = Quiz(window)

window.mainloop()