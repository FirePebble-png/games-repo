from tkinter import *

sch = 0
window = Tk()
size1, size2 = 300, 300
window.geometry(f"{size1}x{size2}")
text_for_label = """Добро пожаловать в новый мир! Как ты предпочитаешь передвигаться?
 1 - пешком 
 2 - на лошади """
def main(text_for_label):
    global label
    label = Label(window, text=text_for_label)
    label.place(x=0, y=0)

    entry = Entry(window)
    entry.place(x=0, y=100)

    check_button = Button(window, text='Ответить', command=lambda: get_key(entry.get(), sch))
    check_button.place(x=200, y=200)

    window.mainloop()


def get_key(answer, sch):

    if sch == 0:
        sch += 1
        if answer == "1":
            text_for_label = """Вы пеший странник, куда вам идти?
             1 - на восток
            2 - на запад"""

        elif answer == "2":
            text_for_label = """Под тобй конь могучий, куда путь держишь?
            1 - на восток
            2 - на запад"""
    elif sch == 1:
        sch += 1
        if answer == "1":
            text_for_label = """Вы пеший dguysegfiusehfiosehfioик, куда вам идти?
               1 - на восток
              2 - на запад"""

        elif answer == "2":
            text_for_label = """Под тhwefwjyeefbuiwfbогучий, куда путь держишь?
              1 - на восток
              2 - на запад"""
        elif answer == "3":
            text_for_label = """Под тhwefwjyewdqwefwfqw2fewrggwefwe3f3, куда путь держишь?
              1 - на восток
              2 - на запад"""
    elif sch == 2:
        sch += 1
        if answer == "1":
            text_for_label = """Вы пеший dguysegfiusehfiosehfioик, куда вам идти?
               1 - на восток
              2 - на запад"""

        elif answer == "2":
            text_for_label = """Под тhwefwjyeefbuiwfbогучий, куда путь держишь?
              1 - на восток
              2 - на запад"""
        elif answer == "3":
            text_for_label = """Под тhwefwjyewdqwefwfqw2fewrggwefwe3f3, куда путь держишь?
              1 - на восток
              2 - на запад"""


    label.destroy()
    main(text_for_label)

main(text_for_label)