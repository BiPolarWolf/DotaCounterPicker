from db_operation.select_from_tables import *
from db_operation.insert_in_tables import (insert_all_heroes,
                                           hero_insert,
                                           feature_insert,
                                           insert_hero_feature)
from CTkMessagebox import CTkMessagebox
import customtkinter as CTk
CTk.set_appearance_mode('dark')


#Главный Фрейм
class Main(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.title('DotaCounterPicker')
        self.insert_feature = Insert_Feature(self,)
        self.insert_feature.grid(row=0,column=0,padx=(10,5),pady=10,sticky='nsew')

        self.radio_heroes = Hero_list(self)
        self.radio_heroes.grid(row=0,column=1,padx=(5,10),pady=10,sticky='nsew')



# фрейм для выборки персонажа
class Hero_list(CTk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.heroes_frame = CTk.CTkScrollableFrame(self,width=150, height=300)
        self.hero_id_var = CTk.IntVar(value=0)
        heroes = select_heroes()
        for i,value in enumerate(heroes):
            radio_button = CTk.CTkRadioButton(self.heroes_frame,text=value[1],value=value[0],variable=self.hero_id_var)
            radio_button.grid(row=i,column=0,sticky='new',padx=10,pady=5)

        self.heroes_frame.grid(row=0,column=0,sticky='new',padx=10,pady=10)
        self.get_hero_button = CTk.CTkButton(self,text='Выбрать',command=self.get_hero)
        self.get_hero_button.grid(row=len(heroes),column=0,sticky='new',padx=5,pady=5)

    def get_hero(self):
        hero_id = self.hero_id_var.get()
        hero_info = select_hero_info(hero_id)
        print(hero_info)


#Фрейм для добавления способности в базу данных
class Insert_Feature(CTk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.add_feature = CTk.CTkLabel(self, text='Добавить Оссобенность')
        self.add_feature.grid(row=0, column=0, padx=0, pady=0,columnspan=2, sticky='nsew')
        self.add_feature.configure(fg_color='#606060')

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