import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('DotaCounterPicker')
        self.geometry('250x300')
        self.grid_columnconfigure(0, weight=1)

        self.create_hero = CreateHeroFrame(self,'Добавить Персонажа')
        self.create_hero.grid(row=0,column=0,sticky='ew')



class CreateHeroFrame(customtkinter.CTkFrame):
    def __init__(self,master,title):
        super().__init__(master)
        self.grid_columnconfigure(0,weight=1)

        self.title_label=customtkinter.CTkLabel(self,text=title,fg_color="gray30"  )
        self.title_label.grid(row=0,column=0,sticky='new')

        self.name_frame = customtkinter.CTkFrame(self)
        self.name_frame.grid(row=1,column=0,sticky='new')
        self.name_frame.grid_columnconfigure(1,weight=1)
        self.name_label = customtkinter.CTkLabel(self.name_frame,text='Имя:')
        self.name_label.grid(row=0,column=0,padx=(10,5),pady=10)
        self.name_entry = customtkinter.CTkEntry(self.name_frame,placeholder_text='Введите Имя')
        self.name_entry.grid(row=0,column=1,sticky='ew',padx=5)
        self.attributes_frame = Attributes_frame(self,'Указать Аттрибут',
                                                 ['Сила','Ловкость','Интеллект','Универсальный'])
        self.attributes_frame.grid(row=2,column=0,sticky='new')
class Attributes_frame(customtkinter.CTkFrame):
    def __init__(self,master,title,values):
        super().__init__(master)
        self.grid_columnconfigure(0,weight=1)

        self.attr_label= customtkinter.CTkLabel(self,text=title,fg_color="gray30")
        self.attr_label.grid(column=0,row=0,sticky='new')
        self.attribute_var = customtkinter.StringVar(value='Сила')

        for i ,value in enumerate(values):
            radio_button = customtkinter.CTkRadioButton(self,text=value,value=value,variable=self.attribute_var)
            radio_button.grid(row=i+1,column=0,sticky='ew',pady=7,padx=10)

    def get(self):
        return self.attribute_var.get()

    def set(self,value):
        self.attribute_var.set(value)
if __name__ == '__main__':
    app = App()
    app.mainloop()