import os
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import utils


def displayCalendar():
    viewCalendar = Tk()
    viewCalendar.title("Competition Calendar")
    viewCalendar.geometry('1083x427')
    tree = ttk.Treeview(viewCalendar, show="headings", height=20,
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
    ls = utils.getCalendar()
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


def displayRanking():
    viewRanking = Tk()
    viewRanking.title("Ranking Board")
    viewRanking.geometry('800x433')
    viewRanking.minsize(800, 433)
    viewRanking.maxsize(800, 433)

    tree = ttk.Treeview(viewRanking, show="headings", height=18, columns=("#1", "#2", "#3", "#4"))
    tree.column("#1", width=50, anchor="center")
    tree.column("#2", width=100, anchor="center")
    tree.column("#3", width=600, anchor="center")
    tree.column("#4", width=50, anchor="center")

    def dis_atcoder():
        try:
            x = tree.get_children()
            for item in x:
                tree.delete(item)
        except:
            pass

        tree.heading("#1", text="No")
        tree.heading("#2", text="Name")
        tree.heading("#3", text="University")
        tree.heading("#4", text="Rating")
        ls = utils.getRanking("atcoder")
        for i in range(30):
            lls = ls[i]
            tree.insert("", "end", values=(lls[0], lls[1], lls[2], lls[3]))
        tree.pack()

    def dis_wlacm():
        try:
            x = tree.get_children()
            for item in x:
                tree.delete(item)
        except:
            pass
        tree.heading("#1", text="No")
        tree.heading("#2", text="Stu Id")
        tree.heading("#3", text="User name")
        tree.heading("#4", text="AC")
        ls = utils.getRanking("wlacm")
        for i in range(30):
            lls = ls[i]
            tree.insert("", "end", values=(lls[0], lls[1], lls[2], lls[3]))
        tree.pack()
    dis_wlacm()
    Button(viewRanking, text="atcoder", width=30, height=2, command=dis_atcoder).place(x=0, y=387)
    Button(viewRanking, text="wlacm", width=10, height=2, command=dis_wlacm).place(x=220, y=387)
    # Button(viewRanking, text="atcoder", width=30, height=2, command="1").place(x = 0,y=387).pack()
    # Button(viewRanking, text="atcoder", width=30, height=2, command="1").place(x = 0,y=387).pack()
    # Button(viewRanking, text="atcoder", width=30, height=2, command="1").place(x = 0,y=387).pack()
    viewRanking.mainloop()


def main():
    window = Tk()
    window.title('李贇奇2021037100')
    window.geometry('300x230')

    Label(window, text="=== MENU ===").pack()
    Button(window, text="Competition Calendar", width=30, height=2, pady=1, relief=GROOVE,
           command=displayCalendar).pack()
    Button(window, text="Ranking Board", width=30, height=2, relief=GROOVE,
           command=displayRanking).pack()
    window.mainloop()


if __name__ == "__main__":
    main()
