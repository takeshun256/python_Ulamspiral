from tkinter import *
from tkinter import ttk

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#素数判定するis_prime関数
def is_prime(n):
    if n <= 1:
        return False
    for m in range(2, n):
        if m * m > n:
            return True
        if n % m == 0:
            return False

#条件に応じた数字を色付けした螺旋のグラフを出力するscatter_maker関数
def scatter_maker(num):
    fig = plt.Figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    n = 100
    #xy座標から螺旋上の数字を出力するfind_number関数
    def find_number(xx,yy):
        x = xx - n
        y = yy - n
        t = max(abs(x),abs(y))
        if x == y == 0: # 中心
            return 1
        elif y < x and y >= -x: 
            # y < x,y >= -x領域
            return (4*(t**2) + 2*t + 1 + t + y)
        elif y >= x and y > -x:
            # y >= x  y > -x領域
            return (4*(t**2) + 4*t + 1 + t + x)
        elif y > x and y <= -x:
            # y > x  y <= -x領域
            return (4*(t**2) - 2*t + 1 + t + y) 
        elif y <= x and y < -x:
            # y <= x  y < -x領域
            return (4*(t**2) + 1 + t + x)
    #条件に応じた数字を色付けした螺旋を２重リストで出力するcells_maker関数
    def cells_maker(num):
        cells = [[0 for _ in range(2 * n + 1)] for _ in range(2 * n + 1)]

        for y in range(0,2 * n + 1):
            for x in range(0,2 * n + 1):
                if num == 1:
                    if is_prime(find_number(x,y)):
                     cells[y][x] = 1
                else:
                    if find_number(x,y) % num  == 0:
                        cells[y][x] = 1
        return cells

    cells=cells_maker(num)
    x = []
    y = []
    cells_x = len(cells[0])
    cells_y = len(cells)
    for i in range(cells_y):
        for j in range(cells_x):
            if cells[i][j] == 1:
                x.append(j)
                y.append(i)
    ax.scatter(x,y, s=0.3, c='blue')
    return fig
#scatter_makerにテキスト内の数字を入力しグラフを表示するbutton_run関数
def button_run():
    text_input_num = int(text.get())
    scat_fig = scatter_maker(text_input_num)
    canvas = FigureCanvasTkAgg(scat_fig, frame_2)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)

# 以下、rootの構成
root = Tk()
root.title('Ulam spiral')
root.geometry('1300x1350')

# widgetの設定
frame_1 = Frame(root, bd=4, relief='groove',bg='blue')
frame_2 = Frame(root, bd=4, relief='groove',bg='blue')
label_1 = Label(frame_1, bg='blue', fg='white', font=('',20,'bold'), text='Program to create "Ulam Spiral"')
label_2 = Label(frame_1, bg='#a9ceec', fg='black', text='What is Ulam spiral?\n\
The distribution of prime numbers is visualized by arranging them on a two-dimensional plane according to certain simple rules.\n\
It was discovered by mathematician Stanislaw Ulam in 1963.')
label_3 = Label(frame_1, bg='#a9ceec', fg='black', text='↓Select a number in the text box\n\
If 1, a prime spiral is displayed; if 2 or more, a spiral that is a multiple of that number is displayed.')
valuelist = [i for i in range(1,100)]
text = ttk.Combobox(frame_1,values=valuelist,width = 2)
button = Button(frame_1, text='Run',fg='blue',font=('',14,'bold'), command=button_run)
scat_fig=scatter_maker(1)
canvas = FigureCanvasTkAgg(scat_fig, frame_2)

# widgetの配置
frame_1.grid(row=0, column=0, sticky=W + E)
frame_2.grid(row=1, column=0)
label_1.pack(fill=X)
label_2.pack(fill=X)
label_3.pack(fill=X)
text.pack()
button.pack()
canvas.get_tk_widget().grid(row=0, column=0)

root.mainloop()