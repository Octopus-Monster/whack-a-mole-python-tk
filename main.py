import tkinter as tk
from tkinter import messagebox
import random

# 创建主窗口
window = tk.Tk()
window.title("打地鼠游戏")
window.geometry("500x500")

# 定义全局变量
score = 0  # 分数
time = 60  # 倒计时
running = False  # 游戏状态
mole_state = {}  # 按钮状态
mole_image = {}  # 按钮图片

# 定义按钮图片
mole_image["hole"] = tk.PhotoImage(file="pic\\hole.png")  # 洞穴图片
mole_image["mole"] = tk.PhotoImage(file="pic\\mole.png")  # 地鼠图片
mole_image["hit_mole"] = tk.PhotoImage(file="pic\\hit_mole.png")  # 地鼠打中图片
mole_image["rabbit"] = tk.PhotoImage(file="pic\\rabbit.png")  # 兔子图片
mole_image["hit_rabbit"] = tk.PhotoImage(file="pic\\hit_rabbit.png")  # 兔子打中图片


# 定义开始游戏函数
def start_game():
    global running, time, score
    if not running:  # 如果游戏未开始
        running = True  # 设置游戏状态为开始
        time = 60  # 重置倒计时
        score = 0  # 重置分数
        update_time()  # 更新倒计时显示
        update_score()  # 更新分数显示
        update_mole()  # 更新按钮状态


# 定义更新倒计时函数
def update_time():
    global running, time
    if running:  # 如果游戏正在进行
        time -= 1  # 倒计时减一秒
        time_label.config(text=f"倒计时: {time} 秒")  # 更新倒计时显示
        if time > 0:  # 如果倒计时未结束
            window.after(1000, update_time)  # 一秒后再次调用该函数
        else:  # 如果倒计时结束
            running = False  # 设置游戏状态为结束
            tk.messagebox.showinfo("游戏结束", f"你的最终得分是: {score} 分")  # 弹出提示框显示最终得分


# 定义更新分数函数
def update_score():
    global score
    score_label.config(text=f"分数: {score}")  # 更新分数显示


# 定义更新按钮状态函数
def update_mole():
    global running, mole_state
    if running: # 如果游戏正在进行
        # 定义一个空列表，用来存放随机选出的按钮索引
        random_index = []
        # 随机选出3个地鼠按钮
        random_index += random.sample(range(16), 3)
        # 随机选出1个兔子按钮，且不能与地鼠按钮重复
        random_index += random.sample(list(set(range(16)) - set(random_index)), 1)
        # 遍历所有按钮
        for i in range(16):
            # 如果按钮索引在随机列表中
            if i in random_index:
                # 根据索引位置设置按钮状态为地鼠或兔子
                mole_state[i] = "mole" if random_index.index(i) < 3 else "rabbit"
            else: # 如果按钮索引不在随机列表中
                # 设置按钮状态为洞穴
                mole_state[i] = "hole"
            # 更新按钮图片
            mole_button[i].config(image=mole_image[mole_state[i]])
        # 三秒后再次调用该函数
        window.after(1500, update_mole)


# 定义点击按钮函数
def hit_mole(i):
    global running, score, mole_state
    if running:  # 如果游戏正在进行
        if mole_state[i] == "mole":  # 如果点击的是地鼠
            score += 5  # 分数加五分
            mole_state[i] = "hit_mole"  # 设置按钮状态为地鼠打中
            mole_button[i].config(image=mole_image[mole_state[i]])  # 更新按钮图片
            update_score()  # 更新分数显示
        elif mole_state[i] == "rabbit":  # 如果点击的是兔子
            score -= 10  # 分数减十分
            mole_state[i] = "hit_rabbit"  # 设置按钮状态为兔子打中
            mole_button[i].config(image=mole_image[mole_state[i]])  # 更新按钮图片
            update_score()  # 更新分数显示


# 创建开始游戏按钮
start_button = tk.Button(window, text="开始游戏", command=start_game)
start_button.place(x=200, y=50)

# 创建分数显示标签
score_label = tk.Label(window, text=f"分数: {score}")
score_label.place(x=20, y=100)

# 创建倒计时显示标签
time_label = tk.Label(window, text=f"倒计时: {time} 秒")
time_label.place(x=20, y=130)

# 创建16个方格按钮
mole_button = []
for i in range(16):
    x = (i % 4 + 1) * 100  # 计算按钮的横坐标
    y = (i // 4 + 1) * 100  # 计算按钮的纵坐标
    mole_state[i] = "hole"  # 初始化按钮状态为洞穴
    button = tk.Button(window, image=mole_image[mole_state[i]])  # 创建按钮，初始为不可点击状态
    button.place(x=x, y=y)  # 放置按钮
    button.bind("<Button-1>", lambda event, i=i: hit_mole(i))  # 绑定点击事件
    mole_button.append(button)  # 将按钮添加到列表中

# 进入主循环
window.mainloop()
