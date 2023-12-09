import sqlite3
import tkinter
from tkinter.scrolledtext import ScrolledText

table_list = ['Heroes','Roles','HeroRoles']
class InsertMenu():
    def __init__(self):

        # создание главного окна
        self.main_window = tkinter.Tk()

        # Лейбл подсказка будет выше листбокса и фрейма как заголовок
        self.title = tkinter.Label(self.main_window, text='Список Таблиц')

        # создание фрейма для размещения листбокса с списом таблиц в базе
        self.tables_frame = tkinter.Frame(self.main_window,borderwidth=2,relief='ridge')

        #создается объект listvariable хранящий список для внесение его в листбокс
        self.tables = tkinter.Variable(value=table_list)

        # создается лист бокс с уже вложенным списком таблиц и скроллбар для этого листбокса
        self.table_list = tkinter.Listbox(self.tables_frame,listvariable=self.tables,height=4)
        self.table_scroll = tkinter.Scrollbar(self.tables_frame)

        #идет настройка взаимодействия листбокса и скроллбара (связка)
        self.table_list.config(yscrollcommand=self.table_scroll.set)
        self.table_scroll.config(command=self.table_list.yview)


        # упаковывается все штуки
        self.table_list.pack(side='left',)
        self.table_scroll.pack(side='right',fill=tkinter.Y)
        self.title.pack(side='top', padx=10, pady=10)
        self.tables_frame.pack(side='top',padx=10,pady=(0,10))

        tkinter.mainloop()

# создание записи в таблице Heroes
class Insert_in_Heroes:
    def __init__(self):

        # создание главного окна
        self.main_window = tkinter.Tk()
        # Заголовок выше всех фреймов будет
        self.title = tkinter.Label(self.main_window,text='Добавить в таблицу "Heroes"')


        # Фрейм в котором будет показана информация которую ввел пользователь
        self.get_frame = tkinter.Frame(self.main_window,relief='sunken',borderwidth=3)
        # Фрейм в котором пользователь будет вводить данные
        self.post_frame = tkinter.Frame(self.main_window,relief='sunken',borderwidth=3)


        # создается фрейм для ввода имени персонажа
        self.post_name_frame = tkinter.Frame(self.post_frame)
        self.post_name_label = tkinter.Label(self.post_name_frame,text='Введите Имя :')
        self.name_entry = tkinter.Entry(self.post_name_frame,)
        self.update_name = tkinter.Button(self.post_frame,text='Обновить имя',command=self.display_name)



        # создаются в новом фрейме 2 лейбла один как описание другой хранит значение имени
        # создаются фрейм для фрейма get_frame в нем будет показано введенное имя
        self.name_frame =tkinter.Frame(self.get_frame)
        self.name_label_prompt= tkinter.Label(self.name_frame,text='Имя : ')
        self.get_name = tkinter.StringVar(value='Неизвестно')
        self.name_label_value = tkinter.Label(self.name_frame,textvariable=self.get_name)



        # создаются в новом фрейме 2 лейбла один как описание другой хранит значение аттрибута
        self.attribute_frame= tkinter.Frame(self.get_frame)
        self.attribute_label_prompt = tkinter.Label(self.attribute_frame,text='Аттрибут : ')
        self.get_attr = tkinter.StringVar(value='Сила')
        self.attribute_label_value = tkinter.Label(self.attribute_frame,textvariable=self.get_attr)



        # создаются в новом фрейме 2 лейбла один как описание другой хранит описание персонажа
        self.descr_frame = tkinter.Frame(self.get_frame)
        self.descr_label_prompt = tkinter.Label(self.descr_frame,text='Описание : ')
        self.get_descr = tkinter.StringVar(value='Описание Персонажа')
        self.descr_label_value = tkinter.Label(self.descr_frame,textvariable=self.get_descr)




        # создаются фрейм с лейблом и четырьмя радио кнопками для установления аттрибутта персонажу.
        self.post_attribute_frame = tkinter.Frame(self.post_frame,bg='gray')
        self.post_attribute_title = tkinter.Label(self.post_frame,text='Выберите аттрибут Героя :')
        self.choice_attribute = tkinter.IntVar()
        self.choice_attribute.set(1)
        self.choice_red = tkinter.Radiobutton(self.post_frame,text='Сила',variable=self.choice_attribute,value=1,command=self.display_choice)
        self.choice_green = tkinter.Radiobutton(self.post_frame,text='Ловкость',variable=self.choice_attribute,value=2,command=self.display_choice)
        self.choice_blue = tkinter.Radiobutton(self.post_frame,text='Магия',variable=self.choice_attribute,value=3,command=self.display_choice)
        self.choice_all = tkinter.Radiobutton(self.post_frame,text='Универсальный',variable=self.choice_attribute,value=4,command=self.display_choice)


        self.post_description = tkinter.scrolledtext.ScrolledText(self.post_frame,width=30,height=10,wrap = tkinter.WORD,bg='green',fg='white')
        self.get_descr_button = tkinter.Button(self.post_frame,text='Обновить Описание Персонажа',command=self.get_text)


        self.insert_frame = tkinter.Frame(self.main_window,bg='orange').pack(side='bottom',padx=10,pady=10)
        self.insert_button = tkinter.Button(self.insert_frame,text='Добавить в базу данных').pack(side = 'bottom',pady=10)


        self.title.pack(side='top',pady=5,padx=10)
        self.get_frame.pack(side='top',pady=10)
        self.name_frame.pack(side='top',padx=18)
        self.name_label_prompt.pack(side='left')
        self.name_label_value.pack(side='left')


        self.attribute_frame.pack(side='top',padx=18)
        self.attribute_label_prompt.pack(side='left')
        self.attribute_label_value.pack(side='left')


        self.descr_frame.pack(side='top',padx=18)
        self.descr_label_prompt.pack(side='top')
        self.descr_label_value.pack(side='top')



        self.post_frame.pack(side='top')
        self.post_name_frame.pack(side='top',pady=10,padx=10)
        self.post_name_label.pack(side='left')
        self.name_entry.pack(side='left')

        self.update_name.pack(side='top',pady=(0,10))

        self.post_attribute_frame.pack(side='top')
        self.post_attribute_title.pack(side='top')
        self.choice_red.pack(side='top')
        self.choice_green.pack(side='top')
        self.choice_blue.pack(side='top')
        self.choice_all.pack(side='top')


        self.post_description.pack(side='top')
        self.get_descr_button.pack(side='top',pady=10)

        tkinter.mainloop()


# Функция для отображения выбора аттрибута в get_frame
    def display_choice(self):
        choice = self.choice_attribute.get()

        if choice == 1:
            choice = 'Сила'
        elif choice == 2:
            choice = 'Ловкость'
        elif  choice == 3:
            choice = 'Магия'
        elif choice ==4:
            choice = 'Универсальный'


        self.get_attr.set(choice)


    #Функция которая берет значение из ентри виджета и загружает его в StrVar а потом в лейбл  в get_frame (для имени)
    def display_name(self):
        name =  self.name_entry.get()
        self.get_name.set(name)


    def get_text(self):
        text = self.post_description.get('1.0',tkinter.END)
        self.get_descr.set(text)
        print(text.strip())




if __name__ == '__main__':
    insertMenu = InsertMenu()
    insert_in_Heroes = Insert_in_Heroes()