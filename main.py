import os
import tkinter as tk
import tkinter.messagebox
import utils

def main():


    window = tk.Tk()
    window.title('李贇奇2021037100')
    window.geometry('300x230')

    def displayCalendar():
        viewCalendar = tk.Tk()
        viewCalendar.title("Competition Calendar")
        viewCalendar.geometry('1175x745')
        tk.Label(viewCalendar, text=utils.Calendar.getCalendar()).pack()

    tk.Label(window,text="==>Competition Calendar<==").pack()
    tk.Button(window, text="点我", command=displayCalendar).pack()

    window.mainloop()


if __name__ == "__main__":
    main()