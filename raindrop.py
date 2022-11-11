import random
import tkinter as tk

#from tkinter import ttk
from matplotlib import pyplot as plt

root = tk.Tk()
root.title("raindrop")
root.geometry('600x600')

class Cannon:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.draw()
        self.bind()

    def draw(self):       
        self.id = cv.create_oval(self.x-10, self.y-10, self.x+10, self.y+10
            ,activefill="pink",fill="cyan", tag="cannon")
        

    def bind(self):
        frame1.focus_set()
        frame1.bind("<Left>",self.side_move)
        frame1.bind("<Right>",self.side_move)
        frame1.bind("<Up>",self.side_move)
        frame1.bind("<Down>",self.side_move)
    def side_move(self,event):
        if event.keysym == "Left":
            cv.move(self.id,-15,0)
            self.x-=15
        elif event.keysym == "Right":
            cv.move(self.id,15,0)
            self.x+=15
        elif event.keysym == "Up":
            cv.move(self.id,0,-15)
            self.y-=15
        else:
            cv.move(self.id,0,15)
            self.y+=15

    def enemy_move(self):
        t=random.randint(-10,10)
        cv.move(self.id2,t,0)
        root.after(200, self.enemy_move)


class Enemy:
    def __init__(self):
        self.x = random.randint(0,500)
        self.y = 0
        self.size = random.randint(10,50)
        self.color = random.choice(("black","white","blue","red","green","yellow"))
        self.speed = random.randint(5,10)
        self.draw()
        self.move()
    def draw(self):
        self.id= cv.create_oval(self.x-self.size,self.y-self.size
        ,self.x+self.size,self.y+self.size,fill=self.color,tag="enemy")
    def move(self):
        cv.move(self.id,0,self.speed)
        self.y+=self.speed
        root.after(100, self.move)
        self.collision()
    def collision(self):
        if ((self.x-cannon.x)**2+(self.y-cannon.y)**2) < (10+self.size)**2:
            gameover()
    

def enemy_spown():
    enemy=Enemy()
    root.after(500,enemy_spown)

def gameover():  # ゲームオーバー判定
    cv.delete("cannon")
    cv.create_text(300, 300, text="GAME OVER",
                fill="red", font=("System", 90))
# 初期描画
# インスタンス生成

frame1 = tk.Frame(root, bd=4, relief='groove',bg='gray')
frame1.grid(row=0, column=0)
frame2 = tk.Frame(root, bd=4, relief='groove',bg='black')
frame2.grid(row=1, column=0)
cv = tk.Canvas(frame1, bg="gray",width=600,height=600)
cv.grid(row=2, column=0)
#button1 = tk.Button(frame2, text='Run',fg='blue',font=('',14,'bold'))
#button1.pack()
#label1 = tk.Label(frame2, bg='blue', fg='white', font=('',20,'bold'), text="")
#label1.pack(fill="both")
cannon=Cannon(250,400)
enemy_spown()


root.mainloop()
