from db_operation.select_from_tables import *
from db_operation.insert_in_tables import (insert_all_heroes,
                                           hero_insert,
                                           feature_insert,
                                           insert_hero_feature)
from pathlib import Path
from CTkMessagebox import CTkMessagebox
import customtkinter as CTk
from PIL import Image
CTk.set_appearance_mode('dark')



info_icon = CTk.CTkImage(light_image=Image.open('D:\\pycharm_projects\\Dota_counter_pick\\images\\icon_info.png'),
                                  dark_image=Image.open("D:\\pycharm_projects\\Dota_counter_pick\\images\\icon_info.png"),
                                  size=(30, 30))

#Главный Фрейм
class Main(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.title('DotaCounterPicker')
        self.insert_feature = Insert_Feature(self)
        self.insert_feature.grid(row=0,column=0,padx=(10,5),pady=10,sticky='nsew')

        self.radio_heroes = Hero_list(self)
        self.radio_heroes.grid(row=0,column=1,padx=(5,10),pady=10,sticky='nsew')



# фрейм для выборки персонажа
class Hero_list(CTk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.title_label = CTk.CTkLabel(self,text='Способности Персонажей')
        self.title_label.grid(row=0,column=0,columnspan=2,sticky='new',pady=10)
        self.heroes_frame = CTk.CTkScrollableFrame(self,width=150,height=300)
        self.heroes_frame.grid(row=1, column=0, sticky='nsew', padx=10,)
        self.hero_id_var = CTk.IntVar(value=1)
        heroes = select_heroes()
        for i,value in enumerate(heroes):
            radio_button = CTk.CTkRadioButton(self.heroes_frame,text=value[1],value=value[0],variable=self.hero_id_var)
            radio_button.grid(row=i,column=0,sticky='new',padx=10,pady=5)
        self.get_hero_button = CTk.CTkButton(self,text='Выбрать',command=self.get_hero)
        self.get_hero_button.grid(row=2,column=0,sticky='new',padx=10,pady=5)

        #self.hero_feature_frame = Hero_Features(self,hero=self.get_hero())
        #self.hero_feature_frame.grid(row=0,column=1,sticky='new')


    def get_hero(self):
        hero_id = self.hero_id_var.get()
        hero_info = select_hero_info(hero_id)
        self.hero_feature_frame = Hero_Features(self,hero=hero_info)
        self.hero_feature_frame.grid(row=1, column=1,padx=(0,10), sticky='new')
        self.update_feature_description = CTk.CTkButton(self,text='Обновить описание',command=self.get_hero)
        self.update_feature_description.grid(row=2, column=1, sticky='new',pady=5,padx=(0,10))
    def update_feature_descr(self):
        pass


class Hero_Features(CTk.CTkFrame):
    def __init__(self,master,hero):
        super().__init__(master)
        self.hero_label = CTk.CTkLabel(self,text=f'Способности героя : {hero[1]}')
        self.hero_label.grid(row=0,column=0,sticky='new')
        self.features_bar = CTk.CTkScrollableFrame(self,width=300, height=200)
        self.features_bar.grid(row=1,column=0,sticky='new',padx=10,pady=5)
        self.hero_features_list = select_hero_features1(hero_id=hero[0])

        self.selected_feature = CTk.StringVar(value='Описание способности')
        print(self.hero_features_list)
        for i,value in enumerate(self.hero_features_list):

            label = CTk.CTkLabel(self.features_bar,text=f'{value[2]} ({ value[-1]}-level)')
            label.grid(row=i,column=0,sticky='new',padx=10,pady=5)
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
            descr_button = CTk.CTkRadioButton(self.features_bar,text="",value=value[3],variable=self.selected_feature)
            descr_button.grid(row=i,column=1,sticky='nws')

        self.get_feauture_button = CTk.CTkButton(self,text='Подробнее о способности' ,image=info_icon,command=self.get_description)
        self.get_feauture_button.grid(row=2,column=0,padx=10,pady=(0,5),sticky='ew')

        self.descr_feature = CTk.CTkTextbox(self,wrap='word',corner_radius=10,height=180)
        self.descr_feature.grid(row=3,column=0,padx=10,pady=(0,5),sticky='new')

    def get_description(self,):
        self.descr_feature.delete('0.0', 'end')
        feature_description = self.selected_feature.get()
        self.descr_feature.insert('0.0',feature_description)



#Фрейм для добавления способности в базу данных
class Insert_Feature(CTk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.add_feature_label = CTk.CTkLabel(self, text='Добавить Оссобенность')
        self.add_feature_label.grid(row=0, column=0, padx=0, pady=0,columnspan=2, sticky='nsew')
        self.add_feature_label.configure(fg_color='#606060')

        self.label = CTk.CTkLabel(self,text='Название :')
        self.name_var = CTk.StringVar(value='')
        self.label.grid(row=1,column=0,padx=10,pady=20)
        self.entry = CTk.CTkEntry(self)
        self.entry.grid(row=1,column=1,padx=(0,10),pady=20)
        self.label_descr=CTk.CTkLabel(self,text='Описание',bg_color='gray')
        self.label_descr.grid(row=2,column=0,columnspan=2,padx=10,sticky='new')
        self.descr = CTk.CTkTextbox(self,wrap='word',corner_radius=0,height=180)
        self.descr.grid(row=3,column=0,columnspan=2,padx=10,pady=(0,5),sticky='new')
        self.add_button = CTk.CTkButton(self,text='Добавить',command=self.add_feature)
        self.add_button.grid(row=4,column=0,columnspan=2,padx=10,pady=10,sticky='new')

    def add_feature(self):
        name = self.entry.get()
        descr = self.descr.get("0.0",'end')
        feature_info = [name,descr]
        feature_insert(feature_info)
        CTkMessagebox(title="Способность добавлена", message=f'Способность "{name}" успешно добавлена ! ',icon="check")
        self.entry.delete('0','end')
        self.descr.delete('0.0','end')


if __name__ == '__main__':
    main = Main()
    main.mainloop()