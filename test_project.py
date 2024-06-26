from tkinter import *
from project import mode, input_box, enter_number, toggle_mode, factorial


def test_enter_number():
    enter_number("1+2")
    assert enter_number("=") == 3
    input_box.delete(0, END)

    enter_number("2.5+2.5")
    assert enter_number("=") == 5.0
    input_box.delete(0, END)

    enter_number("5+5+5-10+5")
    assert enter_number("=") == 10
    input_box.delete(0, END)


def test_toggle_mode():
    global mode
    mode = "pos"
    assert toggle_mode() == "neg"
    assert input_box.get()[0] == "-"

    assert toggle_mode() == "pos"
    assert input_box.get() == ""


def test_factorial():
    input_box.insert(0, "3")
    assert factorial() == 6
    input_box.delete(0, END)

    input_box.insert(0, "2*2+1")
    assert factorial() == 120
