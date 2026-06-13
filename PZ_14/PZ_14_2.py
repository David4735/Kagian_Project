import tkinter as tk

root = tk.Tk()
root.title("Метры")

tk.Label(root, text="Расстояние L (см):").pack()
entry = tk.Entry(root)
entry.pack()

result = tk.Label(root, text="")
result.pack()

def calc():
    L = int(entry.get())
    result.config(text=f"Полных метров: {L // 100}")

tk.Button(root, text="Вычислить", command=calc).pack()
root.mainloop()