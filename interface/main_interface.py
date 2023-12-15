from db_operation.select_from_tables import *
from db_operation.update_tables import update_feature_description
from db_operation.insert_in_tables import (
                                           hero_insert,
                                           feature_insert,
                                           insert_hero_feature)
from pathlib import Path
from CTkMessagebox import CTkMessagebox
import customtkinter as CTk
from PIL import Image
CTk.set_appearance_mode('dark')
from pathlib import Path

#Хранит иконку информации которую можно использовать в интерфейсе
info_icon = CTk.CTkImage(light_image=Image.open(str(Path.cwd().parent)+'\\images\\icon_info.png'),
                                  dark_image=Image.open(str(Path.cwd().parent)+"\\images\\icon_info.png"),
                                  size=(30, 30))

main_logo = CTk.CTkImage(light_image=Image.open(str(Path.cwd().parent)+'\\images\\dota_counter_picker.png'),
                                  dark_image=Image.open(str(Path.cwd().parent)+"\\images\\dota_counter_picker.png"),
                                  size=(150, 100))
#Главный Фрейм
class Main(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.title('DotaCounterPicker')

        #Меню для добавления Записей о способностях
        self.add_feature = Add_Feature(self)
        self.add_feature.grid(row=0,column=0,padx=(10,5),pady=10,sticky='nsew')

        #Меню с с скроллющимся списком персонажей и выбора одного из них чтобы показать его способности
        self.hero_features_menu = Hero_list(self)
        self.hero_features_menu.grid(row=0,column=1,padx=(5,10),pady=10,sticky='nsew')



# фрейм для выборки персонажа
class Hero_list(CTk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        #Заголовок сверху находится выше всех
        self.title_label = CTk.CTkLabel(self,text='Способности Персонажей')
        self.title_label.grid(row=0,column=0,columnspan=2,sticky='new',pady=10)

        self.select_hero_frame = CTk.CTkFrame(self,width=150,height=300)
        self.select_hero_frame.grid(row=1, column=0,padx=(0,10), sticky='nsew')
        self.select_hero_frame.grid_rowconfigure(0,weight=1)
        #Фрейм в котором  перебираются все персонажи (фрейм с автоматическим скроллом)
        self.heroes_frame = CTk.CTkScrollableFrame(self.select_hero_frame,width=150,height=300)
        self.heroes_frame.grid(row=0, column=0, sticky='nsew', padx=10,pady=(10,5))
        #Переменная для хранения айди Персонажа , которое определяется с помощью радио кнопок
        self.hero_id_var = CTk.IntVar(value=1)

        #функция  select_heroes выбирает все айди и имена для всех персонажей из таблицы Heroes
        heroes = select_heroes()

        #внутри фрейма heroes_frame создаются радио кнопки соответствующие персонажу
        # (информацию о выбранной кнопке будет хранить self.hero_id_var)
        for i,value in enumerate(heroes):
            radio_button = CTk.CTkRadioButton(self.heroes_frame,text=value[1],value=value[0],variable=self.hero_id_var)
            radio_button.grid(row=i,column=0,sticky='new',padx=10,pady=5)


        #кнопка которая вызывает функцию get_hero разположена внутри фрейм класса Hero_list
        self.get_hero_button = CTk.CTkButton(self.select_hero_frame,text='Выбрать',command=self.get_hero)
        self.get_hero_button.grid(row=1,column=0,sticky='new',padx=5,pady=5)



    # Функция которая создает фрейм для отображения способностей персонажа
    def get_hero(self):

        # Функция получает айди персонажа из hero_id_var.get() в переменную hero_id
        hero_id = self.hero_id_var.get()

        # далее вызываем функцию select_hero_info(hero_id) которая по айди достает всю информацию о персонаже
        hero_info = select_hero_info(hero_id)

        # создается Экземпляр класса Hero_features_menu который является новым фреймом для отображения способностей персонажа
        self.hero_feature_frame = Hero_features_menu(self,hero=hero_info)
        self.hero_feature_frame.grid(row=1, column=1,padx=(0,10), sticky='new')

        self.insert_feature_to_Hero = Insert_Feature_to_Hero(self)
        self.insert_feature_to_Hero.grid(row=1, column=2, padx=(0, 10), sticky='new')


class Hero_features_menu(CTk.CTkFrame):
    def __init__(self,master,hero):
        super().__init__(master)
        #Лейбл для заголовка
        self.hero_label = CTk.CTkLabel(self,text=f'Способности героя : {hero[1]}')
        self.hero_label.grid(row=0,column=0,sticky='new')

        # Скроллбар фрейм в котором будут храниться все способности выбранного персонажа  в виде радио кнопок
        self.features_bar = CTk.CTkScrollableFrame(self,width=270, height=200)
        self.features_bar.grid(row=1,column=0,sticky='new',padx=10,pady=5)

        #переменная в которой будет список способностей для персонажа с выбранным айди
        hero_features_list = select_hero_features1(hero_id=hero[0])

        #Переменаая хранящая значение выбранной радио кнопки из фрейма self.features_bar
        self.selected_feature = CTk.StringVar(value='Описание способности')


        #Перебор всех значений из списка hero_features_list и создания радио кнопок
        for i,value in enumerate(hero_features_list):

            # Лейбл в котором написан название способности и указан ее уровень для каждого персонажа
            label = CTk.CTkLabel(self.features_bar,text=f'{value[2]} ({ value[-1]}-level)')
            label.grid(row=i,column=0,sticky='new',padx=10,pady=5)


            '''
            Уровень 1 - белая запись : Значит что у Героя есть эта способность но особо важной роли она не играет
            Уровень 2 - зеленая запись : Значит что у Героя есть способность которая может приносить не большие трудности врагу
            Уровень 3 - голубая запись : Значит что у Героя есть способность которая может принести много проблем , стоит обратить на нее внимание
            Уровень 4 - розовая запись : Значит что у Героя есть способность которую нужно обязательно чем то перекрыть , иначе возрастает шанс проиграть
            Уровень 5 - оранжевая запись : Значит что у Героя есть способность которую если ничем не перекрыть , то вы проиграете
            '''

            # Сдесь происходит цветовая кастомизация лейбла выше взависимости от уровня способности
            if value[-1] ==1:
                label.configure()
            if value[-1] == 2:
                label.configure(text_color='#2EDB4B')
            elif value[-1] ==3:
                label.configure(text_color='#2EA4DB')
            elif value[-1] ==4:
                label.configure(text_color='#E63DF5')
            elif value[-1] ==5:
                label.configure(text_color='#F09B24')


            # Радио кнопка которая хранит описание способности и передает значение в переменную self.selected_feature
            descr_button = CTk.CTkRadioButton(self.features_bar,text="",value=value[2]+' :\n'+value[3],variable=self.selected_feature)
            descr_button.grid(row=i,column=1,sticky='nws')

        # Кнопка которая вызывает функцию get_description
        self.get_feauture_button = CTk.CTkButton(self,text='Подробнее о способности' ,image=info_icon,command=self.get_description)
        self.get_feauture_button.grid(row=2,column=0,padx=10,pady=(0,5),sticky='ew')

        # Текстовой блок в котором будет храниться описание для способности
        self.descr_feature = CTk.CTkTextbox(self,wrap='word',corner_radius=10,height=180)
        self.descr_feature.grid(row=3,column=0,padx=10,pady=(0,5),sticky='new')

        # Кнопка на случай желания поменять описание способности в базе данных
        self.update_feature_button = CTk.CTkButton(self, text='Обновить описание', command=self.update_feature_descr)
        self.update_feature_button.grid(row=4, column=0, sticky='new', pady=(0,5), padx=(10, 10))

    #Функция делает запрос на обновление поля Description для выбранной способности
    def update_feature_descr(self):
        feature_name = self.selected_feature.get().split(' :\n')[0]
        feature_description = self.descr_feature.get('0.0','end').split(' :\n')[1]
        update_feature_description(feature_name,feature_description)
        CTkMessagebox(title="Обновлено", message=f'Описание способности "{feature_name}" было обновлено !'
                                                 f'\n Чтобы в программе описание обновилось перевыберете персонажа ', icon="check")








    # Функция удаляет предыдущее записанное в текстовом боксе ,
    # берет описание из переменной которая хранит описание для выбранной
    # радио кнопки и записывает это описание в текстовой бокс
    def get_description(self,):
        self.descr_feature.delete('0.0', 'end')
        feature_description = self.selected_feature.get()
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

class Insert_Feature_to_Hero(CTk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.grid_columnconfigure(0,weight=1)
        self.title_label = CTk.CTkLabel(self,text='Назначить способность герою')
        self.title_label.grid(row=0,column=0,pady=5,padx=10,sticky='ew')

        self.choice_feature_frame=CTk.CTkScrollableFrame(self)
        self.choice_feature_frame.grid(row=1,column=0,pady=5,padx=10,sticky='new')

        self.choice_var = CTk.IntVar(value=0)
        features_list = select_features()
        for i, feature in enumerate(features_list):
            label = CTk.CTkRadioButton(self.choice_feature_frame,text=f'"{feature[1]}"',value=feature[0],variable=self.choice_var)
            label.grid(row=i,column=0,sticky='new',pady=5)

        self.choice_button = CTk.CTkButton(self,text='Выбрать',command=self.select_feature)
        self.choice_button.grid(row=2,column=0,pady=5,padx=10,sticky='new')

        self.SliderVar = CTk.IntVar(value=1)
        self.progressbar = CTk.CTkProgressBar(self, orientation="horizontal")
        self.slider = CTk.CTkSlider(self, from_=1, to=5,number_of_steps=4, variable=self.SliderVar)
        self.slider.grid(row=3,column=0,pady=5,padx=10,sticky='new')
    def select_feature(self):
        pass

if __name__ == '__main__':
    main = Main()
    main.mainloop()