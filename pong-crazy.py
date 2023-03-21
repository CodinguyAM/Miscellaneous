from tkinter import *
import random
import time

class Ball:
    def __init__(self, paddle, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color, outline="white")
        self.canvas.move(self.id, 245, 100)
        starts = [1, -1]
        random.shuffle(starts)
        self.vx = starts[0] * random.choice(list(range(1, 6)))
        self.vy = -2
        self.y_limit = self.canvas.winfo_height()
        self.x_limit = self.canvas.winfo_width()
        self.paddle = paddle

    def draw(self):
         self.canvas.move(self.id, self.vx, self.vy)
         self.pos = self.canvas.coords(self.id)
         pos = self.pos
         if (pos[1] <= 0) or (self.hit_paddle()):
             self.vy = self.vy * -1

         if (pos[0] <= 0) or (pos[2] >= self.x_limit):
             self.vx = self.vx * -1

    def hit_paddle(self):
        pos = self.canvas.coords(self.id)
        paddle_pos = self.canvas.coords(self.paddle.id)
        return (((pos[2] >= paddle_pos[0]) and (pos[0] <= paddle_pos[2])) and ((pos[3] >= paddle_pos[1]) and (pos[1] <= paddle_pos[3])))

class Paddle:

    
    def turn_left(self, evt):
        self.v = self.v -2
        #print("LEFT!!")
        
    def turn_right(self, evt):
        self.v = self.v + 2
        #print("RIGHT!!")

    
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(0, 0, 100, 10, fill=color, outline = "white")
        self.canvas.move(self.id, 200, 300)
        self.v = 0
        self.x_limit = canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.v, 0)
        self.pos = self.canvas.coords(self.id)
        pos = self.pos
        #print(self.v)
        if (pos[0] <= 0) or (pos[2] >= self.x_limit):
            self.v = self.v * -1
            #uncomment for a super bouncy paddle!
            #self.v = 0

tk = Tk()
tk.title("PONG")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0, bg = 'white')
canvas.pack()
tk.update()

paddle = Paddle(canvas, "green")
balls = []
for balln in range(7):
    balls.append(Ball(paddle, canvas, random.choice(["red", "blue", "yellow", "cyan"])))
    
while True:
    for ball in balls:
        ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
