from db_operation.select_from_tables import *
from db_operation.insert_in_tables import (insert_all_heroes,
                                           hero_insert,
                                           feature_insert,
                                           insert_hero_feature)
import customtkinter as CTk
CTk.set_appearance_mode('dark')
class Main(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.title('DotaCounterPicker')

        self.add_feature =CTk.CTkLabel(self,text='Добавить Оссобенность')
        self.add_feature.grid(row=0,column=0,padx=0,pady=0,sticky='nsew')
        self.add_feature.configure(fg_color='#606060', corner_radius=0)
        self.insert_feature = Insert_Feature(self,)
        self.insert_feature.grid(row=1,column=0,padx=0,pady=0,sticky='nsew')
        self.insert_feature.configure(fg_color='#303030',corner_radius=0)

class Insert_Feature(CTk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.label = CTk.CTkLabel(self,text='Название :')
        self.name_var = CTk.StringVar(value='')
        self.label.grid(row=0,column=0,padx=10,pady=20)
        self.entry = CTk.CTkEntry(self)
        self.entry.grid(row=0,column=1,padx=(0,10),pady=20)
        self.label_descr=CTk.CTkLabel(self,text='Описание',bg_color='gray')
        self.label_descr.grid(row=1,column=0,columnspan=2,padx=10,sticky='new')
        self.descr = CTk.CTkTextbox(self,wrap='word',corner_radius=0,height=130)
        self.descr.grid(row=2,column=0,columnspan=2,padx=10,pady=(0,5),sticky='new')
        self.add_button = CTk.CTkButton(self,text='Добавить',command=self.add_feature)
        self.add_button.grid(row=3,column=0,columnspan=2,padx=10,pady=10,sticky='new')

    def add_feature(self):
        name = self.entry.get()
        descr = self.descr.get("0.0",'end')
        feature_info = [name,descr]
        feature_insert(feature_info)

if __name__ == '__main__':
    main = Main()
    main.mainloop()