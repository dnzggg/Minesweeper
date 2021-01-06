import random
from tkinter import *
from functools import partial
import threading


class board(threading.Thread):
    def __init__(self,tk,width,height,bomb):
        threading.Thread.__init__(self)
        self.tk = tk
        self.width = width
        self.height = height
        self.bomb = bomb
        self.widths = width
        self.heights = height
        self.bombs = bomb
        self.tk.config(bg = 'black')
        self.label = Label(tk, text="                     " + str(self.bomb), fg='white', bg='black',
                           font=(('helvetica'), 35))
        self.label.pack(fill=X, anchor=NE)
        self.menu = Menu(self.tk, tearoff=0)
        self.menu.add_command(label='Choose a new size', command=self.open)
        self.menu.add_command(label='Continue')
        self.label.bind('<Button-3>', self.pop)
        self.restart_button()
        self.tk.title('Minesweeper')
        self.can = Canvas(self.tk,width = self.width * 25,height=self.height*25,bg = 'black')
        self.can.pack()
        self.rectangles()
        self.mines()
        self.numbers()
        self.button()


    def look_for_finish(self):
        count = 0
        i = -1
        for col in range(0,self.height):
            for row in range(0,self.width):
                i += 1
                if self.buttons[i].winfo_exists() == 1:
                    count += 1
        a = self.bombs - self.bomb
        if (count - a) == 0:
            global stop
            stop = True
            global cool
            cool = cool.subsample(5)
            self.but.config(image = cool)
            self.tk.unbind('<Button-3>')


    def restart(self):
        global stop
        stop = True
        self.tk.destroy()
        tk = Tk()
        var = vars()
        timer = count(tk)
        back = board(tk, self.widths, self.heights, self.bombs)
        var.start()
        timer.start()
        back.start()
        tk.mainloop()


    def restart_button(self):
        global happy
        happy = happy.subsample(5)
        self.but = Button(self.tk,command = self.restart)
        self.but.pack()
        self.but.config(image = happy)
        self.but.place(relx=0.5, rely=0.1, anchor=CENTER)


    def rectangles(self):
        i = -1
        for col in range(0,self.height):
            for row in range(0,self.width):
                i += 1
                self.can.create_rectangle(row * 25,col * 25,row * 25 + 25,col * 25 + 25,outline = 'white' ,tags = str(i)+'r')


    def mines(self):
        self.arr = []
        for i in range(0,self.bomb):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            while self.can.find_withtag(str(x)+str(y)+'o') != ():
                x = random.randint(0, self.width-1)
                y = random.randint(0, self.height-1)
            self.can.create_oval(x * 25 + 3, y * 25 + 3, x * 25 + 22, y * 25 + 22, fill='white', tags=((str((y)*self.width+x)+'bo'),(str(x)+str(y)+'o')))
            self.arr.append(y*self.width+x)


    def numbers(self):
        self.labels = list()
        i = -1
        for col in range(0,self.height):
            for row in range(0,self.width):
                i += 1
                number = 0
                if (i + 1) % self.width != 0:
                    if self.can.find_withtag(str(i + 1)+'bo') != ():
                        number += 1
                if (i) % self.width != 0:
                    if self.can.find_withtag(str(i - 1)+'bo') != ():
                        number += 1
                if self.can.find_withtag(str(i - self.width)+'bo') != ():
                        number += 1
                if self.can.find_withtag(str(i + self.width)+'bo') != ():
                        number += 1
                if (i + 1) % self.width != 0:
                    if self.can.find_withtag(str(i + (self.width+1))+'bo') != ():
                        number += 1
                if (i) % self.width != 0:
                    if self.can.find_withtag(str(i + (self.width-1))+'bo') != ():
                        number += 1
                if (i) % self.width != 0:
                    if self.can.find_withtag(str(i - (self.width+1))+'bo') != ():
                        number += 1
                if  (i + 1) % self.width != 0:
                    if self.can.find_withtag(str(i -(self.width-1))+'bo') != ():
                        number += 1
                if self.can.find_withtag(str(i)+'bo') == ():
                    if number == 1:
                        self.can.create_rectangle((row) * 25, (col) * 25, row * 25 + 25, col * 25 + 25, outline='white',
                                                  tags=str(i) + 'num')
                        l = Label(self.can, text = str(number), font=("Helvetica", 10),bg = 'black',fg = 'deep sky blue')
                        l.pack()
                        l.place(x = row * 25 +7, y = col * 25 + 7, width=10, height=10)
                    elif number == 2:
                        self.can.create_rectangle((row) * 25, (col) * 25, row * 25 + 25, col * 25 + 25, outline='white',
                                                  tags=str(i) + 'num')
                        l = Label(self.can, text=str(number), font=("Helvetica", 10), bg='black', fg='chartreuse')
                        l.pack()
                        l.place(x=row * 25 + 7, y=col * 25 + 7, width=10, height=10)
                    elif number == 3:
                        self.can.create_rectangle((row) * 25, (col) * 25, row * 25 + 25, col * 25 + 25, outline='white',
                                                  tags=str(i) + 'num')
                        l = Label(self.can, text=str(number), font=("Helvetica", 10), bg='black', fg='red')
                        l.pack()
                        l.place(x=row * 25 + 7, y=col * 25 + 7, width=10, height=10)
                    elif number == 4:
                        self.can.create_rectangle((row) * 25, (col) * 25, row * 25 + 25, col * 25 + 25, outline='white',
                                                  tags=str(i) + 'num')
                        l = Label(self.can, text=str(number), font=("Helvetica", 10), bg='black', fg='blue')
                        l.pack()
                        l.place(x=row * 25 + 7, y=col * 25 + 7, width=10, height=10)
                    elif number == 5:
                        self.can.create_rectangle((row) * 25, (col) * 25, row * 25 + 25, col * 25 + 25, outline='white',
                                                  tags=str(i) + 'num')
                        l = Label(self.can, text=str(number), font=("Helvetica", 10), bg='black', fg='red4')
                        l.pack()
                        l.place(x=row * 25 + 7, y=col * 25 + 7, width=10, height=10)
                    elif number == 6:
                        self.can.create_rectangle((row) * 25, (col) * 25, row * 25 + 25, col * 25 + 25, outline='white',
                                                  tags=str(i) + 'num')
                        l = Label(self.can, text=str(number), font=("Helvetica", 10), bg='black', fg='azure3')
                        l.pack()
                        l.place(x=row * 25 + 7, y=col * 25 + 7, width=10, height=10)
                    elif number == 7:
                        self.can.create_rectangle((row) * 25, (col) * 25, row * 25 + 25, col * 25 + 25, outline='white',
                                                  tags=str(i) + 'num')
                        l = Label(self.can, text=str(number), font=("Helvetica", 10), bg='black', fg='white')
                        l.pack()
                        l.place(x=row * 25 + 7, y=col * 25 + 7, width=10, height=10)
                    elif number == 8:
                        self.can.create_rectangle((row) * 25, (col) * 25, row * 25 + 25, col * 25 + 25, outline='white',
                                                  tags=str(i) + 'num')
                        l = Label(self.can, text=str(number), font=("Helvetica", 10), bg='black', fg='gray')
                        l.pack()
                        l.place(x=row * 25 + 7, y=col * 25 + 7, width=10, height=10)
                    else:
                        pass;


    def button(self):
        self.buttons = list()
        i = -1
        for col in range(0, self.height):
            for row in range(0, self.width):
                i += 1
                self.buttons.append(Button(self.can, text=' ', height=1, width=2, bg='gray8',
                                command=partial(self.left_click,i)))
                self.buttons[-1].place(x= (row) * 25, y=(col) * 25)
        self.tk.bind('<Button-3>', self.right_click)


    def left_click(self, n):
        global start
        start = True
        self.look_for_delete(n)
        self.look_for_finish()


    def right_click(self, event):
        try:
            if event.widget['text'] == ' ':
                self.v = '<|'
                self.bomb -= 1
                self.label.config(text = str(self.bomb),anchor=NE)
                event.widget.config(text=self.v, fg='red')
                self.look_for_finish()
            elif event.widget['text'] == '<|':
                self.v = '?'
                event.widget.config(text=self.v,fg = 'white')
                self.bomb += 1
                self.label.config(text=str(self.bomb), anchor=NE)
            elif event.widget['text'] == '?':
                self.v = ' '
                event.widget.config(text=self.v)
        except:
            pass


    def look_for_delete(self,n):
        global stop
        if stop == False:
            if self.buttons[n]['text'] == ' ':
                if self.can.find_withtag(str(n)+'bo') != ():
                    i = 0
                    stop = True
                    global sad
                    sad = sad.subsample(5)
                    self.but.config(image = sad)
                    for col in range(0, self.width):
                        for row in range(0, self.height):
                            i += 1
                            if self.can.find_withtag(str(i)+'bo') != ():
                                self.buttons[i].destroy()
                    self.tk.unbind('<Button-3>')
                elif self.can.find_withtag(str(n)+'bo') or self.can.find_withtag(str(n)+'num')  == ():
                     self.open_which(n)
                elif self.can.find_withtag(str(n)+'num'):
                    self.buttons[n].destroy()


    def open_which(self,n):
        #x#
        ###
        ###
        if n > self.width:
            if self.can.find_withtag(str(n-self.width) + 'bo') == () and self.buttons[n-self.width].winfo_exists() == 1:
                if self.buttons[n-self.width]['text'] == ' ':
                    self.buttons[n - self.width].destroy()
                    if self.can.find_withtag(str(n-self.width) + 'num') == ():
                        self.open_which(n - self.width)
        ###
        ###
        #x#
        try:
            if self.can.find_withtag(str(n+self.width) + 'bo') == () and self.buttons[n+self.width].winfo_exists() == 1:
                if self.buttons[n + self.width]['text'] == ' ':
                    self.buttons[n + self.width].destroy()
                    if self.can.find_withtag(str(n+self.width) + 'num') == ():
                        self.open_which(n + self.width)
        except:
            pass;
        ###
        ##x
        ###
        if (n + 1)%self.width != 0:
            if self.can.find_withtag(str(n+1) + 'bo') == ()and self.buttons[n+1].winfo_exists() == 1:
                if self.buttons[n + 1]['text'] == ' ':
                    self.buttons[n + 1].destroy()
                    if self.can.find_withtag(str(n+1) + 'num') == ():
                        self.open_which(n + 1)
         ###
        #x##
         ###
        if (n) % self.width != 0:
            if self.can.find_withtag(str(n-1) + 'bo') == ()and self.buttons[n-1].winfo_exists() == 1:
                if self.buttons[n - 1]['text'] == ' ':
                    self.buttons[n - 1].destroy()
                    if self.can.find_withtag(str(n-1) + 'num') == ():
                        self.open_which(n - 1)
        #x##
         ###
         ###
        if n > self.width and (n) % self.width != 0:
            if self.can.find_withtag(str(n - (self.width+1)) + 'bo') == () and self.buttons[n - (self.width+1)].winfo_exists() == 1:
                if self.buttons[n - (self.width+1)]['text'] == ' ':
                    self.buttons[n - (self.width+1)].destroy()
                    if self.can.find_withtag(str(n - (self.width+1)) + 'num') == ():
                        self.open_which(n - (self.width+1))
        ##x
        ###
        ###
        if n > self.width and (n + 1)%self.width != 0:
            if self.can.find_withtag(str(n - (self.width-1)) + 'bo') == () and self.buttons[n - (self.width-1)].winfo_exists() == 1:
                if self.buttons[n - (self.width - 1)]['text'] == ' ':
                    self.buttons[n - (self.width-1)].destroy()
                    if self.can.find_withtag(str(n - (self.width-1)) + 'num') == ():
                        self.open_which(n - (self.width-1))
        ###
        ###
        ##x
        try:
            if (n ) % self.width != 0:
                if self.can.find_withtag(str(n+(self.width-1)) + 'bo') == () and self.buttons[n+(self.width-1)].winfo_exists() == 1:
                    if self.buttons[n + (self.width - 1)]['text'] == ' ':
                        self.buttons[n + (self.width-1)].destroy()
                        if self.can.find_withtag(str(n+(self.width-1)) + 'num') == ():
                            self.open_which(n + (self.width-1))
        except:
            pass;
         ###
         ###
        #x##
        try:
            if (n + 1) % self.width != 0:
                if self.can.find_withtag(str(n+(self.width+1)) + 'bo') == () and self.buttons[n+(self.width+1)].winfo_exists() == 1:
                    if self.buttons[n + (self.width + 1)]['text'] == ' ':
                        self.buttons[n + (self.width+1)].destroy()
                        if self.can.find_withtag(str(n+(self.width+1)) + 'num') == ():
                            self.open_which(n + (self.width+1))
        except:
            pass;
        self.buttons[n].destroy()


    def open(self):
        self.tk.destroy()
        tk = Tk()
        menu(tk)
        mainloop()


    def pop(self,event):
        self.menu.post(event.x_root,event.y_root)


class count(threading.Thread):
    def __init__(self,tk):
        threading.Thread.__init__(self)
        self.tk = tk
        self.label = Label(tk,text="",fg = 'white',bg = 'black',font = (('helvetica'),35))
        self.label.pack(anchor = NW,fill = X)
        self.menu = Menu(self.tk, tearoff=0)
        self.menu.add_command(label='Choose a new size', command=self.open)
        self.menu.add_command(label='Continue')
        self.label.bind('<Button-3>', self.pop)
        self.i = 0
        self.update_clock()


    def update_clock(self):
        global stop
        global start
        if stop == False and start == True:
            self.i += 1
        else:
            pass
        self.label.configure(text=str(self.i) +'                            ')
        self.label.after(1000, self.update_clock)


    def open(self):
        self.tk.destroy()
        tk = Tk()
        menu(tk)
        mainloop()


    def pop(self,event):
        self.menu.post(event.x_root,event.y_root)


class menu():
    def __init__(self,tk):
        self.tk = tk
        self.tk.geometry("300x300-800+120")
        self.tk.config(bg='black')
        self.tk.title('Menu')

        self.v = StringVar()
        self.widt = Entry(self.tk,text = self.v,bg = 'black',fg = 'white',width = 15,bd=1,font = ('Helvetica',15))
        self.widt.pack()
        self.widt.bind("<Button-1>", self.deletewidth)
        self.v.set('Width here')
        self.widt.place(relx=0.32, rely=0.3, anchor=CENTER)

        self.a = StringVar()
        self.heigh = Entry(self.tk, text=self.a, bg='black', fg='white',width = 15,bd=1,font = ('Helvetica',15))
        self.heigh.pack()
        self.heigh.place(relx=0.69, rely=0.42, anchor=CENTER)
        self.heigh.bind("<Button-1>", self.deleteheight)
        self.a.set('Height here')

        self.b = StringVar()
        self.bom = Entry(self.tk, text=self.b, bg='black', fg='white', width=15, bd=1, font=('Helvetica', 15))
        self.bom.pack()
        self.bom.place(relx=0.32, rely=0.6, anchor=CENTER)
        self.bom.bind("<Button-1>", self.deletebomb)
        self.b.set('Bomb here')

        self.button = Button(self.tk,text = 'Play game',bg = 'black',fg = 'white',font = ('Helvetica',20),command = self.look_for_int)
        self.button.pack()
        self.button.place(relx=0.6, rely=0.8, anchor=CENTER)

        L = Label(self.tk, text='Welcome to Minesweeper', fg='White', bg='black', font='avantgarde50')
        L.pack()
        L.place(relx=0.5, rely=0.1, anchor=CENTER)


    def deletewidth(self,event):
        self.v.set('')
        self.widt.unbind("<Button-1>")


    def deleteheight(self,event):
        self.a.set('')
        self.heigh.unbind("<Button-1>")


    def deletebomb(self,event):
        self.b.set('')
        self.bom.unbind("<Button-1>")


    def play(self):
        if  (0 < self.width < 40) and (0 < self.height < 40) and (self.bomb <= self.width*self.height/4):
            self.tk.destroy()
            tk = Tk()
            var = vars()
            timer = count(tk)
            back = board(tk,self.width,self.height,self.bomb)
            var.start()
            timer.start()
            back.start()
            tk.mainloop()
        else:
            messagebox.showerror('Error','Width or height can not be more than 40 and bomb is a quarter of the board.')


    def look_for_int(self):
        try:
            self.width = int(self.v.get())
            try:
                self.height = int(self.a.get())
                try:
                    self.bomb = int(self.b.get())
                    self.play()
                except:
                    self.bomb = int(self.width*self.height/4)
                    self.play()
            except:
                self.height = self.width
                try:
                    self.bomb = int(self.b.get())
                    self.play()
                except:
                    self.bomb = int(self.width*self.height/4)
                    self.play()
        except:
            try:
                self.height = int(self.a.get())
                self.width = self.height
                try:
                    self.bomb = int(self.b.get())
                    self.play()
                except:
                    self.bomb = int(self.width*self.height/4)
                    self.play()
            except:
                self.height = 16
                self.width = 31
                try:
                    self.bomb = int(self.b.get())
                    self.play()
                except:
                    self.bomb = 99
                    self.play()


class vars(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global stop
        stop = False
        global start
        start = False
        global happy
        happy = PhotoImage(file='happy.gif')
        global sad
        sad = PhotoImage(file = 'sad.gif')
        global cool
        cool = PhotoImage(file = 'cool.gif')


tk = Tk()
menu(tk)
mainloop()
