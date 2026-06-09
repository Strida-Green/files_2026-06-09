"""
Tkinter предоставляет виджеты в двух вариантах:
виджеты, которые располагаются непосредственно в пакете tkinter, и
виджеты из пакета tkinter.ttk.
Оба пакета предоставляют практически одни и те же виджеты, например,
виджет Button есть в обоих пакетах.
ttk предоставляет чуть больше функциональности по настройке виджетов, в частности,
по их стилизации. И считается, что виджеты из ttk несколько современнее, чем
стандартные, в то же время с ttk, возможно, чуть сложнее работать.
"""


import tkinter as tk
from tkinter import ttk as ttk

import glob

def fun_001():
    # Пример (открытие всех xml файлов):
    for filename_in in glob.glob('*.xml'):
        with open(filename_in, 'r') as file_in:
            # data = file.read().replace(',', '.').replace(' ', ';')
            data = file_in.read().replace(',', '.')
        filename_out = filename_in
        with open(filename_out, "w") as file_out:
            file_out.write(data)

    print("Готово! Запятая заменена на точку.")


def on_button_01_click():
    fun_001()

window = tk.Tk()
#window.geometry('400x150')

window.title("приложение на Tkinter") # заголовок окна
window.geometry("700x350") # размеры окна

# виджет текстовая метка
label = tk.Label(
    text="запятая->точка",
    fg="black",
    bg="white")
    #width=100,
    #height=20
label.pack() # разместить метку в окне

# виджет кнопка
# button = tk.Button(window, text="Запятую заменить на точку!", command=on_button_click_01)
button_01 = ttk.Button(
    text="(ttk)Запятую заменить на точку!",
    command=on_button_01_click
)
button_01.pack(anchor="s") # разместить кнопку в окне


window.update_idletasks()
window.mainloop()

"""
def main():
    root = Tk()
    ex = Example()
    root.geometry("300x150+300+300")
    root.mainloop()
"""