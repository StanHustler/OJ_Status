import os
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import time
import utils


def displayCalendar():
    viewCalendar = Tk()
    viewCalendar.title("Competition Calendar")
    viewCalendar.geometry('1083x427')
    tree = ttk.Treeview(viewCalendar, show="headings", height=18,
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

    calendar = utils.Calendar(utils.nowMonth(), utils.timeStamp())

    ls = calendar.getCalendar()

    def plant(ls):

        try:
            x = tree.get_children()

            for item in x:
                tree.delete(item)
        except:
            pass

        for i in range(len(ls)):
            dic = ls[i]

            tree.insert("", "end", values=(
                i + 1,
                dic["contestName"],
                dic["ojName"],
                utils.timestamp2time(str(dic["startTime"])[:-3]),
                utils.timestamp2time(str(dic["endTime"])[:-3]),
                dic["link"].split("?")[0]
            ))

    def prev():
        raw_date = calendar.date.split("-")
        rawY = raw_date[0]
        rawM = raw_date[1]
        if rawM == "1":
            rawM = "12"
            rawY = str(int(rawY) - 1)
        calendar.date = rawY + "-" + str(int(rawM) - 1)
        calendar.second = utils.timeStamp()

        ls = calendar.getCalendar()
        plant(ls)

    def next():
        raw_date = calendar.date.split("-")
        rawY = raw_date[0]
        rawM = raw_date[1]
        if rawM == "12":
            rawM = "1"
            rawY = str(int(rawY) + 1)
        calendar.date = rawY + "-" + str(int(rawM) + 1)
        calendar.second = utils.timeStamp()

        ls = calendar.getCalendar()
        plant(ls)

    plant(ls)
    tree.pack()
    Button(viewCalendar, text="Prev", height=2, relief=GROOVE, command=prev).place(x=0, y=387, width=542)
    Button(viewCalendar, text="Prev", width=28, height=2, relief=GROOVE, command=next).place(x=542, y=387, width=542)
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

    Button(viewRanking,
           text="wlacm", width=28, height=2, relief=GROOVE, command=dis_wlacm).place(x=0, y=387)
    Button(viewRanking,
           text="atcoder", width=28, height=2, relief=GROOVE, command=dis_atcoder).place(x=201, y=387)
    Button(viewRanking,
           text="nowcoder", width=28, height=2, relief=GROOVE, command=dis_nowcoder).place(x=401, y=387)
    Button(viewRanking,
           text="codeforces", width=28, height=2, relief=GROOVE, command=dis_codeforces).place(x=601, y=387)
    viewRanking.mainloop()


def displayAC():
    viewRanking = Tk()
    viewRanking.title("Ranking Board")
    viewRanking.geometry('553x433')
    viewRanking.minsize(553, 433)
    viewRanking.maxsize(553, 433)

    tree = ttk.Treeview(viewRanking, show="headings", height=18, columns=("#1", "#2", "#3", "#4", "#5", "#6"))
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
            tree.insert("", "end", values=(lls[0], lls[1], lls[2], lls[3], lls[4], lls[5]))
        tree.pack()

    dis_wlacm()

    Button(viewRanking, text="wlacm", width=30, height=2, relief=GROOVE, command=dis_wlacm).place(x=0, y=387)
    viewRanking.mainloop()


def displaySearch():
    viewSearch = Tk()
    viewSearch.title("Search")
    viewSearch.geometry('600x185')
    viewSearch.minsize(600, 185)
    viewSearch.maxsize(600, 185)

    def onClick():
        res = utils.getSearch(E1.get().strip())
        print(E1.get())
        if "atcoder" in res.keys():
            tree1 = ttk.Treeview(viewSearch, show="headings", height=1, columns=("#1", "#2", "#3", "#4", "#5"))
            tree1.column("#1", width=100, anchor="center")
            tree1.column("#2", width=200, anchor="center")
            tree1.column("#3", width=100, anchor="center")
            tree1.column("#4", width=100, anchor="center")
            tree1.column("#5", width=100, anchor="center")
            tree1.heading("#1", text="OJ")
            tree1.heading("#2", text="username")
            tree1.heading("#3", text="rank")
            tree1.heading("#4", text="rating")
            tree1.heading("#5", text="match")
            tree1.insert("", "end", values=(['atcoder'] + res["atcoder"]))
        else:
            tree1 = ttk.Treeview(viewSearch, show="headings", height=1, columns=("#1"))
            tree1.column("#1", width=600, anchor="center")
            tree1.heading("#1", text="atcoder")
            tree1.insert("", "end", values=(['No Result']))
        tree1.pack()

        if "wlacm" in res.keys():
            tree2 = ttk.Treeview(viewSearch, show="headings", height=1, columns=("#1", "#2", "#3", "#4", "#5", "#6"))
            tree2.column("#1", width=100, anchor="center")
            tree2.column("#2", width=100, anchor="center")
            tree2.column("#3", width=100, anchor="center")
            tree2.column("#4", width=100, anchor="center")
            tree2.column("#5", width=100, anchor="center")
            tree2.column("#6", width=100, anchor="center")
            tree2.heading("#1", text="OJ")
            tree2.heading("#2", text="username")
            tree2.heading("#3", text="rank")
            tree2.heading("#4", text="solved")
            tree2.heading("#5", text="submit")
            tree2.heading("#6", text="AC")
            tree2.insert("", "end", values=(['wlacm'] + res["wlacm"]))
        else:
            tree2 = ttk.Treeview(viewSearch, show="headings", height=1, columns=("#1"))
            tree2.column("#1", width=600, anchor="center")
            tree2.heading("#1", text="wlacm")
            tree2.insert("", "end", values=(['No Result']))
        tree2.pack()

        if "codeforces" in res.keys():
            tree3 = ttk.Treeview(viewSearch, show="headings", height=1, columns=("#1", "#2", "#3", "#4"))
            tree3.column("#1", width=100, anchor="center")
            tree3.column("#2", width=300, anchor="center")
            tree3.column("#3", width=100, anchor="center")
            tree3.column("#4", width=100, anchor="center")
            tree3.heading("#1", text="OJ")
            tree3.heading("#2", text="username")
            tree3.heading("#3", text="Rating")
            tree3.heading("#4", text="AC")
            tree3.insert("", "end", values=(['codeforces'] + res["codeforces"]))
        else:
            tree3 = ttk.Treeview(viewSearch, show="headings", height=1, columns=("#1"))
            tree3.column("#1", width=600, anchor="center")
            tree3.heading("#1", text="codeforces")
            tree3.insert("", "end", values=(['No Result']))
        tree3.pack()

    E1 = Entry(viewSearch)
    E1.place(x=0, y=141, width=400, height=47)
    Button(viewSearch, text="Search", width=30, height=2, relief=GROOVE, command=onClick).place(x=400, y=141)
    viewSearch.mainloop()


def main():
    window = Tk()
    window.title('李贇奇2021037100')
    window.geometry('300x230')

    Label(window, text="=== MENU ===").pack()
    Button(window, text="Competition Calendar", width=30, height=2, relief=GROOVE, command=displayCalendar).pack()
    Button(window, text="Ranking Board", width=30, height=2, relief=GROOVE, command=displayRanking).pack()
    Button(window, text="AC status", width=30, height=2, relief=GROOVE, command=displayAC).pack()
    Button(window, text="Search", width=30, height=2, relief=GROOVE, command=displaySearch).pack()
    window.mainloop()


if __name__ == "__main__":
    main()
