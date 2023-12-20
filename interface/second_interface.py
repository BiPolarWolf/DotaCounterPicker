from db_operation.select_from_tables import *
from db_operation.delete_from_table import delete_from_hero_feature
from db_operation.update_tables import update_feature_description
from db_operation.insert_in_tables import (
                                           hero_insert,
                                           feature_insert,
                                           insert_hero_feature,insert_feature_vs_feature)
from CTk_icons import info_icon,delete_icon,add_icon,main_logo
from CTkMessagebox import CTkMessagebox
from main_interface import  Heroes_Scroll_Frame,Feature_list_frame

import customtkinter as CTk
CTk.set_appearance_mode('dark')


#Основное окно
class Counter_Picker(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.title('DotaCounterPicker')


        self.choice_hero_menu = Choice_hero_menu(self)
        self.choice_hero_menu.grid(row=0, column=0, sticky='nsew', padx=10,pady=(10,5))






# Главный фрейм в котором все находится
class Choice_hero_menu(CTk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.grid_rowconfigure((0,1,2,3),weight=1)

        #Первый самый левый фрейм - выбор персонажа
        self.hero_select_frame = CTk.CTkFrame(self)
        self.hero_select_frame.grid(row=0, column=0, sticky='new', padx=5, pady=(10, 5))
        self.hero_select_frame.grid_rowconfigure(1,weight=1)


        # ввод имени персонажа и открытие его способности через кнопку
        self.search_bar = CTk.CTkFrame(self.hero_select_frame)
        self.search_bar.grid(row=0, column=0, sticky='nsew', padx=10, pady=(10, 5))
        self.entry= CTk.CTkEntry(self.search_bar,placeholder_text='Кого Законтрить ?')
        self.entry.grid(column=0,row=0,sticky='nsew',padx=5,pady=(10,5))
        self.search_button = CTk.CTkButton(self.search_bar,text='Поиск',command=self.search,width=50)
        self.search_button.grid(column=1, row=0, sticky='nsew', padx=5, pady=(10, 5))

        #фрейм в котором будет список персонажей на выбор
        self.heroes_scroll_frame = Heroes_Scroll_Frame(self.hero_select_frame,width=150,height=410)
        self.heroes_scroll_frame.grid(row=1, column=0, sticky='nsew', padx=10,pady=(10,5))
        # Кнопка для выбора персонажа
        self.hero_choice_button = CTk.CTkButton(self.hero_select_frame,text='Выбрать',command=self.choice_hero)
        self.hero_choice_button.grid(row=2,column=0,sticky='nsew', padx=10,pady=10)

        #Второй фрейм в котором показываются способности выбранного персонажа , можно увидеть их описание
        self.hero_features_frame=CTk.CTkFrame(self)
        self.hero_features_frame.grid(row=0, column=1, sticky='new', padx=5, pady=(10, 5))
        self.hero_label = CTk.CTkLabel(self.hero_features_frame, text=f'Способности героев')
        self.hero_label.grid(row=0, column=0, sticky='new',)

        # скролл фрейм для вывода всех способностей выбранного персонажа (автоматический создается пустым)
        self.hero_features_scroll= Hero_Features_Frame(self.hero_features_frame,hero_features_list=[],width=250)
        self.hero_features_scroll.grid(row=1, column=0, sticky='new', padx=10,pady=10)


        # Кнопка которая выполняет функция get_description
        self.get_feauture_button = CTk.CTkButton(self.hero_features_frame, text='Подробнее о способности', image=info_icon,
                                                 command=self.get_description)
        self.get_feauture_button.grid(row=2, column=0, padx=10, pady=(0, 5), sticky='ew')


        # Текстовой блок в котором будет храниться описание для способности
        self.descr_feature = CTk.CTkTextbox(self.hero_features_frame, wrap='word', corner_radius=10, height=180)
        self.descr_feature.grid(row=3, column=0, padx=10, pady=(5,10), sticky='new')

        #Кнока которая выполняет функцию get_counter_features
        self.choice_lose_feature = CTk.CTkButton(self.hero_features_frame, text='Найти Контр-Способность',command=self.get_counter_features)
        self.choice_lose_feature.grid(row=4, column=0, padx=10, pady=(5,10), sticky='new')

        #Создается 3ий фрейм в котором будет выводится контр способности для выбранной способности
        self.winner_features_frame=CTk.CTkFrame(self,width=300)
        self.winner_features_frame.grid(row=0,column=2,sticky='new', padx=5, pady=10)

        #Лейбл в котором указана способность для которой подбираются ее контр способности
        self.loser_feature_label = CTk.CTkLabel(self.winner_features_frame, text=f'Контр способности')
        self.loser_feature_label.grid(row=0, column=0, sticky='new',padx=5, pady=5)

        # Скролл фрейм в котором будет выводит список контр способностей для выбранной способности
        self.counter_features = Winners_list_frame(self.winner_features_frame,features_list=[],width=250,height=200)
        self.counter_features.grid(row=1,column=0,sticky='new',padx=5, pady=5)

        # Кнопка которая выполняет функция get_winner_description
        self.get_feauture_button1 = CTk.CTkButton(self.winner_features_frame, text='Подробнее о способности',
                                                 image=info_icon,
                                                 command=self.get_winner_description)
        self.get_feauture_button1.grid(row=2, column=0, padx=10, pady=(0, 5), sticky='ew')

        # Текстовой блок в котором будет храниться описание для способности
        self.descr_feature1 = CTk.CTkTextbox(self.winner_features_frame, wrap='word', corner_radius=10, height=180)
        self.descr_feature1.grid(row=3, column=0, padx=10, pady=(5, 10), sticky='new')

        # Кнока которая выполняет функцию get_feature_heroes (находит всех персонажей с этой способностью)
        self.choice_feature_heroes = CTk.CTkButton(self.winner_features_frame, text='Герои со способностью',
                                                 command=self.get_feature_heroes)
        self.choice_feature_heroes.grid(row=4, column=0, padx=10, pady=(5, 10), sticky='new')

        #Фрейм для вывода списка Персонажей с выбранной способностью
        self.feature_heroes_frame = CTk.CTkFrame(self,width=300)
        self.feature_heroes_frame.grid(row=0,column=3,sticky='nsew', padx=5, pady=10)
        self.feature_heroes_frame.grid_rowconfigure(1,weight=1)

        #Заголовок в котором указана способность
        self.feature_heroes_label = CTk.CTkLabel(self.feature_heroes_frame, text=f'Герои со способностью')
        self.feature_heroes_label.grid(row=0, column=0, sticky='new', padx=5, pady=5)

        # Скролл Фрейм со списком Героев у которых есть эти способности
        self.winners_heroes_scroll = Winner_Heroes_frame(self.feature_heroes_frame,width=310,feature_id=0)
        self.winners_heroes_scroll.grid(row=1, column=0, sticky='news', padx=5, pady=5)


    # функция которая берет введенное пользователем имя и проверяет есть ли такой персонаж в баже , если есть
    # то выдает способности этого персонажа , если нет , то ничего не делает
    def search(self):
        entry_hero_name = self.entry.get()
        heroes = select_heroes()

        for id,name in heroes:
            if entry_hero_name == name:
                hero_id = id
                hero_info = select_hero_info(hero_id)
                self.hero_label.configure(text=f'Способности героя : {hero_info[1]}')

                # переменная в которой будет список способностей для персонажа с выбранным айди
                hero_features_list = select_hero_features1(hero_id=hero_id)
                self.hero_features_scroll = Hero_Features_Frame(self.hero_features_frame, hero_features_list, width=250)
                self.hero_features_scroll.grid(row=1, column=0, sticky='new', padx=10, pady=10)

    # Функция которая отвечает за выдачу описания контрящих способностей в текстбоксе
    def get_winner_description(self):
        feature_id = self.counter_features.get_feature_id()
        feature_info = select_feature_info(feature_id)
        self.descr_feature1.delete('0.0','end')
        self.descr_feature1.insert('0.0',feature_info[2])


    # Функция которая возвращает список контр способностей  для одной способноси и меняет текст лейбла
    def get_counter_features(self):
        loser_id = self.hero_features_scroll.get_choice_feature()
        loser_name = select_feature_info(loser_id )[1]
        features_list = select_winners_features(loser_id)
        self.counter_features = Winners_list_frame(self.winner_features_frame, features_list=features_list, width=250,height=200)
        self.counter_features.grid(row=1, column=0, sticky='new', padx=5, pady=5)
        self.loser_feature_label.configure(text=f'Контрят "{loser_name}"')

    # Функция которая отвечает за выдачу описания  способностей персонажа в текстбоксе
    def get_description(self):
        feature_id = self.hero_features_scroll.get_choice_feature()
        select_feature = select_feature_info(feature_id)
        self.descr_feature.delete('0.0','end')
        self.descr_feature.insert('0.0',select_feature[-1])

    # Функция которая выдает способности для выбранного персонажа и меняет текст лейбла для этого персонажа
    def choice_hero(self):
        hero_id = self.heroes_scroll_frame.get_hero_id()
        hero_info = select_hero_info(hero_id)
        self.hero_label.configure(text=f'Способности героя : {hero_info[1]}')

        # переменная в которой будет список способностей для персонажа с выбранным айди
        hero_features_list = select_hero_features1(hero_id=hero_id)
        self.hero_features_scroll= Hero_Features_Frame(self.hero_features_frame,hero_features_list,width=250)
        self.hero_features_scroll.grid(row=1, column=0, sticky='new', padx=10,pady=10)

    # выдает список Героев для выбранной способности и меняет текста Лейбла для этой способности
    def get_feature_heroes(self):
        feature_id = self.counter_features.get_feature_id()
        feature_info = select_feature_info(feature_id)
        self.feature_heroes_label.configure(text=f'Герои с {feature_info[1]}')

        self.winners_heroes_scroll = Winner_Heroes_frame(self.feature_heroes_frame, width=300, feature_id=feature_id)
        self.winners_heroes_scroll.grid(row=1, column=0, sticky='news', padx=5, pady=5)



#Класс фрейма в котором будут генерироваться способности которые контрят выбранную способность
class Winners_list_frame(CTk.CTkScrollableFrame):
    def __init__(self,master,features_list,width,height):
        super().__init__(master,width,height)
        self.Value_Var = CTk.IntVar(value=0)
        if len(features_list) !=0:
            for i, feature in enumerate(features_list):
                label = CTk.CTkRadioButton(self,text=f'"{feature[2]}" на {feature[1]} баллов ',value=feature[0],variable=self.Value_Var)
                label.grid(row=i,column=0,sticky='new',pady=5)
            if feature[1] in (1,2,3):
                label.configure()
            if feature[1] in(4,5):
                label.configure(text_color='#2EDB4B')
            elif feature[1] in(6,7):
                label.configure(text_color='#2EA4DB')
            elif feature[1] in (8,9):
                label.configure(text_color='#E63DF5')
            elif feature[1] == 10:
                label.configure(text_color='#F09B24')

            else:label.configure(text='Не найдено')
        else:
            None
    def get_feature_id(self):
        return self.Value_Var.get()


#Класс Фрейма в котором будут Генерироваться Герои с выбранной способностью
class Winner_Heroes_frame(CTk.CTkScrollableFrame):
    def __init__(self, master, feature_id,width):
        super().__init__(master,width)

        heroes = select_feature_heroes(feature_id)
        self.heroes_var =CTk.IntVar()
        for i, value in enumerate(heroes):

            '''
            Уровень 1 - белая запись : Значит что у Героя есть эта способность но особо важной роли она не играет
            Уровень 2 - зеленая запись : Значит что у Героя есть способность которая может приносить не большие трудности врагу
            Уровень 3 - голубая запись : Значит что у Героя есть способность которая может принести много проблем , стоит обратить на нее внимание
            Уровень 4 - розовая запись : Значит что у Героя есть способность которую нужно обязательно чем то перекрыть , иначе возрастает шанс проиграть
            Уровень 5 - оранжевая запись : Значит что у Героя есть способность которую если ничем не перекрыть , то вы проиграете
            '''

            # Радио кнопка которая хранит описание способности и передает значение в переменную self.selected_feature
            counter_hero_info = CTk.CTkLabel(self, text=f'{value[0]} - {value[1]} ({value[2]}-level)')
            counter_hero_info.grid(row=i, column=0, pady=5, sticky='nws')

            # Сдесь происходит цветовая кастомизация лейбла выше взависимости от уровня способности
            if value[-1] == 1:
                counter_hero_info.configure()
            if value[-1] == 2:
                counter_hero_info.configure(text_color='#2EDB4B')
            elif value[-1] == 3:
                counter_hero_info.configure(text_color='#2EA4DB')
            elif value[-1] == 4:
                counter_hero_info.configure(text_color='#E63DF5')
            elif value[-1] == 5:
                counter_hero_info.configure(text_color='#F09B24')


# Класса Фрейм в котором будут генерироваться способности для выбранного Героя
class Hero_Features_Frame(CTk.CTkScrollableFrame):
    def __init__(self,master,hero_features_list,width):
        super().__init__(master,width)

        # Переменаая хранящая значение выбранной радио кнопки из фрейма self.features_bar
        self.features_var = CTk.IntVar(value=0)

        # Перебор всех значений из списка hero_features_list и создания радио кнопок
        for i, value in enumerate(hero_features_list):

            '''
            Уровень 1 - белая запись : Значит что у Героя есть эта способность но особо важной роли она не играет
            Уровень 2 - зеленая запись : Значит что у Героя есть способность которая может приносить не большие трудности врагу
            Уровень 3 - голубая запись : Значит что у Героя есть способность которая может принести много проблем , стоит обратить на нее внимание
            Уровень 4 - розовая запись : Значит что у Героя есть способность которую нужно обязательно чем то перекрыть , иначе возрастает шанс проиграть
            Уровень 5 - оранжевая запись : Значит что у Героя есть способность которую если ничем не перекрыть , то вы проиграете
            '''

            # Радио кнопка которая хранит описание способности и передает значение в переменную self.selected_feature
            descr_button = CTk.CTkRadioButton(self, text=f'{value[2]} ({value[-1]}-level)',
                                              value=value[1], variable=self.features_var)
            descr_button.grid(row=i, column=0, pady=5, sticky='nws')

            # Сдесь происходит цветовая кастомизация лейбла выше взависимости от уровня способности
            if value[-1] == 1:
                descr_button.configure()
            if value[-1] == 2:
                descr_button.configure(text_color='#2EDB4B')
            elif value[-1] == 3:
                descr_button.configure(text_color='#2EA4DB')
            elif value[-1] == 4:
                descr_button.configure(text_color='#E63DF5')
            elif value[-1] == 5:
                descr_button.configure(text_color='#F09B24')

    def get_choice_feature(self):
        return self.features_var.get()


if __name__ == '__main__':
    counter_picker = Counter_Picker()
    counter_picker.mainloop()
