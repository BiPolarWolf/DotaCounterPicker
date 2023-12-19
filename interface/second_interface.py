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

class Counter_Picker(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.title('DotaCounterPicker')


        self.choice_hero_menu = Choice_hero_menu(self)
        self.choice_hero_menu.grid(row=0, column=0, sticky='nsew', padx=10,pady=(10,5))


class Search_bar(CTk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.entry= CTk.CTkEntry(self,placeholder_text='Кого Законтрить ?')
        self.entry.grid(column=0,row=0,sticky='nsew',padx=5,pady=(10,5))
        global text
        self.search_button = CTk.CTkButton(self,text='Поиск',command=self.search)
        self.search_button.grid(column=1, row=0, sticky='nsew', padx=5, pady=(10, 5))

    def search(self):
        return self.entry.get()



class Choice_hero_menu(CTk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.grid_rowconfigure((0,1,2,3),weight=1)
        self.hero_select_frame = CTk.CTkFrame(self)
        self.hero_select_frame.grid(row=0, column=0, sticky='new', padx=5, pady=(10, 5))
        self.hero_select_frame.grid_rowconfigure(1,weight=1)
        self.search_bar = Search_bar(self.hero_select_frame)
        self.search_bar.grid(row=0, column=0, sticky='nsew', padx=10, pady=(10, 5))
        self.heroes_scroll_frame = Heroes_Scroll_Frame(self.hero_select_frame,width=150,height=410)
        self.heroes_scroll_frame.grid(row=1, column=0, sticky='nsew', padx=10,pady=(10,5))

        self.hero_choice_button = CTk.CTkButton(self.hero_select_frame,text='Выбрать',command=self.choice_hero)
        self.hero_choice_button.grid(row=2,column=0,sticky='nsew', padx=10,pady=10)

        self.hero_features_frame=CTk.CTkFrame(self)
        self.hero_features_frame.grid(row=0, column=1, sticky='new', padx=5, pady=(10, 5))
        self.hero_label = CTk.CTkLabel(self.hero_features_frame, text=f'Способности героев')
        self.hero_label.grid(row=0, column=0, sticky='new',)

        self.hero_features_scroll= Hero_Features_Frame(self.hero_features_frame,hero_features_list=[],width=250)
        self.hero_features_scroll.grid(row=1, column=0, sticky='new', padx=10,pady=10)


        self.get_feauture_button = CTk.CTkButton(self.hero_features_frame, text='Подробнее о способности', image=info_icon,
                                                 command=self.get_description)
        self.get_feauture_button.grid(row=2, column=0, padx=10, pady=(0, 5), sticky='ew')


        # Текстовой блок в котором будет храниться описание для способности
        self.descr_feature = CTk.CTkTextbox(self.hero_features_frame, wrap='word', corner_radius=10, height=180)
        self.descr_feature.grid(row=3, column=0, padx=10, pady=(5,10), sticky='new')


        self.choice_lose_feature = CTk.CTkButton(self.hero_features_frame, text='Найти Контр-Способность',command=self.get_counter_features)
        self.choice_lose_feature.grid(row=4, column=0, padx=10, pady=(5,10), sticky='new')

        self.winner_features_frame=CTk.CTkFrame(self,width=300)
        self.winner_features_frame.grid(row=0,column=2,sticky='new', padx=5, pady=10)

        self.loser_feature_label = CTk.CTkLabel(self.winner_features_frame, text=f'Контр способности')
        self.loser_feature_label.grid(row=0, column=0, sticky='new',padx=5, pady=5)

        self.counter_features = Winners_list_frame(self.winner_features_frame,features_list=[],width=250,height=200)
        self.counter_features.grid(row=1,column=0,sticky='new',padx=5, pady=5)



        self.get_feauture_button1 = CTk.CTkButton(self.winner_features_frame, text='Подробнее о способности',
                                                 image=info_icon,
                                                 command=self.get_winner_description)

        self.get_feauture_button1.grid(row=2, column=0, padx=10, pady=(0, 5), sticky='ew')

        # Текстовой блок в котором будет храниться описание для способности
        self.descr_feature1 = CTk.CTkTextbox(self.winner_features_frame, wrap='word', corner_radius=10, height=180)
        self.descr_feature1.grid(row=3, column=0, padx=10, pady=(5, 10), sticky='new')

        self.choice_feature_heroes = CTk.CTkButton(self.winner_features_frame, text='Герои со способностью',
                                                 command=self.get_feature_heroes)
        self.choice_feature_heroes.grid(row=4, column=0, padx=10, pady=(5, 10), sticky='new')

        self.feature_heroes_frame = CTk.CTkFrame(self,width=300)
        self.feature_heroes_frame.grid(row=0,column=3,sticky='nsew', padx=5, pady=10)
        self.feature_heroes_frame.grid_rowconfigure(1,weight=1)

        self.feature_heroes_label = CTk.CTkLabel(self.feature_heroes_frame, text=f'Герои со способностью')
        self.feature_heroes_label.grid(row=0, column=0, sticky='new', padx=5, pady=5)

        self.winners_heroes_scroll = Winner_Heroes_frame(self.feature_heroes_frame,width=250,feature_id=0)
        self.winners_heroes_scroll.grid(row=1, column=0, sticky='news', padx=5, pady=5)


    def get_feature_heroes(self):
        feature_id = self.counter_features.get_feature_id()
        heroes = select_feature_heroes(feature_id)


    def get_winner_description(self):
        feature_id = self.counter_features.get_feature_id()
        feature_info = select_feature_info(feature_id)
        self.descr_feature1.delete('0.0','end')
        self.descr_feature1.insert('0.0',feature_info[2])

    def get_counter_features(self):

        loser_id = self.hero_features_scroll.get_choice_feature()
        loser_name = select_feature_info(loser_id )[1]
        features_list = select_winners_features(loser_id)
        self.counter_features = Winners_list_frame(self.winner_features_frame, features_list=features_list, width=250,height=200)
        self.counter_features.grid(row=1, column=0, sticky='new', padx=5, pady=5)
        self.loser_feature_label.configure(text=f'Контрят "{loser_name}"')
    def get_description(self):
        feature_id = self.hero_features_scroll.get_choice_feature()
        select_feature = select_feature_info(feature_id)
        self.descr_feature.delete('0.0','end')
        self.descr_feature.insert('0.0',select_feature[-1])

    def choice_hero(self):
        hero_id = self.heroes_scroll_frame.get_hero_id()
        hero_info = select_hero_info(hero_id)
        self.hero_label.configure(text=f'Способности героя : {hero_info[1]}')

        # переменная в которой будет список способностей для персонажа с выбранным айди
        hero_features_list = select_hero_features1(hero_id=hero_id)
        self.hero_features_scroll= Hero_Features_Frame(self.hero_features_frame,hero_features_list,width=250)
        self.hero_features_scroll.grid(row=1, column=0, sticky='new', padx=10,pady=10)

    def get_feature_heroes(self):
        feature_id = self.counter_features.get_feature_id()
        self.winners_heroes_scroll = Winner_Heroes_frame(self.feature_heroes_frame, width=250, feature_id=feature_id)
        self.winners_heroes_scroll.grid(row=1, column=0, sticky='news', padx=5, pady=5)




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





class Winner_Features_Frame(CTk.CTkFrame):
    def __init__(self,master,loser_feature_id):
        super().__init__(master)
        self.loser_feature_label = CTk.CTkLabel(self, text=f'Противодействующие способности :')
        self.loser_feature_label.grid(row=0, column=0, sticky='new')

        winner_features = select_winners_features(loser_feature_id)
        self.winner_features_list = Winners_list_frame(self,features_list=winner_features,width=250,height=200)
        self.winner_features_list.grid(row=1, column=0, sticky='new', padx=10, pady=5)

        # Кнопка которая вызывает функцию get_description
        self.get_feauture_button = CTk.CTkButton(self, text='Подробнее о способности', image=info_icon,
                                                 command=self.get_description)
        self.get_feauture_button.grid(row=2, column=0, padx=10, pady=(0, 5), sticky='ew')

        # Текстовой блок в котором будет храниться описание для способности
        self.descr_feature = CTk.CTkTextbox(self, wrap='word', corner_radius=10, height=180)
        self.descr_feature.grid(row=3, column=0, padx=10, pady=(0, 5), sticky='new')

        self.choice_winner_button = CTk.CTkButton(self,text='Найти Героев с этой способностью',command=self.get_heroes)
        self.choice_winner_button.grid(row=4, column=0, sticky='new', padx=10, pady=5)


    def get_heroes(self):
        feature_id = self.winner_features_list.get_feature_id()
        self.winner_heroes_frame = Winner_Heroes_frame(self,feature_id,width=300)
        self.winner_heroes_frame.grid(row=1, column=1, sticky='new', padx=10, pady=5,rowspan=4)


    def get_description(self):
        self.descr_feature.delete('0.0', 'end')
        feature_id =self.winner_features_list.get_feature_id()
        feature_description = select_feature_info(feature_id)[2]
        self.descr_feature.insert('0.0',feature_description)


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









'''        # Кнопка которая вызывает функцию get_description
        self.get_feauture_button = CTk.CTkButton(self, text='Подробнее о способности', image=info_icon,
                                                 command=self.get_description)
        self.get_feauture_button.grid(row=2, column=0, padx=10, pady=(0, 5), sticky='ew')

        # Текстовой блок в котором будет храниться описание для способности
        self.descr_feature = CTk.CTkTextbox(self, wrap='word', corner_radius=10, height=180)
        self.descr_feature.grid(row=3, column=0, padx=10, pady=(0, 5), sticky='new')


        self.feature_choice_button = CTk.CTkButton(self,
                                                   text='Найти противодействующие способности',
                                                   command=self.find_win_features)
        self.feature_choice_button.grid(column=0, row=4, sticky='new', padx=10, pady=5)

    # Функция удаляет предыдущее записанное в текстовом боксе ,
    # берет описание из переменной которая хранит описание для выбранной
    # радио кнопки и записывает это описание в текстовой бокс
    def get_description(self):
        self.descr_feature.delete('0.0', 'end')
        feature_id = self.features_var.get()
        feature_info = select_feature_info(feature_id)
        feature_description = feature_info[2]
        self.descr_feature.insert('0.0',feature_description)

    def get_feature_id(self):
        return self.features_var.get()

    def find_win_features(self):
        loser_feature_id = self.get_feature_id()
        print(loser_feature_id)
        self.choice_winner_menu = Winner_Features_Frame(self,loser_feature_id)
        self.choice_winner_menu.grid(column=1,row=1,sticky='nsew', padx=10,pady=5,rowspan=5)'''

if __name__ == '__main__':
    counter_picker = Counter_Picker()
    counter_picker.mainloop()
