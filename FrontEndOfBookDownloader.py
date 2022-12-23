# Импортируем библиотеки
import time
import tkinter
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox, filedialog
from tkinter.ttk import Radiobutton
from tkinter import scrolledtext
import tkinter.ttk as ttk
import BackEndOfBookDownloader
import threading
txt = ""
txtPath = ""
thrBE = ""

# Базовые настройки
window = Tk()
window.title("Book downloader")
window.iconbitmap(r'Book.ico')
window.geometry('300x300')
window.resizable(False, False)
tab_control = ttk.Notebook(window)
tab_control.pack(expand=1, fill='both')

# Создание 2-x вкладок меню
home = ttk.Frame(tab_control)
settings = ttk.Frame(tab_control)

tab_control.add(home, text='Главная')
tab_control.add(settings, text='Настройки')

chkState = IntVar()
chkState.set(1)
chk = Checkbutton(settings, text='Нумерация книг', variable=chkState)
chk.place(x=150, y=30)


def InsertText(Txt):
    global txt
    txt.config(state="normal")
    txt.insert(INSERT, f"{Txt}\n")
    txt.config(state="disabled")


def a():
    print(chkState.get())


def Progarmm():
    global txt

    BackEndOfBookDownloader.MakeSoft()
    BackEndOfBookDownloader.DownloadProgramm()

    thrBE = ""

    # Функция Дефокуса, позваляет убрать выделение(фокус)
    def defocus(event):
        event.widget.master.focus_set()


    def StopDownload():
        messageStopDownload = messagebox.askyesno('BookDownloader', 'Вы действительно хотите\n прекратить загрузку книг')

        if messageStopDownload:

            BackEndOfBookDownloader.Stop()

            comboAudio.config(state="readonly")
            spinNum.config(state="readonly")

            btnStopDownload.place_forget()
            btnProceed.place_forget()
            btnStop.place_forget()

            btnStart.place(x=195, y=105)



            return True
        elif not messageStopDownload:
            return False




    def Proceed():

        btnProceed.place_forget()
        btnStop.place(x=170, y=105)

        return True


    def Stop():
        BackEndOfBookDownloader.Stop()

        btnStop.place_forget()
        btnProceed.place(x=165, y=105)


    def SearchPath():
        global txtPath


        Dir = filedialog.askdirectory()

        txtPath = StringVar(settings)
        txtPath.set(Dir)

        TxtPath = Entry(settings, textvariable=txtPath, width=30)
        TxtPath.place(x=20, y=100)


    def Start():
        global thrBE
        global txtPath



        try:
            if txtPath.get() == "":
                messagebox.showinfo('Book downloader', 'Укажите путь для загрузки '
                                                       'книг в настройках')
        except:
            messagebox.showinfo('Book downloader', 'Укажите путь для загрузки '
                                                   'книг в настройках')

        else:

            if comboAudio.get() == " Dark Puffin Cafe ":

                messagebox.showinfo("Book downloader", "Канал Dark Puffin Cafe недоступен\n данная функция в разработке")
            else:


                comboAudio.config(state="disabled")
                spinNum.config(state="disabled")

                btnStart.place_forget()
                btnStopDownload.place(x=120, y=105)
                btnStop.place(x=170, y=105)


                thrBE = threading.Thread(target=BackEndOfBookDownloader.DownloadBooks,
                                         args=(spinNum.get(), fr"{txtPath.get()}", chkState.get()))

                thrBE.start()

                thrCheckFinish = threading.Thread(target=CheckFinish)
                thrCheckFinish.start()



    def CheckFinish():
        global thrBE
        stop = False

        while not stop:
            if thrBE.is_alive():
                pass
            else:

                stop = True

                comboAudio.config(state="readonly")
                spinNum.config(state="readonly")

                btnStopDownload.place_forget()
                btnProceed.place_forget()
                btnStop.place_forget()

                btnStart.place(x=195, y=105)


    # Обьявляю переменную которая помогает создать вкладки меню


    # Вкладка Главная

    # Создание и расположение текста
    lblAudio = Label(home, text="Канал для скачивания книг:", font=("Arial Bold", 11))
    lblAudio.place(x=20, y=5)

    # Создание виджета combobox
    comboAudio = Combobox(home, state="readonly", width=19)
    comboAudio['values'] = (" Гарри Стил ", " Dark Puffin Cafe ")
    comboAudio.current(0)
    comboAudio.place(x=23, y=30)

    # Консоль
    txt = scrolledtext.ScrolledText(home, width=30, height=7, state="disabled")
    txt.place(x=20, y=150)

    # Вставка текста в Консоль
    txt.insert(INSERT, 'Амогус\n')

    # Текст
    lblNum = Label(home, text="Количество книг для загрузки:", font=("Arial Bold", 11))
    lblNum.place(x=20, y=75)

    # Spinbox для чисел
    spinNum = Spinbox(home, from_=3, to=50, width=5, state="readonly")
    spinNum.place(x=23, y=95)


    # Текст
    lblLanguage = Label(settings, text="Язык:", font=("Arial Bold", 10))
    lblLanguage.place(x=23, y=5)

    # Переменная для выбора варианта
    R = tkinter.IntVar()
    R.set(1)

    # Два RadioButton
    Rus = Radiobutton(settings, text='Русский', value=1, variable=R)
    Eng = Radiobutton(settings, text='English', value=2, variable=R)
    Rus.place(x=20, y=30)
    Eng.place(x=20, y=50)

    # Бинд на дефокус
    Rus.bind("<FocusIn>", defocus)
    Eng.bind("<FocusIn>", defocus)
    chk.bind("<FocusIn>", defocus)
    chk.bind(a)
    comboAudio.bind("<FocusIn>", defocus)
    # Текст
    lblPath = Label(settings, text="Папка для загрузки книг:", font=("Arial Bold", 10))
    lblPath.place(x=20, y=80)

    # Виджет который создает текстовое поле в настройках
    txtPath = Entry(settings, width=30)
    txtPath.place(x=20, y=100)

    lblSort = Label(settings, text="Сортировка:", font=("Arial Bold", 10))
    lblSort.place(x=153, y=5)

    btnSerachPath = Button(settings, text="Найти", command=SearchPath)
    btnSerachPath.place(x=203, y=97)

    btnStart = Button(home, text="Старт", command=Start)
    btnStart.place(x=175, y=105)

    btnProceed = Button(home, text="Продолжить", command=Proceed)
    btnStop = Button(home, text="Остановить", command=Stop)
    btnStopDownload = Button(home, text="Стоп", command=StopDownload)

    window.mainloop()
