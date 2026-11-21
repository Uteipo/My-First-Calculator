import tkinter as tk 
window = tk.Tk()
window.title('Калькулятор бета')
window.geometry ('300x400')
display = tk.Entry(window, font=('Arial', 20),  justify='right', takefocus= 0)
display.pack(fill='x', padx=10, pady=10) 
display.bind('<Button-1>', lambda e: 'break')
Frame = tk.Frame(window)
Frame.pack()
btn_7= tk.Button(Frame, text='7',bg='white', fg='black', command=lambda:display.insert(tk.END, '7'), width=5, height=2, font=('Arial', 14))
btn_7.grid(row=0, column=0, padx=5, pady=5)
btn_8= tk.Button(Frame, text='8',bg='white', fg='black', command=lambda:display.insert(tk.END, '8'), width=5, height=2, font=('Arial', 14))
btn_8.grid(row=0, column=1, padx=5, pady=5)
btn_9= tk.Button(Frame, text='9',bg='white', fg='black', command=lambda:display.insert(tk.END, '9'), width=5, height=2, font=('Arial', 14))
btn_9.grid(row=0, column=2, padx=5, pady=5)
btn_4= tk.Button(Frame, text='4',bg='white', fg='black', command=lambda:display.insert(tk.END, '4'), width=5, height=2, font=('Arial', 14))
btn_4.grid(row=1, column=0, padx=5, pady=5)
btn_5= tk.Button(Frame, text='5',bg='white', fg='black', command=lambda:display.insert(tk.END, '5'), width=5, height=2, font=('Arial', 14))
btn_5.grid(row=1, column=1, padx=5, pady=5)
btn_6= tk.Button(Frame, text='6',bg='white', fg='black', command=lambda:display.insert(tk.END, '6'), width=5, height=2, font=('Arial', 14))
btn_6.grid(row=1, column=2, padx=5, pady=5)
btn_1= tk.Button(Frame, text='1',bg='white', fg='black', command=lambda:display.insert(tk.END, '1'), width=5, height=2, font=('Arial', 14))
btn_1.grid(row=2, column=0, padx=5, pady=5)
btn_2= tk.Button(Frame, text='2',bg='white', fg='black', command=lambda:display.insert(tk.END, '2'), width=5, height=2, font=('Arial', 14))
btn_2.grid(row=2, column=1, padx=5, pady=5)
btn_3= tk.Button(Frame, text='3',bg='white', fg='black', command=lambda:display.insert(tk.END, '3'), width=5, height=2, font=('Arial', 14))
btn_3.grid(row=2, column=2, padx=5, pady=5)
btn_0= tk.Button(Frame, text='0',bg='white', fg='black', command=lambda:display.insert(tk.END, '0'), width=5, height=2, font=('Arial', 14))
btn_0.grid(row=3, column=1, padx=5, pady=5)
btn_plus= tk.Button(Frame, text='+',bg='white', fg='black', command=lambda:display.insert(tk.END, '+'), width=5, height=2, font=('Arial', 14))
btn_plus.grid(row=0, column=3, padx=5, pady=5)
btn_minus= tk.Button(Frame, text='-',bg='white', fg='black', command=lambda:display.insert(tk.END, '-'), width=5, height=2, font=('Arial', 14))
btn_minus.grid(row=1, column=3, padx=5, pady=5)
btn_mul= tk.Button(Frame, text='*',bg='white', fg='black', command=lambda:display.insert(tk.END, '*'), width=5, height=2, font=('Arial', 14))
btn_mul.grid(row=2, column=3, padx=5, pady=5)
btn_div= tk.Button(Frame, text='/',bg='white', fg='black', command=lambda:display.insert(tk.END, '/'), width=5, height=2, font=('Arial', 14)) 
btn_div.grid(row=3, column=3, padx=5, pady=5)
def calculate():
    try:    
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, 'Ошибка')    
btn_equal = tk.Button(Frame, text='=',bg='white', fg='black', command=calculate, width=5, height=2, font=('Arial', 14))
btn_equal.grid(row=3, column=2, padx=5, pady=5)
def clear_display():
    display.delete(0, tk.END)
btn_clear = tk.Button(Frame,text= 'C',bg='white', fg='black', command=clear_display, width=5, height=2, font=('Arial', 14))
btn_clear.grid(row=3, column=0, padx=5, pady=5)
def key_press(event):
    allowed_chars = '0123456789+-*/.'

    if event.keysym == 'BackSpace':
        current_text = display.get()
        if len(current_text) > 0:
            display.delete(len(current_text) - 1, tk.END)

    elif event.keysym in ('Return', 'KP_Enter'):
        calculate()

    elif event.keysym == 'Escape':
        clear_display()

    elif event.char in allowed_chars and event.char != '':
        display.insert(tk.END, event.char)

window.bind('<Key>', key_press)
window.mainloop()

