from tkinter import *
from tkinter import ttk, scrolledtext, messagebox
import functions
#functions.execute()
def run():

    if combo.get() == "Option1":
        functions.active_device()
        messagebox.showinfo('✔✔', 'İşleminiz başarıyla gerçekleştirildi!')
    elif combo.get() == "Option2":
        functions.deactive_device()
        messagebox.showinfo('✔✔', 'İşleminiz başarıyla gerçekleştirildi!')
    elif combo.get() == "Option3":
        functions.active_firewall()
        messagebox.showinfo('✔✔', 'İşleminiz başarıyla gerçekleştirildi!')
    elif combo.get() == "Option4":
        functions.deactive_firewall()
        messagebox.showinfo('✔✔', 'İşleminiz başarıyla gerçekleştirildi!')
    elif combo.get() == "Option5":
        messagebox.showinfo('✌✌', 'Kendi regedit sorgunu ekleyerek geliştirebilirsin!')
    else:
        messagebox.showinfo('╳', 'İşleminiz gerçekleştirilemedi!')

root = Tk()
root.geometry("597x200")
root.title("WinRegApp")
root['bg'] = '#000000'
root.resizable(width=FALSE, height=FALSE)
text = scrolledtext.ScrolledText(root,width=72,height=10)
text.insert('1.0', '\nOption1 ► USB DEPOLAMA CİHAZLARINI AKTİF DURUMA GETİRİR!\n'
                   'Option2 ► USB DEPOLAMA CİHAZLARINI DEVRE DIŞI BIRAKIR!\n'
                   'Option3 ► WİNDOWS GÜVENLİK DUVARINI AKTİF HALE GETİRİR!\n'
                   'Option4 ► WİNDOWS GÜVENLİK DUVARINI DEVRE DIŞI BIRAKIR!')
text.place(x=0,y=65)
frame = Frame(root)
frame.pack()
list = ["Option1", "Option2", "Option3", "Option4", "Option5"]
combo = ttk.Combobox(frame, values=list)
combo.set("———————————")
combo.pack(padx=4, pady=4)
Button = Button(frame, text="♣", command=run, width=100)
Button.pack(padx=5, pady=5)
root.mainloop()



