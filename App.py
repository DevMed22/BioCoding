import tkinter

import button as button
import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

app = customtkinter.CTk()
app.geometry("500x500")
app.title('BioCoding app')
# prog.minsize("300x300")
tabview = customtkinter.CTkTabview(app,
                                   width=450,
                                   height=450,
                                   corner_radius=10)
tabview.pack(padx=10, pady=10)

home = tabview.add("Home")
sec_1 = tabview.add("sec 1")
sec_2 = tabview.add("sec 2")
sec_3 = tabview.add("sec 3")
sec_4 = tabview.add("sec 4")
sec_5 = tabview.add("sec 5")
sec_6 = tabview.add("sec 6")
sec_7 = tabview.add("sec 7")
sec_8 = tabview.add("sec 8")
quiet = tabview.add("Quiet")

tabview.set("Home")


# ----------------sec_1-----------#
def count_this():
    seq = entry_1.get()
    # print(seq)
    label_2 = customtkinter.CTkLabel(master=sec_1,
                                     text=seq,
                                     width=120,
                                     height=25,
                                     corner_radius=8,
                                     font=("Roboto", 20))
    label_2.pack(pady=12, padx=10)
    label_2.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)


label_1 = customtkinter.CTkLabel(master=sec_1,
                                 text="section 1",
                                 width=120,
                                 height=25,
                                 corner_radius=8,
                                 font=("Roboto", 20))
label_1.pack(pady=12, padx=10)
label_1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

entry_1 = customtkinter.CTkEntry(master=sec_1,
                                 placeholder_text="Enter the Gene Seq",
                                 width=240,
                                 height=30,
                                 border_width=2,
                                 corner_radius=10)
entry_1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

label_2 = customtkinter.CTkLabel(master=sec_1,
                                 text="",
                                 width=120,
                                 height=25,
                                 corner_radius=8,
                                 font=("Roboto", 20))
label_2.pack(pady=12, padx=10)
label_2.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

button_1 = customtkinter.CTkButton(master=sec_1,
                                   width=120,
                                   height=32,
                                   border_width=0,
                                   corner_radius=8,
                                   text="CTkButton",
                                   command=count_this)
button_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()
