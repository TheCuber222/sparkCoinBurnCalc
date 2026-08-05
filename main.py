import tkinter as tk
from tkinter import messagebox

def calculate():
    """根据输入的净销毁数，计算需要一次性焚烧的数量"""
    text = entry.get().strip()
    if not text:
        messagebox.showwarning("提示", "请输入净销毁数量")
        return

    try:
        x = int(text)
    except ValueError:
        messagebox.showerror("错误", "请输入正整数")
        return

    if x <= 0:
        messagebox.showerror("错误", "净销毁数必须为正整数")
        return

    # 公式：需焚烧 = x + floor(x / 9)
    need_burn = x + x // 9

    # 显示结果
    label_result.config(text=f"需一次性焚烧：{need_burn} 个")

root = tk.Tk()
root.title("火花币焚烧计算器")
root.geometry("320x150")
root.resizable(False, False)

# 输入区域
tk.Label(root, text="净销毁数量：").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=1, padx=10, pady=10)
entry.focus()

# 计算按钮
btn = tk.Button(root, text="计算", command=calculate, width=10)
btn.grid(row=1, column=0, columnspan=2, pady=5)

# 结果显示
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
