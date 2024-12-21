from tkinter import *




root=Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3=IntVar()






root.geometry("905x505")




english=Checkbutton(root,text="English",variable=CheckVar1,onvalue = 1, offvalue = 0)
english.grid(row=1,column=1)


Hindi=Checkbutton(root,text="Hindi",variable=CheckVar2,onvalue=1,offvalue=0)
Hindi.grid(row=2,column=1)

sanskrit=Checkbutton(root,text="Sankrit",variable=CheckVar3)
sanskrit.grid(row=3,column=1)
root.mainloop()