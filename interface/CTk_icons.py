import customtkinter as CTk
from PIL import Image
from pathlib import Path


#Хранит иконку информации которую можно использовать в интерфейсе
info_icon = CTk.CTkImage(light_image=Image.open(str(Path.cwd().parent)+'\\images\\icon_info.png'),
                                  dark_image=Image.open(str(Path.cwd().parent)+"\\images\\icon_info.png"),
                                  size=(30, 30))

main_logo = CTk.CTkImage(light_image=Image.open(str(Path.cwd().parent)+'\\images\\dota_counter_picker.png'),
                                  dark_image=Image.open(str(Path.cwd().parent)+"\\images\\dota_counter_picker.png"),
                                  size=(150, 100))

add_icon = CTk.CTkImage(light_image=Image.open(str(Path.cwd().parent)+'\\images\\icon_add.png'),
                                  dark_image=Image.open(str(Path.cwd().parent)+"\\images\\icon_add.png"),
                                  size=(30, 30))

delete_icon = CTk.CTkImage(light_image=Image.open(str(Path.cwd().parent)+'\\images\\icon_delete.png'),
                                  dark_image=Image.open(str(Path.cwd().parent)+"\\images\\icon_delete.png"),
                                  size=(30, 30))
