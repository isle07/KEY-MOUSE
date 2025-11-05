# ...existing code...
from tkinter import *
from tkinter import ttk, messagebox
import pyautogui
import time
import threading

pyautogui.FAILSAFE = True

# 기본 설정
root = Tk()
root.title("KEY-MOUSE")
root.geometry("420x260")
root.resizable(False, False)
pad = {"padx": 8, "pady": 6}
pyautogui.PAUSE = 0

# 스타일 (ttk로 약간 다듬음)
style = ttk.Style(root)
style.theme_use("default")


# 변수
repeat_var = StringVar(value="10")
cps_var = StringVar(value="1")
x_var = StringVar(value="0")
y_var = StringVar(value="0")
status_var = StringVar(value="행복한 오토 마우스^^")

click_thread = None
stop_event = threading.Event()

# 레이아웃
main = ttk.Frame(root)
main.pack(fill="both", expand=True, **pad)

status_label = ttk.Label(main, textvariable=status_var, anchor="center")
status_label.grid(row=0, column=0, columnspan=3, sticky="ew", **pad)

ttk.Label(main, text="반복 횟수:").grid(row=1, column=0, sticky="e")
repeat_entry = ttk.Entry(main, textvariable=repeat_var, width=12)
repeat_entry.grid(row=1, column=1, sticky="w")

ttk.Label(main, text="CPS (초당 클릭):").grid(row=2, column=0, sticky="e")
cps_entry = ttk.Entry(main, textvariable=cps_var, width=12)
cps_entry.grid(row=2, column=1, sticky="w")

ttk.Label(main, text="X:").grid(row=3, column=0, sticky="e")
x_entry = ttk.Entry(main, textvariable=x_var, width=12)
x_entry.grid(row=3, column=1, sticky="w")

ttk.Label(main, text="Y:").grid(row=4, column=0, sticky="e")
y_entry = ttk.Entry(main, textvariable=y_var, width=12)
y_entry.grid(row=4, column=1, sticky="w")

def validate_positive_int(value, name):
    try:
        v = int(value)
        if v <= 0:
            raise ValueError
        return v
    except Exception:
        messagebox.showerror("입력 오류", f"{name}에 자연수를 입력하세요.")
        return None

def capture_position(delay=3):
    status_var.set(f"{delay}초 후 현재 마우스 위치를 캡쳐합니다...")
    root.update_idletasks()
    time.sleep(delay)
    x, y = pyautogui.position()
    x_var.set(str(x))
    y_var.set(str(y))
    status_var.set(f"캡처 완료: ({x},{y})")

def start_clicking_thread():
    global click_thread, stop_event
    if click_thread and click_thread.is_alive():
        return
    repeat = validate_positive_int(repeat_var.get(), "반복 횟수")
    cps = validate_positive_int(cps_var.get(), "CPS")
    try:
        x = int(x_var.get())
        y = int(y_var.get())
    except Exception:
        messagebox.showerror("입력 오류", "좌표는 정수여야 합니다.")
        return
    if repeat is None or cps is None:
        return

    delay = 1.0 / cps
    stop_event.clear()

    def worker():
        status_var.set("클릭 시작...")
        for i in range(repeat):
            if stop_event.is_set():
                status_var.set("중지됨")
                break
            pyautogui.moveTo(x, y)
            pyautogui.click()
            status_var.set(f"진행: {i+1}/{repeat}")
            # Sleep in small increments so stop can be responsive
            slept = 0.0
            while slept < delay:
                if stop_event.is_set():
                    break
                time.sleep(min(0.05, delay - slept))
                slept += 0.05
        else:
            status_var.set("작업 완료")
        start_btn.config(state="normal")
        stop_btn.config(state="disabled")

    start_btn.config(state="disabled")
    stop_btn.config(state="normal")
    click_thread = threading.Thread(target=worker, daemon=True)
    click_thread.start()

def stop_clicking():
    stop_event.set()

def capture_dialog():
    if messagebox.askyesno("포지션 캡처", "3초 후 현재 마우스 위치를 캡처합니다. 준비되었습니까?"):
        threading.Thread(target=capture_position, args=(3,), daemon=True).start()

# 버튼
btn_frame = ttk.Frame(main)
btn_frame.grid(row=5, column=0, columnspan=3, pady=(10,0))

start_btn = ttk.Button(btn_frame, text="시작", command=start_clicking_thread)
start_btn.grid(row=0, column=0, padx=6)

stop_btn = ttk.Button(btn_frame, text="중지", command=stop_clicking, state="disabled")
stop_btn.grid(row=0, column=1, padx=6)

capture_btn = ttk.Button(btn_frame, text="마우스 위치 캡처", command=capture_dialog)
capture_btn.grid(row=0, column=2, padx=6)

# 단축키: Esc로 중지
root.bind("<Escape>", lambda e: stop_clicking())

root.mainloop()
# ...existing code...
