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
    tree.column("#2", width=200, anchor="center")
    tree.column("#3", width=500, anchor="center")
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

    def dis_nowcoder():
        try:
            x = tree.get_children()
            for item in x:
                tree.delete(item)
        except:
            pass
        tree.heading("#1", text="No")
        tree.heading("#2", text="Username")
        tree.heading("#3", text="University")
        tree.heading("#4", text="Rating")
        ls = utils.getRanking("nowcoder")
        for i in range(30):
            lls = ls[i]
            tree.insert("", "end", values=(lls[0], lls[1], lls[2], lls[3]))
        tree.pack()

    def dis_codeforces():
        try:
            x = tree.get_children()
            for item in x:
                tree.delete(item)
        except:
            pass
        tree.heading("#1", text="No")
        tree.heading("#2", text="Username")
        tree.heading("#3", text="Number of participation")
        tree.heading("#4", text="Rating")
        ls = utils.getRanking("codeforces")
        for i in range(30):
            lls = ls[i]
            tree.insert("", "end", values=(lls[0], lls[1], lls[2], lls[3]))
        tree.pack()

    dis_wlacm()

    Button(viewRanking, text="wlacm", width=27, height=2, relief=GROOVE, command=dis_wlacm).place(x=0, y=387)
    Button(viewRanking, text="atcoder", width=27, height=2, relief=GROOVE, command=dis_atcoder).place(x=201, y=387)
    Button(viewRanking, text="nowcoder", width=27, height=2, relief=GROOVE, command=dis_nowcoder).place(x=401, y=387)
    Button(viewRanking, text="codeforces", width=27, height=2, relief=GROOVE, command=dis_codeforces).place(x=601, y=387)
    viewRanking.mainloop()

def displayAC():
    viewRanking = Tk()
    viewRanking.title("Ranking Board")
    viewRanking.geometry('553x433')
    viewRanking.minsize(553, 433)
    viewRanking.maxsize(553, 433)

    tree = ttk.Treeview(viewRanking, show="headings", height=18, columns=("#1", "#2", "#3", "#4","#5","#6"))
    tree.column("#1", width=50, anchor="center")
    tree.column("#2", width=100, anchor="center")
    tree.column("#3", width=100, anchor="center")
    tree.column("#4", width=50, anchor="center")
    tree.column("#5", width=100, anchor="center")
    tree.column("#6", width=150, anchor="center")


    def dis_wlacm():
        try:
            x = tree.get_children()
            for item in x:
                tree.delete(item)
        except:
            pass
        tree.heading("#1", text="No")
        tree.heading("#2", text="Stu Id")
        tree.heading("#3", text="length")
        tree.heading("#4", text="Language")
        tree.heading("#5", text="Size")
        tree.heading("#6", text="Time")
        ls = utils.getAC("wlacm")
        for i in range(20):
            lls = ls[i]
            tree.insert("", "end", values=(lls[0], lls[1], lls[2], lls[3],lls[4],lls[5]))
        tree.pack()


    dis_wlacm()

    Button(viewRanking, text="wlacm", width=30, height=2, relief=GROOVE, command=dis_wlacm).place(x=0, y=387)
    viewRanking.mainloop()

def displaySearch():
    viewSearch = Tk()
    viewSearch.title("Ranking Board")
    viewSearch.geometry('553x433')
    viewSearch.minsize(553, 433)
    viewSearch.maxsize(553, 433)

    def onClick():
        E1.get()
        #

    tree = ttk.Treeview(viewSearch, show="headings", height=18, columns=("#1", "#2", "#3", "#4", "#5", "#6"))
    tree.column("#1", width=50, anchor="center")
    tree.column("#2", width=100, anchor="center")
    tree.column("#3", width=100, anchor="center")
    tree.column("#4", width=50, anchor="center")
    tree.column("#5", width=100, anchor="center")
    tree.column("#6", width=150, anchor="center")

    E1=Entry(viewSearch,text="please input username")
    E1.place(x=0, y=387)
    Button(viewSearch, text="Search", width=30, height=2, relief=GROOVE, command=onClick).place(x=200, y=387)
    viewSearch.mainloop()



def main():
    window = Tk()
    window.title('李贇奇2021037100')
    window.geometry('300x230')

    Label(window, text="=== MENU ===").pack()
    Button(window, text="Competition Calendar", width=30, height=2, relief=GROOVE,command=displayCalendar).pack()
    Button(window, text="Ranking Board", width=30, height=2, relief=GROOVE,command=displayRanking).pack()
    Button(window, text="AC status", width=30, height=2, relief=GROOVE,command=displayAC).pack()
    Button(window, text="Search", width=30, height=2, relief=GROOVE, command=displaySearch).pack()
    window.mainloop()


if __name__ == "__main__":
    main()
