import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

root = tk.Tk()
root.title('Aceitas?')
root.geometry('600x600')
root.configure(background="cyan")

move_count = 0  # Contador de movimentos

def move_button_1(e):
    global move_count  # Usar a variável global

    if move_count < 2:  # Verificar se o número de movimentos é menor que 2
        if abs(e.x - button_1.winfo_x()) < 58 and abs(e.y - button_1.winfo_y()) < 40:
            x = random.randint(0, root.winfo_width() - button_1.winfo_width())
            y = random.randint(0, root.winfo_height() - button_1.winfo_height())
            button_1.place(x=x, y=y)
            move_count += 1  # Incrementar o contador de movimentos

def show_options():
    root.withdraw()  # Esconde a janela atual
    options_window = tk.Toplevel()  # Cria uma nova janela
    options_window.title('Opções')
    options_window.geometry('600x600')  # Define as mesmas dimensões da primeira janela
    options_window.configure(background="cyan")

    option_label = Label(options_window, text='Escolha uma opção:', font=('Montserrat', 12, 'bold'), bg="cyan")
    option_label.pack()

    option1_button = Button(options_window, text='Opção 1', bg='#008b8b', relief=RIDGE, bd=3, command=option1_selected)
    option1_button.pack()

    option2_button = Button(options_window, text='Opção 2', bg='#008b8b', relief=RIDGE, bd=3, command=option2_selected)
    option2_button.pack()

def option1_selected():
    messagebox.showinfo('Opção 1', 'Você selecionou a opção 1')

def option2_selected():
    messagebox.showinfo('Opção 2', 'Você selecionou a opção 2')

def denied(e):
    messagebox.showinfo('Minha melhor amiga', 'Ok então')
    global move_count  # Usar a variável global
    x = random.randint(0, root.winfo_width() - button_1.winfo_width())
    y = random.randint(0, root.winfo_height() - button_1.winfo_height())
    button_1.place(x=x, y=y)
    move_count += 1  # Incrementar o contador de movimentos

    if move_count >= 2:  # Verificar se o número de movimentos é maior ou igual a 2
        root.unbind('')  # Remover o evento de movimento

def accepted():
    messagebox.showinfo('Minha melhor amiga', 'cafeteria essa semana?')
    show_options()

margin = Canvas(root, width=500, bg="cyan", height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()

text_id = Label(root, bg="cyan", text='Não era pra ter te ligado. Você me perdoa?', fg='#590d22',
                font=('Montserrat', 10, 'bold'))
text_id.pack()

button_1 = Button(root, text="Não", bg="#008b8b", command=lambda: denied(None), relief=RIDGE, bd=3,
                  font=('Montserrat', 8, 'bold'))
button_1.pack()

button_2 = Button(root, text="Sim", bg="#008b8b", relief=RIDGE, bd=3, command=accepted,
                  font=('Montserrat', 14, 'bold'))
button_2.pack()

root.bind('<Button-1>', move_button_1)
root.mainloop()
