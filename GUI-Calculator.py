import tkinter as tk
from tkinter import messagebox

#更新輸入框
def press(key):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + key)

#清空輸入框
def clear():
    entry.delete(0, tk.END)

#計算結果並顯示
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("錯誤", "除以0錯誤！")
    except Exception as e:
        messagebox.showerror("錯誤", f"無效的輸入！\n{e}")


#主視窗
root = tk.Tk()
root.title("介面計算機")

#輸入框
entry = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=5, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#按鈕設置
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9',1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text = text, width=5, height=2, font=("Arail", 15), command= calculate)
    elif text == 'C':
        btn = tk.Button(root, text = text, width=5, height=2, font=("Arail", 15), command= clear)
    else:
        btn = tk.Button(root, text = text, width=5, height=2, font=("Arail", 15), command = lambda t=text:press(t))
    btn.grid(row = row, column=col, padx=5, pady=5)

#運行主迴圈
root.mainloop()