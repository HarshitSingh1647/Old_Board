try:
    from tkinter import *
    from base import *
    from tkinter.colorchooser import askcolor
    import tkfontselector as tkFont
    import pyperclip as cop
    import os
    from PIL import ImageTk,Image


    try:
        import pywhatkit as kit

        from gtts import gTTS
        from playsound import playsound

        import random
        import wikipedia
        import speech_recognition as sr



        state="yes"
    except:

        state=("no")






    class Paint(object):

        DEFAULT_PEN_SIZE = 5.0
        DEFAULT_COLOR = 'black'


        def __init__(self):

            self.root = Tk()
            def setwin():
                #scroll
                self.scrollbar.pack(side="right",fill=Y)
                #main text
                self.entry.pack(side="right")
                #clear
                self.r.pack(side="left")
                self.r.place(y=10)
                #wiki button
                self.wiki.place(x=1000,y=10)
                #main pen
                self.pen_button.pack()
                self.pen_button.place(x=100,y=10)
                #brush button
                self.brush_button.pack()
                self.brush_button.place(x=200,y=10)
                # computer speaking btn
                self.speak_button.place(x=800,y=10)
                #colour choosing btn
                self.color_button.pack()
                self.color_button.place(x=300,y=10)
                #eraser btn
                self.eraser_button.place(x=400,y=10)
                #main canvas
                self.c.pack(side="left")
                #caption label

                self.label1.place(x=5,y=650)

                #caption btn
                self.speech.pack(side="bottom")
                #width choosing scale
                self.choose_size_button.place(x=450,y=0)
                #mode label (top)
                self.label2.place(x=1200,y=10)
                #google btn
                self.google.place(x=900,y=10)
                #self.rec_butt.pack()
                self.rec_butt.place(x=700,y=10)
                #copy btn
                self.pys_b.place(x=1100,y=10)
                #last 2 btn
                self.rec_bu.place(x=600,y=10)
                self.speech_text.place(x=1300,y=10)

            self.root.geometry("700x400+300+100")
            global var2
            global var1
            global ty
            self.ty="pen"

            self.var2 = StringVar()
            self.var1 = StringVar()
            if wrapornot=="wrape":
                self.entry = Text(self.root,wrap=WORD,height=36,width=55,bg="white")
            if wrapornot=="dontwrape":
                 self.entry = Text(self.root,height=36,width=55,bg="white")

            self.scrollbar = Scrollbar(self.root)


            self.entry.config(yscrollcommand=self.scrollbar.set)
            self.scrollbar.config(command=self.entry.yview)

            self.wiki_image=PhotoImage(file="lib/wikipedia_image.png")

            self.wiki = Button(self.root,image=self.wiki_image,command=self.searchwiki)
            cnp=PhotoImage(file="lib/canvas.png")
            self.r = Button(self.root,image=cnp,command=self.clear,cursor="sizing")
            penp=PhotoImage(file="lib/pen.png")
            self.pen_button = Button(self.root,image=penp, command=self.use_pen)

            brushp=PhotoImage(file="lib/brush.png")
            self.brush_button = Button(self.root,image=brushp, command=self.use_brush)


            self.speak_image = PhotoImage(file="lib/speak_image.png")
            self.speak_button = Button(self.root,image=self.speak_image,command=self.speak)
            copp=PhotoImage(file="lib/col.png")
            self.color_button = Button(self.root,image=copp, command=self.choose_color)
            eraserp=PhotoImage(file="lib/eraser.png")
            self.eraser_button = Button(self.root,image=eraserp, command=self.use_eraser)


            self.c=Canvas(self.root,width=850,height=550,bg= "white" ,cursor="tcross")

            self.label1=Label(self.root,textvariable=self.var1,width=200,font="Calibri",bg="light grey")
            self.var1.set('_None_')
            self.label1.lift()

            self.mic_photo = PhotoImage(file="lib/mic_pho.png")
            self.speech = Button(self.root, image=self.mic_photo, command=self.takeCommand)


            self.choose_size_button = Scale(self.root, from_=1, to=200, orient=HORIZONTAL)
            self.choose_size_button.pack()





            self.label2=Label(self.root,textvariable=self.var2,font="Calibri",bg="light grey")
            self.var2.set('None')

            self.goo_png=PhotoImage(file="lib/google.png")
            self.google=Button(self.root,image=self.goo_png,command=self.go_search)
            recp=PhotoImage(file="lib/rec.png")
            self.rec_butt=Button(self.root,image=recp,command=self.create_rec)

            self.speech_text=Button(self.root,image=self.mic_photo,command=self.takevoiceinput)
            self.py_p=PhotoImage(file="lib/copy-png.png")
            self.pys_b=Button(self.root,image=self.py_p,command=self.kitin)

            self.textp=PhotoImage(file="lib/txtpng.png")
            self.rec_bu=Button(self.root,image=self.textp,command=self.new_text1,cursor="plus")


            if state=="yes":
                self.root.title(f"{username} (Authorised)")
                self.wiki['state'] = 'normal'
                self.speak_button['state'] = 'normal'
                self.google['state'] = 'normal'
                self.speech['state'] = 'normal'
                self.speech_text['state'] = 'normal'
                self.root.update()
            if state=="no":
                self.root.title("NO conection")
                self.wiki['state'] = 'disabled'
                self.speak_button['state'] = 'disabled'
                self.google['state'] = 'disabled'
                self.speech_text['state'] = 'disabled'
                self.speech['state'] = 'disabled'
                self.root.update()

            self.setup()
            setwin()
            self.root.mainloop()


        def new_text1(self):

            self.roottxt=Tk()

            def copy():
                cop.copy(f"{self.lb.get('1.0',END)}")
            def speak1():

                r1 = random.randint(1, 10000000)
                r2 = random.randint(1, 10000000)
                randfile = "text\ "+str(r2) + "randomtext" + str(r1) + ".mp3"
                tts = gTTS(text=f"{self.lb.get('1.0',END)}", lang="en-IN", slow=False)
                tts.save(randfile)
                playsound(randfile)
                os.remove(randfile)

            def wiki():
                try:


                    self.results = wikipedia.summary(f"({self.lb.get('1.0',END)})", sentences=1)
                    rc=self.lb.get('1.0',END)
                    self.lb.delete("1.0",END)
                    self.lb.insert('1.0',f'{rc}{self.results}')
                    self.roottxt.update()
                    r1 = random.randint(1, 10000000)
                    r2 = random.randint(1, 10000000)
                    randfile = "text\ "+str(r2) + "randomtext" + str(r1) + ".mp3"
                    tts = gTTS(text=self.results, lang="en-IN", slow=False)
                    tts.save(randfile)
                    playsound(randfile)
                    os.remove(randfile)

                except:

                    self.lb.insert('1.0',"no results")

            def takevoiceinput2():
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    self .var2.set("Listening...")
                    self.root.update()
                    print("Listening...")
                    r.pause_threshold = 1
                    r.energy_threshold = 400
                    audio = r.listen(source)
                try:
                    self.var2.set("Recognizing...")
                    self.root.update()
                    print("Recognizing")
                    self.query = r.recognize_google(audio, language="en-IN")

                except:
                    self.var2.set("NONE")
                    self.root.update()
                rc=self.lb.get('1.0',END)
                self.lb.delete("1.0",END)
                self.lb.insert('1.0',f'{rc}{self.query}')
                self.var2.set("None")
                self.root.update()
                print(self.query)
                return self.query


            self.roottxt.attributes("-topmost",True)
            self.dFont=tkFont.Font(family="Arial", size=30)
            self.bb=Button(self.roottxt,text="Mic",command=takevoiceinput2)
            if wrapornot == "dontwrape":
                self.lb=Text(self.roottxt,pady=40,width=25, height=4, font=self.dFont)
            if wrapornot=="wrape":
                self.lb=Text(self.roottxt,wrap=WORD,pady=40,width=25, height=4, font=self.dFont)
            self.wib=Button(self.roottxt,text="Wiki",command=wiki)
            self.speakb=Button(self.roottxt,text="Speak",command=speak1)
            self.co=Button(self.roottxt,text="Copy",command=copy)

            self.bb.pack()
            self.bb.place(x=0,y=0)
            self.wib.pack()
            self.wib.lift()
            self.wib.place(x=30,y=0)
            self.bb.lift()
            self.speakb.pack()
            self.speakb.lift()
            self.speakb.place(x=63,y=0)
            self.co.pack()
            self.co.lift()
            self.co.place(x=102,y=0)
            self.lb.pack(fill=BOTH, expand = YES)


            self.roottxt.mainloop()











        def copy1(self):
                cop.copy(f"{self.entry.get('1.0',END)}")

        def searchwiki(self):
            try:

                self.results = wikipedia.summary(f"({self.entry.get('1.0',END)})", sentences=1)
                df=self.entry.get("1.0",END)
                self.entry.delete("1.0",END)
                self.entry.insert('1.0',f"{df}{self.results}")
                self.root.update()
                r1 = random.randint(1, 10000000)
                r2 = random.randint(1, 10000000)
                randfile = "text\ "+str(r2) + "randomtext" + str(r1) + ".mp3"
                tts = gTTS(text=self.results, lang="en-IN", slow=False)
                tts.save(randfile)
                playsound(randfile)
                os.remove(randfile)

            except Exception as blahexcept:
                self.entry.insert('1.0',"no results")
        def kitin(self):

            cop.copy(f'{self.entry.get("1.0",END)}')







        def go_search(self):
            kit.search(f"{self.entry.get('1.0',END)}")

        def takevoiceinput(self):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                self .var2.set("Listening...")
                self.root.update()
                print("Listening...")
                r.pause_threshold = 1
                r.energy_threshold = 400
                audio = r.listen(source)
            try:
                self.var2.set("Recognizing...")
                self.root.update()
                print("Recognizing")
                self.query = r.recognize_google(audio, language="en-IN")

            except:
                self.var2.set("NONE")
                self.root.update()
            yob=self.entry.get("1.0",END)
            self.entry.delete("1.0",END)
            self.entry.insert('1.0',f"{yob}{self.query}")
            self.var2.set("None")
            self.root.update()
            print(self.query)
            return self.query






        def takeCommand(self):



            r = sr.Recognizer()
            with sr.Microphone() as source:
                self .var1.set("Listening...")
                self.root.update()
                print("Listening...")
                r.pause_threshold = 1
                r.energy_threshold = 400
                audio = r.listen(source)
            try:
                self.var1.set("Recognizing...")
                self.root.update()
                print("Recognizing")
                self.query = r.recognize_google(audio, language="en-IN")

            except:
                self.var1.set("NONE")
                self.root.update()


            self.var1.set(self.query)
            self.root.update()
            print(self.query)
            return self.query


        def setup(self):
            self.old_x = None
            self.old_y = None
            self.line_width = self.choose_size_button.get()
            self.color = self.DEFAULT_COLOR
            self.eraser_on = False
            self.active_button = self.pen_button
            self.c.bind('<B1-Motion>', self.paint)

            self.c.bind('<ButtonRelease-1>', self.reset)
        def speak(self):
            r1 = random.randint(1, 10000000)
            r2 = random.randint(1, 10000000)
            randfile = "text\ "+str(r2) + "randomtext" + str(r1) + ".mp3"
            tts = gTTS(text=f"{self.entry.get('1.0',END)}", lang="en-IN", slow=False)
            tts.save(randfile)
            playsound(randfile)
            os.remove(randfile)

        def clear(self):
            self.c.configure(bg="white")
            self.c.delete("all")

        def use_pen(self):
            self.activate_button(self.pen_button)
            self.ty="pen"

        def use_brush(self):
            self.activate_button(self.brush_button)
            self.ty="brush"

        def choose_color(self):
            self.eraser_on = False
            my_colo = askcolor(color=self.color)[1]
            print(self.color)
            self.color = my_colo
            print(self.color)
            self.root.update()

        def use_eraser(self):

            self.ty = "eraser"
            self.activate_button(self.eraser_button)
        def create_rec(self):
            self.eraser_on = False
            self.activate_button(self.rec_butt)
            self.ty = "rec"
        def activate_button(self, some_button, eraser_mode=False):
            self.active_button.config(relief=RAISED)
            some_button.config(relief=SUNKEN)
            self.active_button = some_button
            self.eraser_on = eraser_mode

        def paint(self, event):
            self.line_width = self.choose_size_button.get()
            paint_color=self.color
            if self.ty=="eraser":
                if self.old_x and self.old_y:
                    self.c.configure(cursor="circle")
                    self.c.create_line(self.old_x, self.old_y, event.x, event.y,width=self.line_width,fill="white",capstyle=ROUND, smooth=TRUE, splinesteps=50)
            if self.ty=="rec":
                if self.old_x and self.old_y:
                    self.c.configure(cursor="dotbox")
                    self.c.create_rectangle(event.x,event.y,event.x,event.y,width=self.line_width, fill=paint_color)


            if self.ty=="brush":
                self.c.configure(cursor="target")
                hi1=event.x+70

                if self.old_x and self.old_y:

                    self.c.create_line(self.old_x,self.old_y, hi1,event.y,
                                       width=self.line_width, fill=paint_color,
                                       capstyle=ROUND, smooth=TRUE, splinesteps=50)
            if self.ty=="pen":
                self.c.configure(cursor="tcross")
                if self.old_x and self.old_y:
                    self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                                       width=self.line_width, fill=paint_color,
                                       capstyle=ROUND, smooth=TRUE, splinesteps=500000000)
            self.old_x = event.x
            self.old_y = event.y

        def reset(self, event):
            self.old_x, self.old_y = None, None

    if __name__ == "__main__":
        Paint()
except Exception as eyo:
    print(eyo)


