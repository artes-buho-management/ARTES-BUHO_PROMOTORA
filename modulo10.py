import tkinter as tk

SHIFT = 3

def cesar(*args):
    new = []
    for char in entry_var.get():
        if char.isalpha():
            cod = ord(char) + SHIFT
            if cod > ord('z'):
                cod -= 26
            new.append(chr(cod))
        else:
            new.append(char)
    label_var.set("".join(new))


root = tk.Tk()
root.title("Ticua cipher gui (TCG)")
root.resizable(0, 0)
root.geometry("480x480")

entry_var = tk.StringVar(root)
label_var = tk.StringVar(root)
entry_var.trace("w", cesar)

entry = tk.Entry(root, textvariable=entry_var)
entry.place(x=50, y=50)
w = tk.Label(root, textvariable=label_var)
w.pack()

root.mainloop()