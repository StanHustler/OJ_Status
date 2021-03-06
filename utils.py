import requests
from bs4 import BeautifulSoup
import re
import datetime
import time
import json
import xlwt


class setting:
    ##calendar##
    calendar_url = "https://ac.nowcoder.com/acm/calendar/contest?token=&month="
    ##rank##
    atcoder_rank = "https://atcoder.jp/ranking"
    wlacm_rank = "http://wlacm.com/ranklist.php"
    nowcoder_rank = "https://ac.nowcoder.com/acm/contest/rating-index"
    codeforces_rank = "https://codeforces.com/ratings"
    ##AC##
    wlacm_AC = "http://wlacm.com/status.php?&jresult=4"
    # PTA_AC = "https://pintia.cn/problem-sets/1470579156098625536/submissions"
    # nowcoder_AC = "https://ac.nowcoder.com/acm/contest/26012#submit"
    ##search##
    atcoder_search = "https://atcoder.jp/users/"
    wlacm_search = "http://wlacm.com/userinfo.php?user="
    codeforces_search = "https://codeforces.com/profile/"


def getHTMLText(url, *cookie):
    try:
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
        }
        if len(cookie) != 0:
            headers['cookie'] = cookie[0]
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "connect error"


def isChinese(str):
    for i in str:
        if i >= '\u4e00' and i <= '\u9fa5':
            return True
    return False


def timestamp2time(timestamp):
    time_local = time.localtime(int(timestamp))
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt


def nowMonth():
    # date format: yyyy-mm
    res = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month)
    return res


def timeStamp():
    second = '{:.3f}'.format(time.time())
    second = str(second).replace(".", "")
    return second

def exportExcel(ls,name):
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet(name)
    for i in range(len(ls)):
        for j in range(len(ls[i].values())):
            lls=list(ls[i].values())
            worksheet.write(i, j, lls[j])
    workbook.save('C:\\Users\\Stan\\Desktop\\'+name+ '.xls')

class Calendar:

    def __init__(self, date, second):
        self.date = date
        self.second = second

    def getCalendar(self):
        html = getHTMLText(setting.calendar_url + self.date+"&_="+self.second)
        print(setting.calendar_url + self.date+"&_="+self.second)
        data=json.loads(html)['data']
        return data


def getRanking(OJ):
    ls = []
    if OJ == "atcoder":
        html = getHTMLText(setting.atcoder_rank)
        soup = BeautifulSoup(html, "html.parser")
        for i in range(len(soup.tbody("tr"))):
            frag = soup.tbody("tr")[i]("td")
            ls.append(
                [
                    frag[0].text,
                    frag[1]("a")[1].text,
                    frag[1]("a")[2].text,
                    frag[3].text
                ]
            )
    elif OJ == "wlacm":
        html = getHTMLText(setting.wlacm_rank)
        soup = BeautifulSoup(html, "html.parser")
        for i in range(len(soup.tbody("tr"))):
            frag = soup.tbody("tr")[i]("td")
            ls.append(
                [
                    frag[0].text.strip(),
                    frag[1].text,
                    frag[2].text,
                    frag[3].text
                ]
            )
    elif OJ == "nowcoder":
        html = getHTMLText(setting.nowcoder_rank)
        soup = BeautifulSoup(html, "html.parser")
        for i in range(len(soup.tbody("tr"))):
            frag = soup.tbody("tr")[i]("td")
            ls.append(
                [
                    frag[0].text.strip(),
                    frag[1].span.text,
                    frag[2].text.strip("\n"),
                    frag[4].text
                ]
            )
    elif OJ == "codeforces":
        html = getHTMLText(setting.codeforces_rank)
        soup = BeautifulSoup(html, "html.parser")
        frag = soup("div", {"class": "datatable ratingsDatatable"})[0]("tr")[1]("td")
        for i in range(0, len(frag), 4):
            try:
                ls.append(
                    [
                        frag[0 + i].text.strip(),
                        frag[1 + i].text.strip(),
                        frag[2 + i].text.strip(),
                        frag[3 + i].text.strip()
                    ]
                )
            except:
                pass
    return ls


def getAC(OJ):
    ls = []
    if OJ == "wlacm":
        html = getHTMLText(setting.wlacm_AC)
        soup = BeautifulSoup(html, "html.parser")
        for i in range(len(soup.tbody("tr"))):
            frag = soup.tbody("tr")[i]("td")
            ls.append(
                [
                    frag[0].text.strip(),
                    frag[1].text,
                    frag[4].text,
                    frag[6].text,
                    frag[7].text,
                    frag[8].text
                ]
            )
    # TODO
    # elif OJ == "PTA":
    #     with open("cookies.json", "r") as f:
    #         cookie = eval(f.read())["PTA"]
    #     html = getHTMLText(setting.PTA_AC, cookie)
    #     soup = BeautifulSoup(html, "html.parser")
    #     return soup
    return ls


def getSearch(username):
    res = {}

    # atcoder
    html = getHTMLText(setting.atcoder_search + username)
    soup = BeautifulSoup(html, "html.parser")
    try:
        src = soup("table", {"class": "dl-table"})[1]("tr")
        res["atcoder"] = [
            username,  # username
            src[0].td.text,  # rank
            src[1].td.text.replace("\n", ""),  # rating
            src[3].td.text  # match
        ]
    except:
        pass

    # wlacm
    html = getHTMLText(setting.wlacm_search + "".join(re.findall(r'\d+', username)))
    soup = BeautifulSoup(html, "html.parser")
    try:
        src = soup("table", {"id": "statics"})[0]("tr")
        res["wlacm"] = [
            soup.caption.text.split("--")[1],  # username
            re.search(r'>[0-9]{1,}<', str(src[0]('td')[1])).group(0)[1:-1],  # rank
            src[1]('td')[1].text.strip(),  # solved
            src[2]('td')[1].text,  # submit
            src[3]('td')[1].text  # AC
        ]
    except:
        pass

    # codeforces
    html = getHTMLText(setting.codeforces_search + username)
    soup = BeautifulSoup(html, "html.parser")
    try:
        res["codeforces"] = [
            username,  # username
            soup("span", {"style": "font-weight:bold;"})[0].text,  # rating
            soup("div", {"class": "_UserActivityFrame_counterValue"})[0].text.split()[0],  # AC
        ]
    except:
        pass
    return res


