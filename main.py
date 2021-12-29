import os
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import utils


def main():
    window = tk.Tk()
    window.title('李贇奇2021037100')
    window.geometry('300x230')

    def displayCalendar():
        viewCalendar = tk.Tk()
        viewCalendar.title("Competition Calendar")
        viewCalendar.geometry('1083x427')
        tree = ttk.Treeview(viewCalendar, show="headings",height=20,
                            columns=("id", "name", "source", "start_time", "end_time", "link"))
        tree.column("id", width=40, anchor="center")
        tree.column("name", width=350, anchor="center")
        tree.column("source", width=100, anchor="center")
        tree.column("start_time", width=145, anchor="center")
        tree.column("end_time", width=145, anchor="center")
        tree.column("link", width=300, anchor="center")

        tree.heading("id", text="ID")
        tree.heading("name", text="Name")
        tree.heading("source", text="Source")
        tree.heading("start_time", text="Start time")
        tree.heading("end_time", text="End time")
        tree.heading("link", text="Link")
        ls = utils.getCalendar(utils.setting.calendar_url)
        for i in range(len(ls)):
            dic = ls[i]

            tree.insert("", "end", values=(
                i + 1,
                dic["name"],
                dic["source"],
                dic["start_time"].replace("T", " ").split("+")[0],
                dic["end_time"].replace("T", " ").split("+")[0],
                dic["link"]
            ))
        tree.pack()
        viewCalendar.mainloop()

    tk.Label(window, text="==>Competition Calendar<==").pack()
    tk.Button(window, text="点我", command=displayCalendar).pack()

    window.mainloop()


if __name__ == "__main__":
    main()
