from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

import re
import configparser
import pyodbc

config = configparser.ConfigParser()
config.read("guisettings.ini")
bpath = config['base']['base_path']
# print(type(config['base']['base_path']))


def CopyPaste(e):
    if e.keycode == 86 and e.keysym != 'v':
        e.widget.event_generate('<<Paste>>')
    elif e.keycode == 67 and e.keysym != 'c':
        e.widget.event_generate('<<Copy>>')
    elif e.keycode == 88 and e.keysym != 'x':
        e.widget.event_generate('<<Cut>>')


def trakz():
    try:
        conn =  pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+base_path.get()+';')#C:\1amper\1amper_be.accdb;')
        cursor = conn.cursor()
        mailo = mails_text.get('1.0','end')
        x = re.findall("PC\\d{9}BY",mails_text.get('1.0','end'))
        # print(x)
        tracks_text.delete('1.0','end')
        for i in x:
            cursor.execute(f"UPDATE Zakaz SET Zakaz.zStatus = 2 WHERE [Zakaz]![zTrackNum]='*{i}*';")
            tracks_text.insert('1.0',i+' ')
        root.clipboard_clear()
        root.clipboard_append(tracks_text.get('1.0','end'))
        conn.commit()
        conn.close()
        showinfo(title="Трекномера", message="Состояние заказов изменено на 'Забрал'")
    except:
        popup = Tk()
        popup.geometry("300x100")
        popup.title("Ошибка!")
        erlabel = ttk.Label(popup,text="Не могу подключиться к базе", background='red', font='18')
        erlabel.pack(expand=True)
        popup.mainloop()
root = Tk()
root.title("Email'ы в треки")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky='nwes')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mails_text = Text(mainframe,width=25, height=15, bg='LightCyan2',
                   fg='black', wrap=WORD, font="18")


tracks_text = Text(mainframe,width=25, height=15, bg='LightCyan2', fg='black', wrap=WORD, font="18")
ttk.Button(mainframe, text="Извлечь треки", command=trakz).grid(column=2, row=2, sticky='we')

label = ttk.Label(mainframe,text="Путь к базе")
base_path = Entry(mainframe)

label.grid(row=1,column=1,sticky='e')
base_path.grid(row=1,column=2,columnspan=2,sticky='we')
base_path.insert(0,bpath)
mails_text.grid(row=2, column=1,rowspan=2)
tracks_text.grid(row=2, column=3,rowspan=2)
root.bind("<Control-Key>", CopyPaste) #s. тут указывает на Tk или CTk
root.mainloop()
