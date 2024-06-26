from tkinter import *
from functools import partial
from re import search
from math import factorial as fac


window = Tk()
window.title("calculator.")
window.config(background="black")


num_pad = Frame(window)
operator_pad = Frame(window)

mode = "pos"

input_box = Entry(window,
                  fg="light green",
                  bg="black",
                  width=17,
                  font=("dahlia", 12),
                  borderwidth=5,
                  )


def main():
    btn_style = {'bg': 'black', 'fg': 'grey', 'font': ('dahlia', 30)}

    for i in range(9):
        row, col = i // 3, i % 3
        Button(num_pad,
               text=str(i + 1),
               command=partial(enter_number, str(i+1)),
               **btn_style,
               ).grid(row=row, column=col)

    Button(num_pad,
           text="0",
           command=partial(enter_number, "0"),
           **btn_style
           ).grid(row=3, column=1)

    Button(num_pad,
           text="+/-",
           command=toggle_mode,
           font=('dahlia', 15),
           **{k: v for k, v in btn_style.items() if k != 'font'}
           ).grid(row=3, column=0, sticky="WESN")

    Button(num_pad,
           text=".",
           **btn_style,
           command=partial(enter_number, ".")
           ).grid(row=3, column=2, sticky="WESN")

    for row, operator in enumerate(["+", "-", "x", "="]):
        Button(operator_pad,
               text=operator,
               **btn_style,
               command=partial(enter_number, operator)
               ).grid(row=row, column=0, sticky="WESN")

    Button(window,
           text="clear",
           command=partial(input_box.delete, 0, END),
           font=('dahlia', 15),
           **{k: v for k, v in btn_style.items() if k != 'font'}
           ).grid(row=1, column=0, columnspan=1, sticky="WESN")

    Button(window,
           text="n!",
           command=factorial,
           font=('dahlia', 15),
           **{k: v for k, v in btn_style.items() if k != 'font'}
           ).grid(row=1, column=1, sticky="WESN")


    input_box.grid(row=0, column=0, columnspan=2, sticky="WESN")
    num_pad.grid(row=2, column=0, sticky="WESN")
    operator_pad.grid(row=2, column=1, sticky="WESN")

    window.mainloop()


def enter_number(n):
    if input_box.get() == "invalid equation.":
        input_box.delete(0, END)
    elif n == "=":
        equation = input_box.get()
        if search(r"^(\-?\d+(\.\d+)?[\+|\-|\*|\/])+\d+(\.\d+)?=?$", equation):
            input_box.delete(0, END)
            input_box.insert(0, eval(equation))
            return eval(equation)
        else:
            input_box.delete(0, END)
            input_box.insert(0, "invalid equation.")
    else:
        if n == "x":
            input_box.insert(END, "*")
        else:
            input_box.insert(END, n)


def toggle_mode():
    global mode
    if mode == "pos":
        input_box.insert(0, "-")
        mode = "neg"
        return mode
    elif mode == "neg":
        input_box.delete(0)
        mode = "pos"
        return mode


def factorial():
    if not input_box.get().isdigit():
        if search(r"^(\-?\d+(\.\d+)?[\+|\-|\*|\/])+\d+(\.\d+)?$", input_box.get()):
            n = fac(int(eval(input_box.get())))
            input_box.delete(0, END)
            input_box.insert(0, n)
            return n
        else:
            input_box.delete(0, END)
            input_box.insert(0, "invalid equation.")
            return "invalid equation."
    else:
        n = fac(int(input_box.get()))
        input_box.delete(0, END)
        input_box.insert(0, n)
        return n


if __name__ == "__main__":
    main()
