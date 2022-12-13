import tkinter as tk

# создаем окно
win = tk.Tk()
win.geometry(f"225x270+100+200")
win['bg'] = '#ccccff'
win.title('Калькулятор')

# создаем поле ввода
calc = tk.Entry(win, justify=tk.RIGHT)
calc.grid(row=0, column=0, columnspan=4, stick='we')


# функции для кнопок
def add_digit(digit):
    val = calc.get() + str(digit)
    calc.delete(0, tk.END)
    calc.insert(0, val)


def get_oper(operation):
    val = calc.get()
    if val[-1] in '-+/*':
        val = val[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, val + operation)

def calculate():
    val = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, eval(val))

def clear():
    calc.delete(0, tk.END)
    calc.insert(0,'0')


def make_digit_btn(digit):
    return tk.Button(text=digit, command=lambda: add_digit(digit))


def make_operation_btn(operation):
    return tk.Button(text=operation, command=lambda: get_oper(operation))


def make_calc_btn(operation):
    return tk.Button(text=operation, command=calculate)

def make_clear_btn(operation):
    return tk.Button(text=operation, command=clear)


# создание кнопок
make_digit_btn('1').grid(row=1, column=0, stick='wens')
make_digit_btn('2').grid(row=1, column=1, stick='wens')
make_digit_btn('3').grid(row=1, column=2, stick='wens')
make_digit_btn('4').grid(row=2, column=0, stick='wens')
make_digit_btn('5').grid(row=2, column=1, stick='wens')
make_digit_btn('6').grid(row=2, column=2, stick='wens')
make_digit_btn('7').grid(row=3, column=0, stick='wens')
make_digit_btn('8').grid(row=3, column=1, stick='wens')
make_digit_btn('9').grid(row=3, column=2, stick='wens')
make_digit_btn('0').grid(row=4, column=0, stick='wens')

make_operation_btn('+').grid(row=1, column=3, stick='wens')
make_operation_btn('-').grid(row=2, column=3, stick='wens')
make_operation_btn('*').grid(row=3, column=3, stick='wens')
make_operation_btn('/').grid(row=4, column=3, stick='wens')

make_calc_btn('=').grid(row=4, column=2, stick='wens')

make_clear_btn('AC').grid(row=4, column=1, stick='wens')

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

# вызов функции для отрисовки окна
win.mainloop()
