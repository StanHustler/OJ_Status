import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable


def getHTMLText(url):
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
            'Referer': 'https://www.baidu.com/link?url=nV__VLzaxpWPJBmpmsyh_0ZOHmnauP8Qm4cDGfbb0Um3COrclHlbrr4FDfBJBzqU_bbMhuUsRpC7iqjskDMbkq&wd=&eqid=e43c8e050005decb0000000561cc5120',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "connect error"


class Calendar:
    url = "https://contests.sdutacm.cn/contests.json"

    def getCalendar(url=url):
        t = PrettyTable(["Id", "Name", "Source", "start_time", "end_time", "link"])
        ls = eval(getHTMLText(url))

        for i in range(len(ls)):
            dic = ls[i]

            t.add_row(
                [
                    i + 1,
                    dic["name"][:25],
                    dic["source"],
                    dic["start_time"].replace("T", " ").replace("+", "~"),
                    dic["end_time"].replace("T", " ").replace("+", "~"),
                    dic["link"]
                ]
            )
        t.align = "l"
        return t

# print(Calendar.getCalendar())
