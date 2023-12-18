from db_operation.select_from_tables import *
from db_operation.delete_from_table import delete_from_hero_feature
from db_operation.update_tables import update_feature_description
from db_operation.insert_in_tables import (
                                           hero_insert,
                                           feature_insert,
                                           insert_hero_feature,insert_feature_vs_feature)
from CTk_icons import info_icon,delete_icon,add_icon,main_logo
from CTkMessagebox import CTkMessagebox
from main_interface import  Heroes_Scroll_Frame

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

        self.entry= CTk.CTkEntry(self,placeholder_text='Введите персонажа')
        self.entry.grid(column=0,row=0,sticky='nsew',padx=5,pady=(10,5))
        global text
        self.search_button = CTk.CTkButton(self,text='Поиск',command=self.search)
        self.search_button.grid(column=1, row=0, sticky='nsew', padx=5, pady=(10, 5))

    def search(self):
        return self.entry.get()


class Choice_hero_menu(CTk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.search_bar = Search_bar(self)
        self.search_bar.grid(row=0, column=0, sticky='nsew', padx=10, pady=(10, 5))
        self.heroes_scroll_frame = Heroes_Scroll_Frame(self,width=150,height=300 ,text='')
        self.heroes_scroll_frame.grid(row=1, column=0, sticky='nsew', padx=10,pady=(10,5))


if __name__ == '__main__':
    counter_picker = Counter_Picker()
    counter_picker.mainloop()
