import codecs
import time
import tkinter.messagebox
from tkinter import *
from PIL import Image, ImageTk
import pygame, sys, random

pygame.mixer.init()
pygame.font.init()

right_ans = 0


def close_everything():
    pygame.quit()
    sys.exit()
    root.quit()


def save_all(name, aw_col, d, g):
    pygame.mixer.init()
    hoho = pygame.mixer.Sound("sounds/ben_hoho.wav")
    hoho.play()
    file_txt = codecs.open("all_results.txt", "a", encoding='utf-8')
    percent = round(s / aw_col, 3) * 100
    file_txt.write(
        str(name) + " | " + str(g) + " | " + str(s) + " | " + str(aw_col) + " | " + str(
            percent) + "%" + " | " + d + "\n")
    pygame.time.wait(2000)
    file_txt.close()
    close_everything()


def math_check(login, x1, x2, window3, size2):
    global s
    if int(login.get()) == x1 * x2:
        label2 = Label(window3, text="Отлично!", font="Courier 25", fg="green")
        label2.place(x=200, y=size2 - 100)
        print("попали!")
        yes = pygame.mixer.Sound("sounds/ben_yes.wav")
        yes.play()
        shotSound = pygame.mixer.Sound('sounds/vyistrel-7892.wav')
        shotSound.play()
        s += 1
    else:
        label2 = Label(window3, text="Ошибка!", font="Courier 25", fg="red")
        label2.place(x=200, y=size2 - 100)
        print("мимо!")
        no = pygame.mixer.Sound("sounds/ben_no.wav")
        no.set_volume(5)
        no.play()
        shotSound = pygame.mixer.Sound('sounds/vyistrel-7892.wav')
        shotSound.set_volume(0.4)
        shotSound.play()
    window3.update()
    pygame.time.wait(1500)
    window3.quit()
    window3.destroy()


def math_generation():
    print("Пытаемся попасть")
    window3 = Toplevel(root)
    window3.title("Скорее проведи рассчеты!")
    size1, size2 = 390, 200
    window3.geometry(f"{size1}x{size2}")
    window3.wm_geometry("+%d+%d" % (0, 0))

    zero = Label(text="")
    zero.pack(side=TOP)

    x1 = random.randint(2, 9)
    x2 = random.randint(2, 99)
    label = Label(window3, text=f"{x1} X {x2} = ?", font="Courier 43")
    label.place(x=0, y=0)

    login = tkinter.Entry(window3, font="Courier 30")
    login.insert(END, "0")
    login.place(x=0, y=size2 - 100, width=200, height=40)

    check_button = Button(window3, text='Проверить', fg='blue', font="Courier 10", width=48, height=2,
                          command=lambda: math_check(login, x1, x2, window3, size2))
    check_button.place(x=0, y=size2 - 40)

    window3.overrideredirect(1)
    window3.mainloop()


def Main(pik, name):
    global s, aw_col, t, g, tit1
    tit1 = time.time()
    window.withdraw()
    pygame.mixer.init()
    pygame.font.init()
    ben = pygame.mixer.Sound("sounds/ben_hihi.wav")
    ben.play()
    background = pygame.image.load('pictures/back2.jpg')
    window_w, window_h = background.get_size()
    print(pik, name)
    g = pik
    x = 0
    y = 0
    display = pygame.display.set_mode((window_w, window_h))
    pygame.display.set_caption("Pirat Elite")
    target = pygame.image.load('pictures/enemy.jpg')
    a, b = target.get_size()
    targetPosition = target.get_rect()
    targetPosition.bottom = random.randint(b // 2, window_h - (b // 2))
    targetPosition.left = random.randint(0, window_w - (a // 2))
    aw_col = 0
    s = 0
    pygame.mixer.music.load("sounds/mainTheme.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.03)

    while True:
        pygame.mouse.set_visible(0)
        fontScore = pygame.font.Font('Miratrix-Normal.otf', 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_everything()

            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    shot = pygame.Rect(x, y, 1, 1)
                    if shot.colliderect(targetPosition):
                        math_generation()
                        aw_col += 1
                        targetPosition.bottom = random.randint(b // 2, window_h - (b // 2))
                        targetPosition.left = random.randint(0, window_w - (a // 2))
                    else:
                        shotSound = pygame.mixer.Sound('sounds/vyistrel-7892.wav')
                        shotSound.play()
        if s == pik:
            pygame.quit()
            finish_form(name)

        score = fontScore.render(f"Счет:  {s}/{pik}", True, 'white')
        display.blit(background, (0, 0))
        display.blit(target, targetPosition)
        pygame.draw.line(display, (0, 0, 0), (x - 30, y), (x + 30, y), 2)
        pygame.draw.line(display, (0, 0, 0), (x, y - 30), (x, y + 30), 2)
        pygame.draw.circle(display, (0, 0, 0), (x + 1, y + 1), 15, 2)
        display.blit(score, (0, 0))
        pygame.display.update()


def restart_game(window4, d, name):
    window4.withdraw()
    pygame.mixer.init()
    hoho = pygame.mixer.Sound("sounds/ben_hoho.wav")
    hoho.play()
    file_txt = codecs.open("all_results.txt", "a", encoding='utf-8')
    percent = round(s / aw_col, 3) * 100
    file_txt.write(
        str(name) + " | " + str(g) + " | " + str(s) + " | " + str(aw_col) + " | " + str(
            percent) + "%" + " | " + d + "\n")
    pygame.time.wait(2000)
    pirat_said1(name)


def finish_form(name):
    tit2 = time.time()
    d0 = round(tit2 - tit1, 3)
    if d0 > 60:
        mins = d0 // 60
        secs = d0 - mins * 60
        d = str(round(mins)) + " мин " + str(round(secs)) + " сек"
    else:
        d = str(d0) + " сек"
    window4 = Toplevel(root)
    window4.title(f"Конец игры")
    size1, size2 = 700, 600
    window4.geometry(f"{size1}x{size2}")
    window4['bg'] = 'black'
    percent = round(s / aw_col, 4) * 100
    x = (window4.winfo_screenwidth() - window4.winfo_reqwidth()) / 2 - 200
    y = (window4.winfo_screenheight() - window4.winfo_reqheight()) / 2 - 200
    window4.wm_geometry("+%d+%d" % (x, y))
    label4 = Label(window4, text=f"""Поверить только! Ты спас всех нас от неприятеля!
{name}, как только мы вернемся в родные 
просторы, в твою честь устроим пир!

Твои результаты:
Уровень сложности - {g}
Получено примеров - {aw_col}
Верно решено - {s}
Процент корректных решений - {percent} %
Затрачено времени - {d}
 """, font="Courier 18", fg='white', bg='black', justify=LEFT)
    pirat4 = Image.open('pictures/microchel1.jpg')
    pirat4 = ImageTk.PhotoImage(pirat4)
    picture4 = Label(window4, image=pirat4, borderwidth=0)
    picture4.place(x=size1 - pirat4.width(), y=size2 - pirat4.height())
    label4.place(x=10, y=10)

    button_light = Button(window4, text='Сохранить результаты', width=25, height=2, bg="green", font="Courier 12 bold",
                          command=lambda: save_all(name, aw_col, d, g))
    button_light.place(x=50, y=size2 - 250)

    button_hard = Button(window4, text='Выйти без сохранения', width=25, height=2, bg="red", font="Courier 12 bold",
                         command=lambda: close_everything())
    button_hard.place(x=50, y=size2 - 175)

    button_restart = Button(window4, text='Сыграть еще раз', width=25, height=2, bg="yellow", font="Courier 12 bold",
                            command=lambda: restart_game(window4, d, name))
    button_restart.place(x=50, y=size2 - 100)
    window4.overrideredirect(1)
    window4.mainloop()


def log_pass(window1):
    global name
    zero = Label()
    zero.pack(side=TOP)
    zero = Label()
    zero.pack(side=TOP)

    label = Label(text="Как тебя зовут?")
    label.pack(side=TOP)

    login = Entry(window1)
    login.pack(side=TOP)

    check_button = Button(window1, text='Начать', command=lambda: pirat_said1(login.get()))
    check_button.pack(side=TOP)
    root.overrideredirect(1)
    root.mainloop()


def pirat_said1(name):
    global window
    pygame.mixer.init()
    root.withdraw()
    ben = pygame.mixer.Sound("sounds/ben.wav")
    ben.play()
    window = Toplevel(root)
    window.title(f"Правила игры для {name}")
    size1, size2 = 800, 550
    window.geometry(f"{size1}x{size2}")
    window['bg'] = 'black'
    x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2 - 200
    y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2 - 200
    window.wm_geometry("+%d+%d" % (x, y))
    label1 = Label(window, text="""Йо-Хо-Хо! Да у нас на корабле новенький!
Для начала посвящу тебя в курс дела: будешь у нас отвечать за
пристрелку орудия. На основании донесений разведчиков, на
нашей карте регулярно появляются места расположения вражеских
судов. Ты должен будешь прицельно стрелять по ним. Однако для
точного попадания необходимо будет провести некоторые
вычисления. Если ты правильно все расчитаешь, то снаряд
попадет точно в цель. Но времени на раздумья очень мало! Наш
корабль с мощной пушкой, но со слабой броней. Поторопись с
потоплением неприятельских судов, пока на дно не ушел наш.



Дело за малым: выбери размер флота, против
которого ты готов сразиться:""", font="Courier 15", fg='white', bg='black', justify=LEFT)
    pirat = Image.open("pictures/microchel1.jpg")
    pirat = ImageTk.PhotoImage(pirat)
    picture = Label(window, image=pirat, borderwidth=0)
    picture.place(x=size1 - pirat.width(), y=size2 - pirat.height())
    label1.place(x=10, y=8)

    button_light = Button(window, text='10\nКораблей', width=10, bg="green", height=5, font="Courier 10 bold",
                          command=lambda x=10: Main(x, name))
    button_light.place(x=50, y=size2 - 150)

    button_midle = Button(window, text='20\nКораблей', width=10, bg="yellow", height=5, font="Courier 10 bold",
                          command=lambda x=20: Main(x, name))
    button_midle.place(x=200, y=size2 - 150)

    button_hard = Button(window, text='30\nКораблей', width=10, bg="red", height=5, font="Courier 10 bold",
                         command=lambda x=30: Main(x, name))
    button_hard.place(x=350, y=size2 - 150)
    window.overrideredirect(1)
    window.mainloop()


def start_window():
    global root
    root = Tk()
    root.geometry("250x150")
    root.title("Знакомство")
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.wm_geometry("+%d+%d" % (x, y))
    log_pass(root)
    root.withdraw()
    # root.mainloop()


if __name__ == "__main__":
    start_window()
