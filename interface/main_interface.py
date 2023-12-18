from db_operation.select_from_tables import *
from db_operation.delete_from_table import delete_from_hero_feature
from db_operation.update_tables import update_feature_description
from db_operation.insert_in_tables import (
                                           hero_insert,
                                           feature_insert,
                                           insert_hero_feature,insert_feature_vs_feature)
from CTk_icons import info_icon,delete_icon,add_icon,main_logo

from CTkMessagebox import CTkMessagebox
import customtkinter as CTk
CTk.set_appearance_mode('dark')




#Главный Фрейм
class Redactor_menu(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.title('DotaCounterPicker')

        #Меню для добавления Записей о способностях
        self.add_feature = Add_Feature(self)
        self.add_feature.grid(row=0,column=0,padx=(10,5),pady=10,sticky='nsew')

        #Меню с с скроллющимся списком персонажей и выбора одного из них чтобы показать его способности
        self.hero_features_menu = Hero_list(self)
        self.hero_features_menu.grid(row=0,column=1,padx=(5,5),pady=10,sticky='nsew')

        self.feature_vs_feature = Feature_vs_Feature(self)
        self.feature_vs_feature.grid(row=0, column=2, padx=(5, 10), pady=10, sticky='nsew')



class Heroes_Scroll_Frame(CTk.CTkScrollableFrame):
    def __init__(self,master,width,height):
        super().__init__(master,width,height)

        # Переменная для хранения айди Персонажа , которое определяется с помощью радио кнопок
        self.hero_id_var = CTk.IntVar(value=1)


        # функция  select_heroes выбирает все айди и имена для всех персонажей из таблицы Heroes
        heroes = select_heroes()

        # внутри фрейма heroes_frame создаются радио кнопки соответствующие персонажу
        # (информацию о выбранной кнопке будет хранить self.hero_id_var)
        for i, value in enumerate(heroes):
            radio_button = CTk.CTkRadioButton(self, text=value[1], value=value[0],
                                              variable=self.hero_id_var)
            radio_button.grid(row=i, column=0, sticky='new', padx=10, pady=5)

    def get_hero_id(self):
        return self.hero_id_var.get()


# фрейм для выборки персонажа
class Hero_list(CTk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        #Заголовок сверху находится выше всех
        self.title_label = CTk.CTkLabel(self,text='Способности Персонажей')
        self.title_label.grid(row=0,column=0,columnspan=3,sticky='new',pady=10)

        self.select_hero_frame = CTk.CTkFrame(self,width=150,height=300)
        self.select_hero_frame.grid(row=1, column=0,padx=(0,10), sticky='nsew')
        self.select_hero_frame.grid_rowconfigure(0,weight=1)
        #Фрейм в котором  перебираются все персонажи (фрейм с автоматическим скроллом)
        self.heroes_frame = Heroes_Scroll_Frame(self.select_hero_frame,width=150,height=300)
        self.heroes_frame.grid(row=0, column=0, sticky='nsew', padx=10,pady=(10,5))

        #кнопка которая вызывает функцию get_hero разположена внутри фрейм класса Hero_list
        self.get_hero_button = CTk.CTkButton(self.select_hero_frame,text='Выбрать',command=self.get_hero)
        self.get_hero_button.grid(row=1,column=0,sticky='new',padx=5,pady=5)



    # Функция которая создает фрейм для отображения способностей персонажа
    def get_hero(self):

        # Функция получает айди персонажа из hero_id_var.get() в переменную hero_id
        hero_id = self.heroes_frame.get_hero_id()

        # далее вызываем функцию select_hero_info(hero_id) которая по айди достает всю информацию о персонаже
        hero_info = select_hero_info(hero_id)

        # создается Экземпляр класса Hero_features_menu который является новым фреймом для отображения способностей персонажа
        self.hero_feature_frame = Hero_features_menu(self,hero=hero_info)
        self.hero_feature_frame.grid(row=1, column=1,padx=(0,10), sticky='new')

        self.insert_feature_to_Hero = Insert_Feature_to_Hero(self,hero_id)
        self.insert_feature_to_Hero.grid(row=1, column=2, padx=(0, 10), sticky='new')


class Hero_features_menu(CTk.CTkFrame):
    def __init__(self,master,hero):
        super().__init__(master)
        #Лейбл для заголовка
        self.hero = hero
        self.hero_label = CTk.CTkLabel(self,text=f'Способности героя : {self.hero[1]}')
        self.hero_label.grid(row=0,column=0,sticky='new')

        # Скроллбар фрейм в котором будут храниться все способности выбранного персонажа  в виде радио кнопок
        self.features_bar = CTk.CTkScrollableFrame(self,width=270, height=200)
        self.features_bar.grid(row=1,column=0,sticky='new',padx=10,pady=5)

        #переменная в которой будет список способностей для персонажа с выбранным айди
        hero_features_list = select_hero_features1(hero_id=self.hero[0])

        #Переменаая хранящая значение выбранной радио кнопки из фрейма self.features_bar
        self.features_var = CTk.IntVar(value=0)


        #Перебор всех значений из списка hero_features_list и создания радио кнопок
        for i,value in enumerate(hero_features_list):

            '''
            Уровень 1 - белая запись : Значит что у Героя есть эта способность но особо важной роли она не играет
            Уровень 2 - зеленая запись : Значит что у Героя есть способность которая может приносить не большие трудности врагу
            Уровень 3 - голубая запись : Значит что у Героя есть способность которая может принести много проблем , стоит обратить на нее внимание
            Уровень 4 - розовая запись : Значит что у Героя есть способность которую нужно обязательно чем то перекрыть , иначе возрастает шанс проиграть
            Уровень 5 - оранжевая запись : Значит что у Героя есть способность которую если ничем не перекрыть , то вы проиграете
            '''



            # Радио кнопка которая хранит описание способности и передает значение в переменную self.selected_feature
            descr_button = CTk.CTkRadioButton(self.features_bar,text=f'{value[2]} ({ value[-1]}-level)',
                                              value=value[1],variable=self.features_var)
            descr_button.grid(row=i,column=0,pady=5 ,sticky='nws')

            # Сдесь происходит цветовая кастомизация лейбла выше взависимости от уровня способности
            if value[-1] ==1:
                descr_button.configure()
            if value[-1] == 2:
                descr_button.configure(text_color='#2EDB4B')
            elif value[-1] ==3:
                descr_button.configure(text_color='#2EA4DB')
            elif value[-1] ==4:
                descr_button.configure(text_color='#E63DF5')
            elif value[-1] ==5:
                descr_button.configure(text_color='#F09B24')


        # Кнопка которая вызывает функцию get_description
        self.get_feauture_button = CTk.CTkButton(self,text='Подробнее о способности' ,image=info_icon,command=self.get_description)
        self.get_feauture_button.grid(row=2,column=0,padx=10,pady=(0,5),sticky='ew')

        # Текстовой блок в котором будет храниться описание для способности
        self.descr_feature = CTk.CTkTextbox(self,wrap='word',corner_radius=10,height=180)
        self.descr_feature.grid(row=3,column=0,padx=10,pady=(0,5),sticky='new')

        # Кнопка на случай желания поменять описание способности в базе данных
        self.update_feature_button = CTk.CTkButton(self, text='Обновить описание', command=self.update_feature_descr)
        self.update_feature_button.grid(row=4, column=0, sticky='new', pady=5, padx=(10, 10))

        self.delete_feature_button = CTk.CTkButton(self, text='Убрать способность', image=delete_icon, command=self.delete_hero_feature)
        self.delete_feature_button.grid(row=5, column=0, sticky='new', pady=5, padx=(10, 10))
        self.delete_feature_button.configure(fg_color='#FF6347')
    #Функция делает запрос на обновление поля Description для выбранной способности
    def update_feature_descr(self):
        feature_id = self.features_var.get()
        feature_info = select_feature_info(feature_id)
        name = feature_info[1]
        description = self.descr_feature.get('0.0','end')

        update_feature_description(name,description)
        CTkMessagebox(title="Обновлено", message=f'Описание способности "{name}" было обновлено !'
                                                 f'\n Чтобы изменения появились перевыберите персонажа ', icon="check")

    def delete_hero_feature(self):
        hero_id = self.hero[0]
        feature_id =self.features_var.get()

        feature_info = select_feature_info(feature_id)
        name = feature_info[1]
        delete_from_hero_feature(hero_id,feature_id)
        CTkMessagebox(title="Удалено", message=f'У Героя была убрана способность "{name}"'
                                                 f'\n Чтобы изменения появились перевыберите персонажа ', icon="cancel")




    # Функция удаляет предыдущее записанное в текстовом боксе ,
    # берет описание из переменной которая хранит описание для выбранной
    # радио кнопки и записывает это описание в текстовой бокс
    def get_description(self):
        self.descr_feature.delete('0.0', 'end')
        feature_id = self.features_var.get()
        feature_info = select_feature_info(feature_id)
        feature_description = feature_info[2]
        self.descr_feature.insert('0.0',feature_description)



#Фрейм для добавления способности в базу данных
class Add_Feature(CTk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        # Лейбл с заголовком и настройкой заднего фона
        self.title_label = CTk.CTkLabel(self, text='Добавить Оссобенность')
        self.title_label.grid(row=0, column=0, padx=0, pady=0,columnspan=2, sticky='nsew')
        self.title_label.configure(fg_color='#606060')

        # Лейбл подсказка для окна ввода
        self.label = CTk.CTkLabel(self,text='Название :')
        self.label.grid(row=1,column=0,padx=10,pady=20)

        # Поле для ввода названия новой способности
        self.entry = CTk.CTkEntry(self)
        self.entry.grid(row=1,column=1,padx=(0,10),pady=20)

        # Лейбл подсказка для Текстового Бокса который нужен для добавления Описания способности
        self.label_descr=CTk.CTkLabel(self,text='Описание',bg_color='gray')
        self.label_descr.grid(row=2,column=0,columnspan=2,padx=10,sticky='new')

        # ТекстБокс для заполнения описания новой способности
        self.descr = CTk.CTkTextbox(self,wrap='word',corner_radius=0,height=180)
        self.descr.grid(row=3,column=0,columnspan=2,padx=10,pady=(0,5),sticky='new')

        # Кнопка для вызоыва функцию self.add_feature
        self.add_button = CTk.CTkButton(self,text='Добавить',command=self.insert_feature)
        self.add_button.grid(row=4,column=0,columnspan=2,padx=10,pady=10,sticky='new')

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(5,weight=1)
        self.logo_label = CTk.CTkLabel(self,image=main_logo,text='')
        self.logo_label.grid(row=5,column=0,columnspan=2,padx=(10,5),pady=10)

    # Функция для добавления вписанных данных из текстовых полей в качестве новой записи  в таблицу Features базы данных
    # Также функция вызывает всплывающее окно указывающее на то что способность успешно добавлена
    # После поля для Названия и Текстовой бокс очищаются от ранее вписанных данных
    def insert_feature(self):
        name = self.entry.get()
        descr = self.descr.get("0.0",'end')
        feature_info = [name,descr]
        feature_insert(feature_info)
        CTkMessagebox(title="Способность добавлена", message=f'Способность "{name}" успешно добавлена ! ',icon="check")
        self.entry.delete('0','end')
        self.descr.delete('0.0','end')



class Feature_list_frame(CTk.CTkScrollableFrame):
    def __init__(self,master,features_list):
        super().__init__(master)
        self.Value_Var = CTk.IntVar(value=0)
        for i, feature in enumerate(features_list):
            label = CTk.CTkRadioButton(self,text=f'"{feature[1]}"',value=feature[0],variable=self.Value_Var)
            label.grid(row=i,column=0,sticky='new',pady=5)


    def get_feature_id(self):
        return self.Value_Var.get()

class Insert_Feature_to_Hero(CTk.CTkFrame):
    def __init__(self,master,hero_id):
        super().__init__(master)
        self.hero_id = hero_id
        self.grid_columnconfigure(0,weight=1)
        self.title_label = CTk.CTkLabel(self,text='Назначить способность герою')
        self.title_label.grid(row=0,column=0,padx=10,sticky='ew')

        features_list = select_features()
        self.choice_feature_frame = Feature_list_frame(self,features_list)
        self.choice_feature_frame.grid(row=1,column=0,pady=5,padx=10,sticky='new')

        # Кнопка которая вызывает функцию get_description
        self.get_feauture_button = CTk.CTkButton(self,text='Подробнее о способности' ,image=info_icon,command=self.get_description)
        self.get_feauture_button.grid(row=2,column=0,padx=10,pady=(0,5),sticky='ew')

        # Текстовой блок в котором будет храниться описание для способности
        self.descr_feature = CTk.CTkTextbox(self,wrap='word',corner_radius=10,height=180)
        self.descr_feature.grid(row=3,column=0,padx=10,pady=(0,5),sticky='new')


        self.SliderVar = CTk.IntVar(value=1)
        self.slider = CTk.CTkSlider(self, from_=1, to=5,number_of_steps=4, variable=self.SliderVar,command=self.slider_event)
        self.slider.grid(row=4,column=0,pady=5,padx=10,sticky='new')

        self.level_label = CTk.CTkLabel(self, text='Уровень 1')
        self.level_label.grid(column=0, row=5, padx=10, pady=5, sticky='ew',)

        # Кнопка которая вызывает функцию get_description
        self.get_feauture_button = CTk.CTkButton(self,text='Добавить способность' ,image=add_icon,command=self.install_feature)
        self.get_feauture_button.grid(row=6,column=0,padx=10,pady=(0,5),sticky='ew')
        self.get_feauture_button.configure(fg_color='#6B8E23')

    def install_feature(self):
        feature_id = self.choice_feature_frame.get_feature_id()
        level = self.SliderVar.get()
        hero_id =self.hero_id
        insert_hero_feature(hero_id,feature_id,level)
        CTkMessagebox(title="Способность добавлена", message=f'Способность успешно добавлена ! ',icon="check")


    def get_description(self):
        self.descr_feature.delete('0.0', 'end')
        feature_id =self.choice_feature_frame.get_feature_id()
        feature_description = select_feature_info(feature_id)[2]
        self.descr_feature.insert('0.0',feature_description)

    def slider_event(self,value):
        if value == 1:
            self.level_label.configure(text='Способность 1 уровня' ,text_color='#FFFFE0')
        elif value == 2:
            self.level_label.configure(text_color='#2EDB4B', text='Способность 2 уровня')
        elif value == 3:
            self.level_label.configure(text_color='#2EA4DB', text='Способность 3 уровня')
        elif value == 4:
            self.level_label.configure(text_color='#E63DF5', text='Способность 4 уровня')
        elif value == 5 :
            self.level_label.configure(text_color='#F09B24', text='Способность 5 уровня')




class Feature_vs_Feature(CTk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)

        self.win_feature = 0
        self.lose_feature = 0

        self.main_title = CTk.CTkLabel(self,text='Установить контр способность')
        self.main_title.grid(column=0,row=0,sticky='ew',pady=5,padx=10)
        self.main_frame = CTk.CTkFrame(self)
        self.main_frame.grid(column=0,row=1,sticky='news',pady=5,padx=10)

        self.main_frame.grid_rowconfigure(0,weight=1)

        feature_list = select_features()
        self.features_scroll_frame = Feature_list_frame(self.main_frame,feature_list)
        self.features_scroll_frame.grid(column=0,row=0,sticky='news',pady=5,padx=10)

        self.win_label = CTk.CTkLabel(self.main_frame,text='')
        self.win_label.grid(column=0,row=1,sticky='news',pady=5,padx=10)
        self.win_label.configure(text_color='#6B8E23')

        self.win_feature_button = CTk.CTkButton(self.main_frame,text='Выбрать способность победителя',command=self.get_win_feature)
        self.win_feature_button.grid(row=2,column=0,padx=10,pady=(0,5),sticky='ew')
        self.win_feature_button.configure(fg_color='#6B8E23')


        self.lose_label = CTk.CTkLabel(self.main_frame, text='')
        self.lose_label.grid(column=0, row=3, sticky='news', pady=5, padx=10)
        self.lose_label.configure(text_color='#FF6347')

        self.lose_feature_button = CTk.CTkButton(self.main_frame, text='Выбрать способность проигравшего', command=self.get_lose_feature)
        self.lose_feature_button.grid(row=4, column=0, padx=10, pady=(0, 5), sticky='ew')
        self.lose_feature_button.configure(fg_color='#FF6347')

        self.SliderVar = CTk.IntVar(value=0)
        self.slider = CTk.CTkSlider(self.main_frame, from_=0, to=10,number_of_steps=10, variable=self.SliderVar,command=self.slider_event)
        self.slider.grid(row=5,column=0,pady=5,padx=10,sticky='new')

        self.strong_number_label = CTk.CTkLabel(self.main_frame,text='')
        self.strong_number_label.grid(row=6,column=0,pady=5,padx=10,sticky='new')

        self.add_to_db_button = CTk.CTkButton(self.main_frame,text='Добавить в базу данных',command=self.add_feature_vs_feature)
        self.add_to_db_button.grid(row=7,column=0,pady=5,padx=10,sticky='new')

    def add_feature_vs_feature(self):
        win_id = self.win_feature
        lose_id = self.lose_feature
        strong = self.SliderVar.get()
        insert_feature_vs_feature(win_id,lose_id,strong)
        self.win_feature=0
        self.lose_feature=0
        self.SliderVar.set(0)

    def slider_event(self,value):
        self.strong_number_label.configure(text=f'Сила превосходства : {int(value)} ')


    def get_win_feature(self):
        win_feature_id = self.features_scroll_frame.get_feature_id()
        feature_name = select_feature_info(win_feature_id)[1]
        self.win_label.configure(text=feature_name)
        self.win_feature = win_feature_id


    def get_lose_feature(self):
        lose_feature_id = self.features_scroll_frame.get_feature_id()
        feature_name = select_feature_info(lose_feature_id)[1]
        self.lose_label.configure(text=feature_name)
        self.lose_feature = lose_feature_id


if __name__ == '__main__':
    main = Redactor_menu()
    main.mainloop()