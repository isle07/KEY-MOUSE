from tkinter import *
import pyautogui
import time

# 기본 설정
root = Tk()
root.title("KEY-MOUSE")
root.geometry("800x600")
root.resizable(False, False)

# 라벨 및 입력 필드
status_label = Label(root, text="행복한 오토 마우스^^")
status_label.pack()

repeat_entry = Entry(root, width=30)
repeat_entry.pack()
repeat_entry.pack_forget()

cps_Entry = Entry(root, width=30)
cps_Entry.pack()
cps_Entry.pack_forget()

x_entry = Entry(root, width=30)
x_entry.pack()
x_entry.pack_forget()

y_entry = Entry(root, width=30)
y_entry.pack()
y_entry.pack_forget()

# 버튼 함수들
def ask_repeat_count():
    status_label.config(text="반복할 횟수(자연수만)")
    start_button.pack_forget()
    repeat_entry.pack_configure()
    next_button.config(command=ask_cps)
    next_button.pack()

def ask_cps():
    global cps_count
    status_label.config(text="속도 설정: 초당 몇 번 클릭하는 속도가 좋습니까")
    repeat_entry.pack_forget()
    cps_Entry.pack()
    next_button.config(command=ask_coordinates)
    cps_count = int(cps_Entry.get())

def ask_coordinates():
    global repeat_count
    status_label.config(text="위치 지정(위:x좌표, 아래:y좌표)(자연수만)")
    repeat_entry.pack_forget()
    cps_Entry.pack_forget()
    x_entry.pack_configure()
    y_entry.pack_configure()
    next_button.pack_forget()
    next_button.pack_configure()
    next_button.config(command=confirm_start)
    repeat_count = int(repeat_entry.get())

def confirm_start():
    global x_pos, y_pos
    x_pos = int(x_entry.get())
    y_pos = int(y_entry.get())
    x_entry.pack_forget()
    y_entry.pack_forget()
    status_label.config(text="정말 시작하시겠습니까?")
    next_button.config(command=start_clicking)

def start_clicking():
    for _ in range(repeat_count):
        pyautogui.moveTo(x_pos, y_pos)
        pyautogui.click()
        time.sleep(1)

# 버튼
start_button = Button(root, text='시작', padx=30, pady=10, command=ask_repeat_count)
start_button.pack()

next_button = Button(root, text='계속', padx=20, pady=5, command=ask_coordinates)
next_button.pack()
next_button.pack_forget()

root.mainloop()
