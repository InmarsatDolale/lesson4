import tkinter as tk


def username():
    name = entry.get()
    label.config(text=f'Привет, {name}!')
    if name == '':
        label.config(text='Ошибка ввода: поле не должно быть пустым, введите имя')
        return
    try:
        float(name)
        label.config(text='Ошибка ввода: имя не должно быть числом')
        return
    except ValueError:
        pass

root = tk.Tk()
root.wm_title("Приветствие")

label = tk.Label(root, text='Введите ваше имя: ')
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root,text='Отправить', command=username)
button.pack()

root.mainloop()

